from dash import Dash, dcc, html, Input, Output
from plotly.express import line
import pandas as pd

#path to the formatted data file 
DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary":"black",
    "secondary": "#e5ecf6",
}

#load in data
df = pd.read_csv(DATA_PATH)

#initialize the app
app = Dash(__name__)

# create the #graph representation of df - dataframe
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales")
    return line_chart

visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(df)
)

#centered header
header = html.H1(
    "Pink Morsel Sales Over Time",
    id="header",
    style={
        "font-size": "30px", 
        "width": "400px", 
        "textAlign": "center", 
        "margin": "auto", 
        "background-color": COLORS["secondary"],
    }
)

#centered left region filter
region_picker = dcc.RadioItems(
    options = ["all", "north", "south", "east", "west"],
    value = "all",
    id="radio",
    inline=True,
)

region_picker_wrapper = html.Div(
    [
        html.P("Select Region:", style={"font-size": "15px"}),
        region_picker
    ],
    style={
        "display": "flex", 
        "alignItems": "center", 
        "width": "400px", 
        "margin": "auto"
    }
)

#define input-output for user interaction
@app.callback( 
    Output(visualization, "figure"),
    Input(region_picker, "value")
    )

#callback function
def update_grapgh(region):
    #identitfy specific data related to region(s) selected
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]

    # generate a new line chart with the filtered data
    fig = generate_figure(trimmed_data)
    return fig

#app layout with html and css
app.layout = html.Div([
    header,
    region_picker_wrapper,
    visualization
], style={"margin": 10, "maxWidth": 800})

#run the app
if __name__ == '__main__':
    app.run(debug=True)