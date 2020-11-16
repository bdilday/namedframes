import pytest
from namedframes import _has_pyspark

if _has_pyspark:
    from pyspark.sql import SparkSession
    from namedframes import SparkNamedFrame

    class ExampleDF(SparkNamedFrame):
        x: float

    class ExampleBogusDF(SparkNamedFrame):
        x: float
        extra: str

    @pytest.fixture
    def spark():
        session = SparkSession.builder.getOrCreate()
        session.sparkContext.setLogLevel("WARN")
        yield session
        session.stop()

    def test_spark_named_frame(spark, pandas_df):
        spark_df = spark.createDataFrame(pandas_df)
        example_df = ExampleDF(spark_df)
        assert isinstance(example_df, ExampleDF)

        with pytest.raises(ValueError):
            _ = ExampleBogusDF(spark_df)
