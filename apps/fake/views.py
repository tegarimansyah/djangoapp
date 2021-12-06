import json
import os, random, time
from faker import Faker
from django.http import JsonResponse
from apps.utils.metrics import BUSINESS_COUNTER, BUSINESS_HISTOGRAM, APP_VERSION
from random import randrange

fake = Faker()


def random(request):
    rand_range=randrange(1200)
    BUSINESS_COUNTER.labels("random").inc()
    
    BUSINESS_HISTOGRAM.labels("random").observe(rand_range)
    return JsonResponse({"name": fake.name(), "address": fake.address(), "random_histogram": rand_range })

def setversion(request):
    version = request.GET.get("version", 0)
    APP_VERSION.labels(version).set(1)
    return JsonResponse({"version": version })


def delay(request):
    # rand_range=randrange(500)
    delay_ms = int(request.GET.get("delay", 0)) / 1000
    if delay_ms > 0:
        time.sleep(delay_ms)
        BUSINESS_HISTOGRAM.labels("delay").observe(int(request.GET.get("delay", 0)))
        return JsonResponse({"delay": delay_ms})

    BUSINESS_COUNTER.labels("without_delay").inc()
    # BUSINESS_HISTOGRAM.labels("delay").observe(rand_range)
    return JsonResponse({"delay": 0})
