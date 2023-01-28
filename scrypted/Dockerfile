ARG BASHIO_VERSION=0.14.3
ARG S6_OVERLAY_VERSION=2.1.0.2
ARG TEMPIO_VERSION=2021.09.0
ARG BUILD_ARCH=debian
ARG BASE="18-bullseye-full"
FROM koush/scrypted:${BASE}

ARG BASHIO_VERSION
ARG S6_OVERLAY_VERSION
ARG TEMPIO_VERSION
ARG BUILD_ARCH

# Make sure we run production build
ENV NODE_ENV production

# Install Nginx and a set of Home Assistant add-on tools
RUN \
    set -x \
    && apt-get update && apt-get install -y --no-install-recommends \
        bash \
        jq \
        tzdata \
        curl \
        ca-certificates \
        nginx-extras\
        libnginx-mod-http-lua\
    && mkdir -p /usr/share/man/man1 \
    \
    && if [ "${BUILD_ARCH}" = "armv7" ]; then \
            export S6_ARCH="arm"; \
        elif [ "${BUILD_ARCH}" = "i386" ]; then \
            export S6_ARCH="x86"; \
        else \
            export S6_ARCH="${BUILD_ARCH}"; \
        fi \
    \
    && curl -L -f -s "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-${S6_ARCH}.tar.gz" \
        | tar zxvf - -C / \
    && mkdir -p /etc/fix-attrs.d \
    && mkdir -p /etc/services.d \
    \
    && curl -L -f -s -o /usr/bin/tempio \
        "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}" \
    && chmod a+x /usr/bin/tempio \
    \
    && mkdir -p /usr/src/bashio \
    && curl -L -f -s "https://github.com/hassio-addons/bashio/archive/v${BASHIO_VERSION}.tar.gz" \
        | tar -xzf - --strip 1 -C /usr/src/bashio \
    && mv /usr/src/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/src/* \
    && apt-get autoremove

# This file is installed by NGINX as a default but we don't need it
RUN rm -rf /etc/nginx/sites-enabled/default

# Install Scrypted
WORKDIR /
ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
ARG SCRYPTED_INSTALL_VERSION="v0.6.10"
RUN test -n "$SCRYPTED_INSTALL_VERSION"
RUN npx -y scrypted@latest install-server ${SCRYPTED_INSTALL_VERSION}

# Copy root filesystem
COPY rootfs /

ENTRYPOINT ["/init"]
