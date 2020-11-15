import pytest
import pandas as pd
from namedframes import NamedPandasDataFrame


class ExampleDF(NamedPandasDataFrame):
    x: int
    y: float


class ExampleBogusDF(NamedPandasDataFrame):
    x: int
    y: float
    extra: str


@pytest.fixture
def pandas_df():
    return pd.DataFrame({"x": [1, 2], "y": [1.1, 2.2]})


def test_pandas_dataframe(pandas_df):
    example_df = ExampleDF(pandas_df)
    assert isinstance(example_df, ExampleDF)


def test_pandas_dataframe_bad_schema(pandas_df):
    with pytest.raises(ValueError):
        _ = ExampleBogusDF(pandas_df)
