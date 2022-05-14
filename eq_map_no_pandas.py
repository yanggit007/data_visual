import plotly.express as px
import test

fig = px.scatter(
    x=test.lons,
    y=test.lats,
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1600,
    height=800,
    title='全球地震散点图',
)

fig.show()
