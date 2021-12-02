from config.settings.base import env

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    "default": env.db(),
}


def requirements():
    return {
        "docker": ["-p 5432:5432 postgres:14.0"],  # https://hub.docker.com/_/postgres
        "pip": ["psycopg2"],
    }
