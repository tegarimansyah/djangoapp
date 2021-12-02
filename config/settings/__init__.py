from split_settings.tools import optional, include
from .base import DEBUG, DJANGO_ENV

include(
    "environment/{0}.py".format(DJANGO_ENV),
    "components/database.py",
    "components/prometheus.py",
    "components/healthcheck.py",
    # Installed app, middleware, etc
    "components/common.py",
)
