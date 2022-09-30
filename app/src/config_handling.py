import pathlib

from collections import OrderedDict
from ruamel_yaml import YAML
from typing import Union

from .log_handling import get_logger


def load_config(file: Union[pathlib.Path, str]) -> OrderedDict:
    log_host = get_logger(load_config.__name__)

    try:
        path = pathlib.Path(file) if isinstance(file, str) else file

        yaml = YAML()
        config = yaml.load(open(path))

        log_host.info("Config file loaded.")

        return config

    except Exception as e:
        log_host.error(str(e))
        raise
