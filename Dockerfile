# vim: ft=dockerfile

FROM kmkfw/base:latest

ENV LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8

# Create KMK directory structure
RUN mkdir -p /app
WORKDIR /app
COPY . .

# Install dependencies
RUN make devdeps submodules micropython-deps circuitpy-deps micropython-build-unix
