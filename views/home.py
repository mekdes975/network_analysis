from PIL import Image
import streamlit as st
import sys, os

current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_script_directory, os.pardir))

sys.path.append(parent_directory)
print(parent_directory)
def app():
    st.title('Home')

    st.write("Trending topics in all-technical-support channel")

    st.write(
        'Go to the data navigation to learn more about the data and the visualization page to get insight of the Data.')
    
    image_path = 'Images/wordCloud.png'
    image = Image.open(image_path)

    st.image(image, caption="Word cloud analysis", use_column_width=True)

# Run the Streamlit app
if __name__ == '__main__':
    app()