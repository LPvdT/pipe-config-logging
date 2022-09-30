#!/usr/bin/env bash

# Build configuration
IMG_BUILD_TAG="pipe_config_logging:0.1";

# Construct and execute command
docker build . -t $IMG_BUILD_TAG;
