from .settings import *
import os

APP_ENV = os.environ.get("app_env", "DEV")

if APP_ENV == "DEV":
    # settings file for all other local may be
    from .develop import *
else:
    # settings file for production
    pass

