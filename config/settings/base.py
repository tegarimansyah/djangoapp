import os
import environ

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG", default=True)
DJANGO_ENV = env("DJANGO_ENV", default="development")

if DEBUG:
    SECRET_KEY = env("SECRET_KEY", default="thisissupersecret")
else:
    SECRET_KEY = env("SECRET_KEY")
