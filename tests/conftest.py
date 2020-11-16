import pytest
import pandas as pd


@pytest.fixture
def pandas_df():
    return pd.DataFrame({"x": [1, 2], "y": [1.1, 2.2]})
