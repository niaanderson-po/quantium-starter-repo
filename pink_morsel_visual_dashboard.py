from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

#data used for graph visual
df = pd.read_csv('/Users/niaapple/Desktop/VSCode/quantium-starter-repo/formatted_data.csv')

#initialize the app
app = Dash(__name__)

#app layout with html and css
app.layout = html.Div([

    #centered header
    html.Header(
        "Pink Morsel Sales Over Time",
        style={"font-size": "30px", "width": "400px", "textAlign": "center", "margin": "auto", "background":"#e5ecf6"}
    ),
    
    #center-left div
    html.Div([
        html.P("Select Region:", style={"font-size": "15px"}),
        dcc.RadioItems(
            id="radio",
            options=[ "all", "north", "south", "east", "west"],
            value="all",
            inline=True,
        )
    ], style={"display": "flex", "alignItems": "center", "width": "400px", "margin": "auto"}),

    #graph representation of df - dataframe
    dcc.Graph(figure={}, id="graph")

], style={"margin": 10, "maxWidth": 800})

#added controls/input-output for user interaction
@app.callback( 
    Output("graph", "figure"),
    Input("radio", "value")
    )

#callback function
def update_line_chart(region):
    #identitfy specific data related to region(s) selected
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]

    #build and return graph/figure based on requested data
    fig = px.line(trimmed_data, x="date", y="sales", color='region')
    return fig

#run the app
if __name__ == '__main__':
    app.run(debug=True)