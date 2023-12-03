import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Function to get the top 20 users
def get_top_20_user(data, channel='Random'):
    st.subheader(f'Top 20 Message Senders in #{channel} channels')
    top_senders = data['sender_name'].value_counts()[:20]
    st.bar_chart(top_senders)

    st.subheader(f'Bottom 10 Message Senders in #{channel} channels')
    bottom_senders = data['sender_name'].value_counts()[-10:]
    st.bar_chart(bottom_senders)

# Function to draw average reply count
def draw_avg_reply_count(data, channel='Random'):
    st.subheader(f'Average Number of reply count per Sender in #{channel}')
    avg_reply_count = data.groupby('sender_name')['reply_count'].mean().sort_values(ascending=False)[:20]
    st.bar_chart(avg_reply_count)

# Function to draw average reply users count
def draw_avg_reply_users_count(data, channel='Random'):
    st.subheader(f'Average Number of reply user count per Sender in #{channel}')
    avg_reply_users_count = data.groupby('sender_name')['reply_users_count'].mean().sort_values(ascending=False)[:20]
    st.bar_chart(avg_reply_users_count)
    
# Function for top 10 senders EDA
def top_10_senders_eda(df):
    st.subheader('Top 10 Senders by Maximum Reply Count')
    
    # Find the top 10 senders by maximum reply_count
    top_10_senders = df.groupby('sender_name')['reply_count'].max().nlargest(10).reset_index()

    # Plot a bar chart for the top 10 senders by maximum reply_count
    st.bar_chart(top_10_senders.set_index('sender_name'))
    
    
def plot_time_differences(df):
    df['msg_sent_time'] = pd.to_datetime(df['msg_sent_time'], unit='s')
    df = df.sort_values(by='msg_sent_time')
    df['time_difference'] = df['msg_sent_time'].diff()
    
    # Plot a histogram using Matplotlib
    plt.hist(df['time_difference'].dt.total_seconds(), bins=50, edgecolor='black')
    plt.xlabel('Time Differences (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Time Differences Between Messages')
    
    # Display the plot in Streamlit using st.pyplot()
    st.pyplot()
