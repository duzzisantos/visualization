from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

csv = ["my.csv"]
df = pd.read_csv(csv)

app = Dash()

app.layout = [
    html.H1(children="Data Analytics Showcasing Country Information"),
    html.Hr(),
    dcc.RadioItems(
        options=[
            "pop",
            "lifExp",
            "gdpPerCap",
            "avgRetirementAge",
        ],
        value="lifExp",
        id="controls-and-radio-item",
    ),
    dash_table.DataTable(data=df.to_dict("records"), page_size=6),
    dcc.Graph(figure={}, id="controls-and-graph"),
]


# Add controls to build the interaction
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(selected_column):
    fig = px.histogram(df, x="continent", y=selected_column, histfunc="avg")
    return fig


# To start the application

if __name__ == "__main__":
    app.run(debug=True)
