"""named spark data frames"""

from pandas import DataFrame as PandasDataFrame
from .utils import ValidateMixIn, ReprMixIn


class PandasNamedFrame(PandasDataFrame, ValidateMixIn, ReprMixIn):
    def __init__(self, pandas_df):
        super().__init__(pandas_df)
        self._validate()

    def __repr__(self):
        return self._repr_alt()
