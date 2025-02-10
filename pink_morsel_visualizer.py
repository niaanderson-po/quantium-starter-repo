from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Soul Foods: Pink Morsel Visualizer'),
    dcc.Graph(id="graph"),
    dcc.RadioItems(
        id="radio",
        options=["north", "south", "east","west", "all"],
        value="all",
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("radio", "value"))
def update_line_chart(region):
    df = pd.read_csv('/Users/niaapple/Desktop/VSCode/quantium-starter-repo/formatted_data.csv') # replace with your own data source
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]
    fig = px.line(trimmed_data, 
        x="date", y="sales", color='region')
    return fig


if __name__ == '__main__':
    app.run(debug=True)