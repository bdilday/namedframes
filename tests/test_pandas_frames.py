import pytest
from namedframes import PandasNamedFrame


class ExampleDF(PandasNamedFrame):
    x: int
    y: float


class ExampleBogusDF(PandasNamedFrame):
    x: int
    y: float
    extra: str


def test_pandas_dataframe(pandas_df):
    example_df = ExampleDF(pandas_df)
    assert isinstance(example_df, ExampleDF)


def test_pandas_dataframe_bad_schema(pandas_df):
    with pytest.raises(ValueError):
        _ = ExampleBogusDF(pandas_df)


def test_repr_alt(pandas_df):
    example_df = ExampleDF(pandas_df)
    assert "DataFrame with columns" in example_df.__repr__()
