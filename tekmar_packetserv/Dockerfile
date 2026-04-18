ARG BUILD_FROM=ghcr.io/home-assistant/base:3.23
FROM ${BUILD_FROM}

# Add env
ENV LANG=C.UTF-8

# Install requirements for app
RUN apk add --no-cache python3 py3-pyserial

# Copy data
COPY rootfs /

LABEL \
    org.opencontainers.image.title: "Home Assistant App: Tekmar Packet Server" \
    org.opencontainers.image.description: "Communicate with the Tekmar Gateway 482" \
    org.opencontainers.image.source: "https://github.com/WillCodeForCats/tekmar-packetserv" \
    org.opencontainers.image.licenses: "MIT License"