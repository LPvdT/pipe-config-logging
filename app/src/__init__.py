import pathlib
from .log_handling import setup_logging

# Configure logging
setup_logging(
    pathlib.Path(__file__).parent.parent.joinpath("logs", "log.log"),
    level="DEBUG",
)
