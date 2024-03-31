# Phonepe-Pulse-Data-Visualization-and-Exploration

## Project Description
PhonePe Pulse Data Visualization and Exploration is a user-friendly tool developed using Streamlit and Plotly in Python. It aims to extract, transform, and visualize data from the PhonePe Pulse GitHub repository, providing valuable insights and information in an interactive and visually appealing dashboard.

## Technologies
- Python
- Pandas
- MySQL
- mysql-connector-python
- Streamlit
- Plotly

## Domain
Fintech

## Problem Statement
The PhonePe Pulse GitHub repository contains a large amount of data related to various metrics and statistics. The goal of this project is to extract, process, and visualize this data in a user-friendly manner. The solution should include steps to:
1. Extract data from the GitHub repository through scripting and clone it.
2. Transform the data into a suitable format, perform cleaning and pre-processing steps.
3. Insert the transformed data into a MySQL database for efficient storage and retrieval.
4. Create a live geo-visualization dashboard using Streamlit and Plotly to display the data interactively.
5. Fetch the data from the MySQL database to display in the dashboard.
6. Provide at least 10 different dropdown options for users to select different facts and figures to display on the dashboard.

## Approach
1. **Data Extraction**: Clone the GitHub repository using scripting to fetch the data and store it in a suitable format such as CSV or JSON.
2. **Data Transformation**: Use Python and Pandas to manipulate and pre-process the data, including cleaning, handling missing values, and transforming it into a suitable format.
3. **Database Insertion**: Utilize mysql-connector-python to connect to a MySQL database and insert the transformed data using SQL commands.
4. **Dashboard Creation**: Employ Streamlit and Plotly libraries to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions and Streamlit's user-friendly interface will be used for this purpose.
5. **Data Retrieval**: Connect to the MySQL database again using mysql-connector-python to fetch data into a Pandas dataframe for dynamic updating of the dashboard.
6. **Deployment**: Ensure the solution is secure, efficient, and user-friendly. Thoroughly test the solution and deploy the dashboard publicly, making it accessible to users.

## Results
The solution leverages the power of Python and its libraries to extract, transform, analyze, and visualize data from the PhonePe Pulse GitHub repository. The resulting dashboard provides valuable insights and information in a user-friendly manner, enhancing the understanding of the data.

## Usage
To use this tool, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Access the dashboard through the provided URL in the terminal.


