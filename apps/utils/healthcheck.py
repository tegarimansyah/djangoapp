import time
import requests
from django.db import DatabaseError, IntegrityError

from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceReturnedUnexpectedResult, ServiceUnavailable

from health_check.db.models import TestModel

from apps.utils.metrics import HEALTH


class MyDatabaseBackend(BaseHealthCheckBackend):
    def check_status(self):
        try:
            start = time.time()

            # Check the db
            obj = TestModel.objects.create(title="test")
            obj.title = "newtest"
            obj.save()
            obj.delete()

            # Set to prometheus
            end = time.time()
            HEALTH.labels("database").set(end - start)
        except IntegrityError:
            raise ServiceReturnedUnexpectedResult("Integrity Error")
        except DatabaseError:
            raise ServiceUnavailable("Database error")


class HTTPBinCheck(BaseHealthCheckBackend):
    def check_status(self):
        try:
            start = time.time()

            # Check the db
            requests.get("https://httpbin.org/get/")

            # Set to prometheus
            end = time.time()
            HEALTH.labels("HTTPBin").set(end - start)
        except Exception as e:
            raise ServiceUnavailable(e)
