import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Student Marks vs Days Present.csv")

fig = ff.create_distplot([df["Marks In Percentage"].tolist()], ["Marks"], show_hist=True)
fig.show()
