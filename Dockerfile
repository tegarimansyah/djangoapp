# pull official base image
FROM python:3.8-slim-buster

# Create appuser && Working Directory
ENV USER=appuser
ENV UID=10001
# See https://stackoverflow.com/a/55757473/12429735RUN 
RUN adduser \    
    --disabled-password \    
    --gecos "" \    
    --home "/nonexistent" \    
    --shell "/sbin/nologin" \    
    --no-create-home \    
    --uid "${UID}" \    
    "${USER}" \
    && mkdir /code 

WORKDIR /app

# Set python-specific environment variables
# Prevent create byte code .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Allow Python log send to stream (STDOUT / STDERR) 
ENV PYTHONUNBUFFERED 1
# Timezone
ENV TZ Asia/Jakarta

# Install dependencies
COPY --chown=appuser:appuser requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install --no-install-recommends -y libpq-dev tini build-essential \
    && pip install --no-cache -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential

# copy project
COPY --chown=appuser:appuser . .

# Using USER created before
USER appuser

# Tell docker how the process PID 1 handle gracefully shutdown
# The default is SIGTERM, but some are not. Explicit is better
STOPSIGNAL SIGTERM

# Add Tini for Single Process per Container &  Signal Handling (PID 1)
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run program under Tini
CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000", "--log-level", "warning"]
