ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG=C.UTF-8

ARG TEMPIO_VERSION
ARG BUILD_ARCH

# Install tempio and Python dependencies in a single layer
RUN \
    # Install system packages
    apk add --no-cache \
        python3 \
        py3-pip \
        curl && \
    # Download and install tempio with error handling
    curl -sSLf -o /usr/bin/tempio \
        "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}" || \
        (echo "ERROR: Failed to download tempio from GitHub releases" && \
         echo "URL: https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}" && \
         echo "TEMPIO_VERSION: ${TEMPIO_VERSION}" && \
         echo "BUILD_ARCH: ${BUILD_ARCH}" && \
         exit 1) && \
    # Verify the download was successful and file exists
    test -f /usr/bin/tempio || \
        (echo "ERROR: tempio binary was not downloaded successfully" && exit 1) && \
    chmod +x /usr/bin/tempio && \
    # Install Python packages
    pip3 --no-cache-dir install pyserial==3.5 && \
    # Clean up
    rm -rf /var/cache/apk/*

COPY rootfs /
