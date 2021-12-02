# Custom Metrics
from prometheus_client import Gauge, Counter
from config.settings.components.version import VERSION

# Create metrics
APP_VERSION = Gauge("myapp_app_version", "Application version", ["version"])
HEALTH = Gauge("myapp_health_latency", "Health Latency", ["instance"])
BUSINESS_COUNTER = Counter(
    "myapp_business_counter", "Business Counter", ["business_name"]
)

# Set metrics
current_version = ".".join((str(i) for i in VERSION))
APP_VERSION.labels(current_version).set(1)
