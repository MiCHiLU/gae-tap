# -*- coding: utf-8 -*-

from functools import wraps
import os
import sys

from google.appengine.api import lib_config
import webapp2


# Config

class ConfigDefaults(object):
  IS_TEST = "unittest" in sys.modules.keys()
  SITE_PACKAGES = "site-packages"

config = lib_config.register("warmup", ConfigDefaults.__dict__)


# Search Path

def execute_once(func):

  @wraps(func)
  def inner(_result=[None], *argv, **kwargv):
    if _result[0] is None:
      _result[0] = func(*argv, **kwargv)
      if _result[0] is None:
        raise ValueError("The return value must be not `None`.")
    return _result[0]

  return inner

@execute_once
def sys_path_append():
  try:
    import __main__ as main
  except ImportError:
    is_shell = False
  else:
    is_shell = not hasattr(main, "__file__")
  base_path = config.SITE_PACKAGES
  if config.IS_TEST or is_shell:
    base_path = os.path.abspath(base_path)
  path = base_path
  if path not in sys.path and os.path.exists(path):
    sys.path.append(path)
  if os.path.exists(base_path):
    path = os.path.join(base_path, "packages")
    if path not in sys.path:
      sys.path.append(path)
    if os.path.exists(path):
      for zipfile in os.listdir(path):
        if zipfile.endswith(".zip"):
          zipfile_path = os.path.join(path, zipfile)
          if zipfile_path not in sys.path:
            sys.path.append(zipfile_path)
  if is_shell or sys.argv[0].endswith("/sphinx-build"):
    import google
    base = os.path.join(os.path.dirname(google.__file__), "../lib/")
    for webapp2 in ["webapp2-2.5.2", "webapp2"]:
      path = os.path.join(base, webapp2)
      if os.path.exists(path):
        sys.path.append(path)
        break
    for path in ["endpoints-1.0", "protorpc-1.0", "jinja2"]:
      sys.path.append(os.path.join(base, path))
  elif config.IS_TEST:
    import google
    base = os.path.join(os.path.dirname(google.__file__), "../lib/")
    for path in ["endpoints-1.0"]:
      sys.path.append(os.path.join(base, path))
  return True
sys_path_append()


from js.angular import angular_cookies, angular_resource
from js.bootstrap import bootstrap
import tap

class WarmUp(tap.RequestHandler):

  @tap.head(angular_cookies, angular_resource, bootstrap)
  def get(self):
    pass

app = webapp2.WSGIApplication([
  ("/_ah/warmup", WarmUp),
])
