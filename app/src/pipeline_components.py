import pathlib
import json
import pandas as pd

from typing import Optional

from .log_handling import get_logger


def load_data(path: str) -> pd.DataFrame:
    log_host = get_logger(load_data.__name__)

    try:
        data = pd.read_csv(path)

        log_host.info("Data loaded.")

        return data
    except Exception as e:
        log_host.error(str(e))
        raise


def one_hot(
    data: pd.DataFrame, column: str, column_subset: list
) -> pd.DataFrame:
    log_host = get_logger(one_hot.__name__)

    try:
        d = data.loc[~data[column].isin(column_subset), :]
        d = pd.concat([pd.get_dummies(data=d[column]), d], axis=1)
        d.columns = [c.lower().replace(" ", "_") for c in d.columns]

        log_host.info("Data onehotting completed.")

        return d.drop(column, axis=1)

    except Exception as e:
        log_host.error(str(e))
        raise


def time_components(
    data: pd.DataFrame, year_column: str, retain_components: list
) -> pd.DataFrame:
    log_host = get_logger(time_components.__name__)

    try:
        d = pd.to_datetime(data[year_column], format="%Y")
        d = pd.Timestamp.now() - d

        retain = list(map(str.lower, retain_components))

        log_host.debug(f"Cached components to retain: {retain}")

        components = d.dt.components
        components = components.get(
            [c for c in components.columns if c.lower() in retain]
        )
        components.columns = [
            f"discovered_{c}_ago" for c in components.columns
        ]

        d = pd.concat([data, components], axis=1)

        log_host.info("Time component decomposition completed.")

        return d.drop(year_column, axis=1)

    except Exception as e:
        log_host.error(str(e))
        raise


def impute(
    data: pd.DataFrame,
    method: Optional[str] = None,
    subset: Optional[list] = None,
) -> pd.DataFrame:
    log_host = get_logger(impute.__name__)

    try:
        if subset:
            targets = subset
            log_host.debug(f"Using column subset: {targets}")
        else:
            targets = data.columns[data.isnull().any()].to_list()

        data[targets] = data.get(targets).interpolate(
            method=method if method else "akima", downcast="infer"
        )

        log_host.info(
            f"NA imputation using '{method if method else 'akima'}' interpolation completed."
        )

        return data

    except Exception as e:
        log_host.error(str(e))
        raise


def return_and_serialize(data: pd.DataFrame, output_path: str) -> pd.DataFrame:
    log_host = get_logger(return_and_serialize.__name__)

    try:
        if isinstance(output_path, str):
            path = pathlib.Path(output_path)
        else:
            path = output_path

        if not path.exists():
            log_host.debug(f"Creating directory tree to '{path.as_posix()}'")

            path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as f_out:
            log_host.warning(
                "Data dump will overwrite existing file with the same name."
            )

            json.dump(
                json.loads(data.to_json(index=False, orient="table")),
                f_out,
                indent=4,
            )

        log_host.info("Data serialization (JSON) completed.")

        return data

    except Exception as e:
        log_host.error(str(e))
        raise
