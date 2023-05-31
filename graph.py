import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Read file
dataOptimization = pd.read_csv("./results_avoa_iteration.csv", sep=",", header=None)
dataTop = pd.read_csv("./results_avoa_top_design.csv", sep=",", header=None)

# # Optimization Graph
# dfOptim = dataOptimization[1]
# figLine = px.line(dfOptim, title="Line Chart")
# figLine.update_layout(
#     xaxis_title="Iteration",
#     yaxis_title="Objective Value",
#     font=dict(
#         family="Railway",
#         size=15,
#         color="RebeccaPurple"
#     )
# )
# figLine.show()

# Parallel Coordinate Graph
dfTopDesigns = dataTop[0]
designs = []
for i in range(len(dfTopDesigns)):
    designs.append(dfTopDesigns.iloc[i].split(";"))

# make column names
columns = []

for i in range(30):
    name = f"x{i+1}"
    columns.append(name)

dfSplitDesigns = pd.DataFrame(designs, columns=columns)

dimensions = []
for i in range(30):
    name = f"x{i+1}"
    # create dimension
    dimensions.append(dict(
        range=[-100, 100],
        label=name,
        values=dfSplitDesigns[name],
        tickvals=[-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100] # this is only show column ticks
    ))


figParallelCoordinate = go.Figure(
    data=go.Parcoords(
        line=dict(colorscale='Electric',
                  showscale=True,
                  cmin=-100,
                  cmax=100),
        dimensions=dimensions
    )
)

figParallelCoordinate.show()
