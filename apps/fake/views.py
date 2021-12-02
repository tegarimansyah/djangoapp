import json
import os, random, time
from faker import Faker
from django.http import JsonResponse
from apps.utils.metrics import BUSINESS_COUNTER

fake = Faker()


def random(request):
    BUSINESS_COUNTER.labels("random").inc()
    return JsonResponse({"name": fake.name(), "address": fake.address()})


def delay(request):
    delay_ms = int(request.GET.get("delay", 0)) / 1000
    if delay_ms > 0:
        time.sleep(delay_ms)
        return JsonResponse({"delay": delay_ms})

    BUSINESS_COUNTER.labels("without_delay").inc()
    return JsonResponse({"delay": 0})
