ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG=C.UTF-8

# Install requirements for add-on
RUN \
    apk add --no-cache python3 \
    && apk add --no-cache py3-pip \
    && apk add --no-cache py3-pyserial

# Copy data
COPY rootfs /
