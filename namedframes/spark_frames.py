"""named spark data frames"""

from pyspark.sql import SQLContext, SparkSession, DataFrame as SparkDataFrame
from pyspark.ml.common import _py2java
from .utils import ValidateMixIn, ReprMixIn


class SparkNamedFrame(SparkDataFrame, ValidateMixIn, ReprMixIn):
    def __init__(self, spark_df):
        spark_session = SparkSession.builder.getOrCreate()
        super().__init__(
            _py2java(spark_session.sparkContext, spark_df),
            SQLContext(spark_session.sparkContext, spark_session),
        )
        self._validate()

    def __repr__(self):
        return self._repr_alt()
