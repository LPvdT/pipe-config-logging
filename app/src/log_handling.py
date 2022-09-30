import pathlib
import logging

from logging import FileHandler, Formatter
from rich.logging import RichHandler
from rich.console import Console
from typing import Union


def setup_logging(log_file: Union[pathlib.Path, str], level: str) -> None:
    if isinstance(log_file, str):
        path = pathlib.Path(log_file)
    else:
        path = log_file

    if not isinstance(level, str) or level not in [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
    ]:
        raise ValueError(f"'{level}' is not a valid option.")

    # Create directory path to log file, if it doesn't exist
    if not path.exists():
        path.parent.mkdir(parents=True)

    # Handlers
    file_handler = FileHandler(filename=path, mode="a", encoding="utf-8")

    rich_handler = RichHandler(
        level=level,
        console=Console(tab_size=2),
        rich_tracebacks=True,
        markup=True,
        show_time=True,
    )

    # Formatters
    formatting = {
        "rich_text": "['[bold]{funcName}[/bold]']: [italic]{message}[/italic]",
        "file_text": "{asctime}\t[{levelname}]: ['{module}' >> '{funcName}']: {message}",
        "log_date": "%Y-%m-%d %H:%M:%S",
    }

    rich_handler.setFormatter(
        Formatter(
            fmt=formatting["rich_text"],
            datefmt=formatting["log_date"],
            style="{",
        )
    )

    file_handler.setFormatter(
        Formatter(
            fmt=formatting["file_text"],
            datefmt=formatting["log_date"],
            style="{",
        )
    )

    # Config
    logging.basicConfig(level=level, handlers=[file_handler, rich_handler])


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name=name)
