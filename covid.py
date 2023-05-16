import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import covidSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.totalCasesByCountry(), con.connection)
con.CloseConnection()
dfCases = pd.DataFrame(query, columns=["country_code", "country_name", "amount_cases"])
figBarCases = px.bar(dfCases.head(20), x = "country_name", y = "amount_cases")


app.layout= html.Div(children = [
    html.H1(children = ' Covid 19 Dashboard'),
    html.H2(children = ' Covid 19 Dashboard'),
    dcc.Graph(
        id = 'barCasesByCountry',
        figure = figBarCases
        ),
    ])

if __name__ == '__main__':
    app.run_server(debug = True)
