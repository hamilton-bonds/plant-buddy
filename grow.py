import datetime as dt
import pandas as pd

FILEPATH = "plants2024.csv"

df = pd.read_csv(FILEPATH)
print(df)
