from src.config_handling import load_config
from src.pipeline_components import (
    load_data,
    one_hot,
    time_components,
    impute,
    return_and_serialize,
)

if __name__ == "__main__":

    # Load config
    config = load_config(file="./config/config.yaml")

    # Run pipeline
    data_transformed = (
        load_data(
            "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv"
        )
        .pipe(one_hot, "method", config["methods"])
        .pipe(time_components, "year", config["time-components"])
        .pipe(impute, "linear")
        .pipe(return_and_serialize, "./dump/transformed.json")
    )
