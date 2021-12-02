from config.settings.components import prometheus, healthcheck

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *prometheus.INSTALLED_APPS,
    *healthcheck.INSTALLED_APPS,
    # My App
    "apps.utils",
    "apps.fake",
]

MIDDLEWARE = [
    # *prometheus.MIDDLEWARE_FIRST,
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # *prometheus.MIDDLEWARE_LAST,
]
