import io
import pandas as pd
import pyarrow as pa
from pyarrow import hdfs
from pyarrow import parquet as pq

infile = '/user/jcrist/test.csv'
outfile = '/user/jcrist/out.parquet'

print("Connecting to HDFS")
fs = hdfs.connect()

print("Reading %r from hdfs" % infile)
with fs.open(infile) as f:
    df = pd.read_csv(io.BytesIO(f.read()))

print("Read %d rows" % len(df))

print("Writing to %r on hdfs" % outfile)
with fs.open(outfile, 'wb') as f:
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f)
print("Done!")
