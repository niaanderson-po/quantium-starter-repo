from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Soul Foods: Pink Morsel Visualizer'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["north", "south", "east","west"],
        value=["north", "south", "east","west"],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(region):
    df = pd.read_csv('/Users/niaapple/Desktop/VSCode/quantium-starter-repo/formatted_data.csv') # replace with your own data source
    mask = df.region.isin(region)
    fig = px.line(df[mask], 
        x="date", y="sales", color='region')
    return fig


if __name__ == '__main__':
    app.run(debug=True)