ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG=C.UTF-8

# Install requirements for app
RUN apk add --no-cache python3 py3-pyserial

# Copy data
COPY rootfs /
