import os
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Python\\Python3x\\python.exe"
import os
os.environ["PYSPARK_PYTHON"] = "python"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("demo").getOrCreate()
df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13),
    ],
    ["first_name", "age"],
)
df.show()