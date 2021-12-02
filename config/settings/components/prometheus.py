INSTALLED_APPS = [
    "django_prometheus",
]

MIDDLEWARE_FIRST = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
]

MIDDLEWARE_LAST = [
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

PROMETHEUS_EXPORT_MIGRATIONS = False
