#!/usr/bin/env bash

# Container runtime configuration
CNT_NAME="pipe_config_logging";
IMG_TAG="pipe_config_logging:0.1";

# Volume mapping
HOST_VOLUME_LOGS="$PWD/app/archive";
CNT_VOLUME_LOGS="/app/logs";

HOST_VOLUME_CONFIG="$PWD/app/config";
CNT_VOLUME_CONFIG="/app/config";

HOST_VOLUME_DUMP="$PWD/app/feeds";
CNT_VOLUME_DUMP="/app/dump";

# Construct and execute command
# Note: Remove host networking here if you want the container to have its own IP address
# Note: Add -it flags when scheduling this script using e.g. Cron
docker run --rm \
    -v $HOST_VOLUME_LOGS:$CNT_VOLUME_LOGS \
    -v $HOST_VOLUME_CONFIG:$CNT_VOLUME_CONFIG \
    -v $HOST_VOLUME_DUMP:$CNT_VOLUME_DUMP \
    --name $CNT_NAME \
    --network=host \
    $IMG_TAG;
