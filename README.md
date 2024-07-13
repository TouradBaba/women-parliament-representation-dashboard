# Population and GDP Data Visualization Dashboard

![Population and GDP Data Visualization Dashboard](Screenshots/Population1.png)

This repository contains a Dash web application built to visualize population and GDP data interactively. The app provides insights into demographic trends, economic indicators, and geographic distributions using interactive maps and various types of charts.

## Features

- **Interactive Dashboards**: Explore population and GDP trends by country and region interactively.
- **Geospatial Visualization**: Utilize interactive maps to visualize population density and GDP distribution.
- **Multi-page Application**: Navigate between different sections dedicated to population and GDP data.

## Deployment

The application is deployed on Heroku and accessible at [Population and GDP Data Visualization Dashboard](https://dash-app1-1d713809e6c0.herokuapp.com/).

## Data Sources

- Population Data: [UN Data - SYB66_1_202310_Population, Surface Area and Density](https://data.un.org/_Docs/SYB/CSV/SYB66_1_202310_Population,%20Surface%20Area%20and%20Density.csv)
- GDP Data: [UN Data - SYB66_230_202310_GDP and GDP Per Capita](http://data.un.org/_Docs/SYB/CSV/SYB66_230_202310_GDP%20and%20GDP%20Per%20Capita.csv)
- Land Area Data: [Our World in Data - Land Area](https://ourworldindata.org/grapher/land-area-km)

## Structure of the Repository

- `Jupyter_Notebooks/`: Contains Jupyter notebooks used for data exploration and analysis.
- `assets/`: Stores some screenshots and the Solar theme from [Bootswatch](https://bootswatch.com/).
- `data/`: Holds cleaned and processed datasets used by the application.
- `pages/`: Includes Python scripts defining different pages of the Dash app.
- `.gitattributes`: Git attributes configuration file.
- `.gitignore`: Git ignore configuration file.
- `Procfile`: Heroku configuration file specifying the application server.
- `app.py`: Main Python file defining the Dash application and its layout.
- `requirements.txt`: List of Python dependencies required to run the application.
- `runtime.txt`: Specifies the Python runtime version used by the application.

## Screenshots

### Population Page

*Population map when selecting a country*

![Population Page](Screenshots/Population2.png)


*Population heatmap and other figures*
![Population Page](Screenshots/Population3.png)


*Population heatmap and other figures when selecting a country
![Population Page](Screenshots/Population4.png)*


### GDP Page

*GIF that show countries GDP variation over time*
![GDP Page](Screenshots/GDP_GIF.gif)

*GDP map*

![GDP Page](Screenshots/GDP1.png)

*GDP map when selecting a country*

![GDP Page](Screenshots/GDP2.png)

*Other figures for GDP*
![GDP Page](Screenshots/GDP2.png)


## Installation and Setup

To run this application locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/TouradBaba/exploratory_data_analysis_and_visualization.git
   cd your-repository
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```
   Open http://127.0.0.1:8050/ in your web browser to view the app.
