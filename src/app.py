import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Load countries data
csv_path = Path(__file__).parent.parent / 'data' / 'cleaned_df.csv'
df = pd.read_csv(csv_path, encoding='latin1')

# Find the latest year for each country
latest_years = df.groupby('Region/Country/Area')['Year'].max().reset_index()

# Merge to get the latest data for each country
latest_data = pd.merge(df, latest_years, on=['Region/Country/Area', 'Year'], how='inner')

# Get unique countries for dropdown options
regions = latest_data['Region/Country/Area'].unique()

# Load regions data specifically for regions (Region, Year, Value)
csv_path2 = Path(__file__).parent.parent / 'data' / 'regions_data.csv'
df2 = pd.read_csv(csv_path2, encoding='latin1')
# Find the latest year for each region
latest_years_regions = df2.groupby('Region')['Year'].max().reset_index()
# Merge to get the latest data for each region
latest_data_regions = pd.merge(df2, latest_years_regions, on=['Region', 'Year'], how='inner')

# Sort the data by 'Value' in descending order
latest_data_regions_sorted = latest_data_regions.sort_values(by='Value', ascending=False)

# Initialize Dash app
app = dash.Dash(__name__)

# Custom CSS stylesheet for styling with Bootstrap and Font Awesome
external_stylesheets = [
    'https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/flatly/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/css/fontawesome.min.css'
]

# Set external stylesheets in Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define app layout with custom styling
app.layout = html.Div(
    className='container-fluid',
    children=[
        html.Div(
            className='jumbotron bg-dark text-white',
            children=[
                html.H1("Women Representation in Parliaments Dashboard", className='display-4'),
                html.P(
                    "Click on a country on the map or select it "
                    "to see details and its representation in parliaments over time.",
                    className='lead'
                )
            ]
        ),
        html.Hr(className='my-4'),

        html.Div(
            className='row',
            children=[
                html.Div(
                    className='col-md-6 map-container',
                    children=[
                        dcc.Graph(id='map', config={'scrollZoom': True})
                    ]
                ),
                html.Div(
                    className='col-md-6 details-container bg-light p-3',
                    children=[
                        html.Div(id='country-details', className='details'),
                        dcc.Dropdown(
                            id='country-dropdown',
                            options=[{'label': country, 'value': country} for country in regions],
                            placeholder="Select a country",
                            className='mb-3'
                        ),
                        dcc.Graph(id='line-chart', className='line-chart')
                    ]
                )
            ]
        ),

        html.Hr(className='my-4'),

        html.Div(
            className='row',
            children=[
                html.Div(
                    className='col-md-12 regions-bar-chart-container',
                    children=[
                        dcc.Graph(
                            id='regions-bar-chart',
                            figure=px.bar(
                                latest_data_regions_sorted,
                                x='Region',
                                y='Value',
                                labels={'Value': 'Percentage (%)'},
                                title='Women Representation in Parliaments by Region 2023',
                                color_discrete_sequence=['steelblue']
                            )
                        )
                    ]
                )
            ]
        ),
        html.Div(id='output', style={'margin-top': '20px', 'font-size': '20px'})
    ]
)


# Callback to update the line chart and country details based on dropdown or map selection
@app.callback(
    [Output('line-chart', 'figure'),
     Output('country-details', 'children'),
     Output('country-dropdown', 'value')],
    [Input('country-dropdown', 'value'),
     Input('map', 'clickData')],
    [State('country-dropdown', 'value')]
)
def update_line_chart_and_details(country, clickData, current_dropdown_value):
    triggered_by = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    if triggered_by == 'map' and clickData is not None:
        country = clickData['points'][0]['location']

    line_chart_figure = {}
    country_details = html.P("Click on a country to see details.", className='placeholder-text')

    if country:
        selected_data_chart = df[df['Region/Country/Area'] == country]

        if not selected_data_chart.empty:
            line_chart_figure = px.line(
                selected_data_chart,
                x='Year',
                y='Value',
                title=f'Women Representation in Parliaments over Time - {country}',
                labels={'Year': 'Year', 'Value': 'Percentage (%)'}
            )

            latest_data_country = latest_data[latest_data['Region/Country/Area'] == country]
            if not latest_data_country.empty:
                percentage = latest_data_country['Value'].values[0]
                latest_year_country = latest_data_country['Year'].values[0]

                country_details = html.Div([
                    html.H3(f"{country}", className='country-name'),
                    html.P(f"Percentage: {percentage}%", className='country-percentage'),
                    html.P(f"Year: {latest_year_country}", className='country-year')
                ], className='country-details')

    return line_chart_figure, country_details, country

# Callback to update the map and rotate it
@app.callback(
    Output('map', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_map(selected_country):
    # Filter data to show only the selected country
    if selected_country:
        selected_data_map = latest_data[latest_data['Region/Country/Area'] == selected_country]
    else:
        selected_data_map = latest_data

    # Create the map figure
    map_figure = px.choropleth(
        selected_data_map,
        locations='Region/Country/Area',
        locationmode='country names',
        color='Value',
        hover_name='Region/Country/Area',
        color_continuous_scale='Viridis',
        projection='orthographic',
        title='Women Representation in Parliaments'
    )

    map_figure.update_geos(
        showcoastlines=True,
        coastlinecolor="Gray",
        showland=True,
        landcolor="LightGray",
        showocean=True,
        oceancolor="LightBlue"
    )

    if selected_country:
        center_lat = selected_data_map['Latitude'].mean()
        center_lon = selected_data_map['Longitude'].mean()
        map_figure.update_geos(
            projection_rotation_lon=center_lon,
            projection_rotation_lat=center_lat
        )

    map_figure.update_layout(
        margin={"r": 0, "t": 60, "l": 0, "b": 0},
        dragmode='pan',
        height=800
    )

    return map_figure


if __name__ == '__main__':
    app.run_server()