#!/usr/bin/env bash

# Build configuration
IMG_BUILD_TAG="pipe_config_logging:0.1";

# Construct and execute command
# Note: Remove host networking here if you want the container to have its own IP address
docker build --network=host . -t $IMG_BUILD_TAG;
