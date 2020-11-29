"""named spark data frames"""

from pandas import DataFrame as PandasDataFrame
from .utils import ValidateMixIn


class PandasNamedFrame(PandasDataFrame, ValidateMixIn):
    def __init__(self, pandas_df):
        super().__init__(pandas_df)
        self._validate()

    def __repr__(self):
        message = "DataFrame with columns:\n"
        column_descriptions = [
            f"{column_name}: {column_type}"
            for column_name, column_type in self.__annotations__.items()
        ]
        message += "\n".join(column_descriptions)
        return message + "\n" + super().__repr__()
