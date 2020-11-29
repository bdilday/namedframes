"""named spark data frames"""

from pandas import DataFrame as PandasDataFrame
from .utils import ValidateMixIn


class PandasNamedFrame(PandasDataFrame, ValidateMixIn):
    def __init__(self, pandas_df):
        super().__init__(pandas_df)
        self._validate()
