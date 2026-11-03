ARG BUILD_FROM=ghcr.io/home-assistant/base:3.23
# checkov:skip=CKV_DOCKER_7: Base image is supplied by the Home Assistant builder via BUILD_FROM; the default above is pinned
FROM ${BUILD_FROM}

# Add env
ENV LANG=C.UTF-8

# Install requirements for app
RUN apk add --no-cache python3 py3-pyserial

# checkov:skip=CKV_DOCKER_3: Runs as root to access the host serial device passed in by the Supervisor

# Copy data
COPY rootfs /

LABEL \
    org.opencontainers.image.title="Home Assistant App: Tekmar Packet Server" \
    org.opencontainers.image.description="Communicate with the Tekmar Gateway 482" \
    org.opencontainers.image.source="https://github.com/WillCodeForCats/tekmar-packetserv" \
    org.opencontainers.image.licenses="MIT License"

# checkov:skip=CKV_DOCKER_2: Container lifecycle is managed by the Home Assistant Supervisor
