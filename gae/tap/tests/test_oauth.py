#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urlparse

import tests.util

from google.appengine.api import urlfetch_stub
from minimock import mock, restore
import pytest

import conf

def Dummy_RetrieveURL(self, url, payload, method, headers, request, response,
                      follow_redirects, deadline, validate_certificate):
  response.set_content("{}")

class OAuthTest(tests.util.TestCase):
  root_path = conf.root_path
  domain = "sample"

  def setUp(self):
    super(OAuthTest, self).setUp()
    mock("urlfetch_stub.URLFetchServiceStub._RetrieveURL", mock_obj=Dummy_RetrieveURL)

  def tearDown(self):
    restore()
    super(OAuthTest, self).tearDown()

  @pytest.mark.skipif('not sys.modules.has_key("simpleauth")',
                      reason="no exists simpleauth module")
  def test_oauth(self):
    if os.path.exists("gae/oauth_config"):
      response = self.app.get("/oauth/google", status=302)
      assert response.location.startswith("https://accounts.google.com/o/oauth2/auth?")
      state = urlparse.parse_qs(response.location)["state"][0]
      self.app.get("/oauth/google/callback?state={0}".format(state), status=500)
      self.expected_logs = [
        ('ERROR', 'lib/webapp2-2.5.2/webapp2.py', '_internal_error', "'access_token'"),
        ('WARNING', 'google/appengine/ext/ndb/tasklets.py', '_help_tasklet_along', "suspended generator _oauth2_callback(handler.py:230) raised KeyError('access_token')"),
      ]
    else:
      self.app.get("/oauth/google", status=401)
      self.expected_logs = [
        ('WARNING', 'gae/tap/ext.py', 'oauth_config', "import_string() failed for 'oauth_config.sample'. Possible reasons are:...\nOriginal exception:\n\nImportError: No module named oauth_config\n\nDebugged import:\n\n- 'oauth_config' not found."),
      ]

class OAuthSecretsTest(tests.util.TestCase):
  root_path = conf.root_path

  @pytest.mark.skipif('os.path.exists("gae/oauth_config/default.py")',
                      reason="exists gae/oauth_config/default.py")
  def test_secrets(self):
    self.app.get("/oauth/google", status=401)
    if sys.modules.has_key("simpleauth"):
      self.expected_logs = [
        ('WARNING', 'gae/tap/ext.py', 'oauth_config', "import_string() failed for 'oauth_config.localhost'. Possible reasons are...g' found in '.../gae/oauth_config/__init__.py...'.\n- 'oauth_config.localhost' not found."),
        ('ERROR', 'lib/webapp2-2.5.2/webapp2.py', '_internal_error', 'cannot import name default'),
      ]
      if not os.path.exists("gae/oauth_config"):
        self.expected_logs.extend([
          ('WARNING', 'gae/tap/ext.py', 'oauth_config', "import_string() failed for 'oauth_config.localhost'. ..."),
        ])

class OAuthSignoutTest(tests.util.TestCase):
  root_path = conf.root_path
  domain = "sample"
  use_cookie = True

  def test_signout(self):
    assert len(self.app.cookiejar) == 0
    self.app.put("/test/sessions")
    assert len(self.app.cookiejar) == 1
    for cookie in self.app.cookiejar:
      if cookie.name == "__s":
        assert cookie.value is not None
        value = cookie.value
        break
      else:
        raise
    self.app.get("/oauth/signout", status=401)
    assert len(self.app.cookiejar) == 1
    for cookie in self.app.cookiejar:
      if cookie.name == "__s":
        assert cookie.value == value
        break
      else:
        raise
    self.app.get("/oauth/signout", headers={"Referer":"http://sample/"})
    assert len(self.app.cookiejar) == 1
    for cookie in self.app.cookiejar:
      if cookie.name == "__s":
        assert cookie.value != value
        assert len(cookie.value) == 61
        break
      else:
        raise
    self.expected_logs = [
      ('WARNING', 'lib/webapp2-2.5.2/webapp2_extras/securecookie.py', 'deserialize', "Invalid cookie signature u'...'"),
    ]
    if not os.path.exists("gae/oauth_config"):
      self.expected_logs.extend([
        ('WARNING', 'gae/tap/ext.py', 'oauth_config', "import_string() failed for 'oauth_config.sample'. ..."),
      ])
