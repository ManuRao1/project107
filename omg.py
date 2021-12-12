import plotly.express as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
# fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],  )
fig = ff.histogram(df, x="Mobile Brand", y="Avg Rating", marginal="rug")
fig.show()