"""named spark data frames"""

from pyspark.sql import SQLContext, SparkSession, DataFrame as SparkDataFrame
from pyspark.ml.common import _py2java
from .utils import ValidateMixIn


class SparkNamedFrame(SparkDataFrame, ValidateMixIn):
    def __init__(self, spark_df):
        spark_session = SparkSession.builder.getOrCreate()
        super().__init__(
            _py2java(spark_session.sparkContext, spark_df),
            SQLContext(spark_session.sparkContext, spark_session),
        )
        self._validate()

    def __repr__(self):
        message = "DataFrame with columns:\n"
        column_descriptions = [
            f"{column_name}: {column_type}"
            for column_name, column_type in self.__annotations__.items()
        ]
        message += "\n".join(column_descriptions)
        return message + "\n" + super().__repr__()
