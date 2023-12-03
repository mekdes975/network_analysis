import streamlit as st
import pandas as pd
import sys, os

current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_script_directory, os.pardir))

sys.path.append(parent_directory)

def app():
    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of all-techincal-support channel messages")
    # st.text_input("Enter the number of rows", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    df = pd.read_csv('../data/messages.csv', nrows=number)


    st.write(df)