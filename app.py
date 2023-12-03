import streamlit as st
from multiapp import MultiApp
from views import home, data, visualization

st.set_page_config(page_title="Slack message data analysis")

app = MultiApp()


st.title("Slack message data analysis")

st.markdown("""
            # technical support Data Analysis
            Slack message data analysis
            """)

app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Visualization", visualization.app)

#  main app
app.run()