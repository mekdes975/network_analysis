import streamlit as st
import pandas as pd
import sys, os

current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_script_directory, os.pardir))

sys.path.append(parent_directory)

from src.postgres_functions import connect_to_postgres
from src.plot import *

# Database connection details (replace with your actual details)
dbname = "slack_feature"
user = "postgres"
password = "postgres1234"
host = "localhost"
port = "5432"

# Connect to PostgreSQL
connection, cursor = connect_to_postgres(dbname, user, password, host, port)

# Read data from the database (replace 'your_query' with your actual SQL query)
your_query = "SELECT * FROM messages"
data = pd.read_sql_query(your_query, connection)

# Close the database connection
connection.close()

# Streamlit app
def main():
    st.title('Message Analysis Dashboard')

    # Display the raw data
    st.subheader('Raw Data')
    st.write(data)

    # Visualization functions
    get_top_20_user(data, channel='all-technical-support')
    draw_avg_reply_count(data, channel='all-technical-support')
    draw_avg_reply_users_count(data, channel='all-technical-support')
    top_10_senders_eda(data)
    plot_time_differences(data)

if __name__ == '__main__':
    main()
