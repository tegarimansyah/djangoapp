CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

def requirements():
    return {
        'docker': [ '-p 6379:6379 redis:5.0' ],
        'pip': [ 'django-redis' ],
    }