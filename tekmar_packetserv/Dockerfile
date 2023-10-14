ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

ARG TEMPIO_VERSION BUILD_ARCH
RUN \
    curl -sSLf -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Install requirements for add-on
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN pip3 --no-cache-dir install pyserial

COPY rootfs /
