# Women in Parliament Dashboard

![Dashboard Preview](images/dashboard_preview.png)

This repository hosts a dashboard built with Dash and Plotly, designed to visualize global women's representation in parliaments.

You can access the live dashboard hosted on:
- [Heroku](https://dash-app2-a77ab9dd53b7.herokuapp.com/)
- [PythonAnywhere](https://touradb.pythonanywhere.com/)

## Features

- Interactive map displaying women's representation data by country.
- Time series chart showing trends in women's representation over years for selected countries.
- Bar chart illustrating women's representation by region.
- Dropdown menu for detailed country-level data on women's representation.
- Built-in filtering and selection based on user interaction with the map.
- Deployed on Heroku and PythonAnywhere for easy accessibility.

## Data Sources

Data sourced from the United Nations Statistics Division (UNSD):
- [Seats held by women in Parliament](https://data.un.org/_Docs/SYB/CSV/SYB66_317_202310_Seats%20held%20by%20women%20in%20Parliament.csv)

## Repository Structure

```
women-parliament-representation-dashboard/
├── app.py
├── requirements.txt
├── data/
│   ├── cleaned_df.csv
│   └── regions_data.csv
├── images/
│   ├── dashboard_preview.png
│   ├── dashboard_preview2.png
│   └── percentage_over_years.gif
├── data_preparation.ipynb
├── Procfile
├── .gitignore
└── .gitattributes
```

## Visual Preview

### Percentage Over Years
![Dashboard Preview](images/percentage_over_years.gif)

### Dashboard Preview with Country Selection
![Dashboard Preview](images/dashboard_preview2.png)

## Installation and Setup

To run the dashboard locally:

1. Clone this repository:
   ```
   git clone https://github.com/TouradBaba/women-parliament-representation-dashboard.git
   ```

2. Navigate to the project directory:
   ```
   cd women-parliament-representation-dashboard
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and go to `http://127.0.0.1:8050/` to view the dashboard.
