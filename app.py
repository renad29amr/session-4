import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # Import Image from Pillow

st.set_page_config(page_title="Session 4", page_icon="ee.png")

# #loads the image file using Pillow so it can be displayed in the app.
img = Image.open("ee.png") 
st.image(img, width=150)
st.title("My Streamlit App")
st.write("Welcome to my dashboard!")
st.write("**Welcome to my first Streamlit application!**")
st.text("**Welcome to my first Streamlit application!**")

# # Slider
rows = st.slider("Select number of rows", 5, 100, 20)

# # Create random dataframe
df = pd.DataFrame(
    np.random.randn(rows, 3),
    columns=['Column A', 'Column B', 'Column C']
)

st.write("Here is a random dataframe:")
st.dataframe(df)

# # Dropdown for column
column_option = st.selectbox(
    "Choose a column to highlight",
    ['Column A', 'Column B', 'Column C']
)

# # Show selected column
st.write(f"You selected column: {column_option}")
st.write(df[column_option])

# # Dropdown for chart type
chart_type = st.selectbox(
    "Choose the type of chart",
    ["Line Chart", "Bar Chart", "Area Chart"]
)

st.write("Chart visualization:")

# Display chart based on user choice
if chart_type == "Line Chart":
    st.line_chart(df)
    st.write("jhfvbhjfvhfjhvf")

elif chart_type == "Bar Chart":
    st.bar_chart(df)

elif chart_type == "Area Chart":
    st.area_chart(df)

# # MULTISELECT for chart types
# chart_types = st.multiselect(
#     "Choose the type(s) of chart",
#     ["Line Chart", "Bar Chart", "Area Chart"]
# )

# # Display charts based on user choice
# for chart_type in chart_types:
#     st.write(f"### {chart_type}")
#     if chart_type == "Line Chart":
#         st.line_chart(df)
#         st.write("description of graph")
#     elif chart_type == "Bar Chart":
#         st.bar_chart(df)
#     elif chart_type == "Area Chart":
#         st.area_chart(df)

# st.title("Streamlit Markdown Demo")

st.write("""
# Heading Example

This is **bold text**

This is *italic text*

## List Example
- Item 1
- Item 2
- Item 3

## Link Example
Visit [Google](https://www.google.com)

## Code Example
Here is a simple code snippet: `print("Hello World")`
""")



# # Normal Markdown
# st.markdown("**Bold text with Markdown**")

# # HTML rendering
# st.write("<h1 style='color: red;'>This is a red header!</h1>",unsafe_allow_html=True)
# st.write("<p style='font-size:20px;'>This is a paragraph with larger text.</p>", unsafe_allow_html=True)
# st.markdown("<p style='font-size:20px;'>This is a paragraph with larger text.</p>",unsafe_allow_html=False)
























# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title("My First Streamlit App")

# st.write("Welcome to my first Streamlit application!")

# # Create a random dataframe
# df = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['Column A', 'Column B', 'Column C']
# )

# st.write("Here is a random dataframe:")
# st.dataframe(df)

# st.write("Line chart of the data:")
# st.line_chart(df)




# st.title("App Title")
# st.header("This is a header")
# st.subheader("This is a subheader")

# st.text("This is a simple text.")
# st.markdown("This is a text with **markdown** formatting.")

# st.dataframe(df)  # Displays an interactive table
# st.table(df)      # Displays a static table


# st.line_chart(df)
# st.bar_chart(df)
# st.area_chart(df)

# name = st.text_input("Enter your name:")
# st.write(f"Hello, {name}!")

# age = st.slider("Select your age:", 0, 100)
# st.write(f"You are {age} years old.")

# with st.sidebar:
#     st.write("This is the sidebar.")

# col1, col2 = st.columns(2)
# col1.write("Content in column 1")
# col2.write("Content in column 2")


# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title("My First Streamlit App")

# st.write("Welcome to my first Streamlit application!")

# # Slider
# rows = st.slider("Select number of rows", 5, 100, 20)

# # Dropdown (Selectbox)
# column_option = st.selectbox(
#     "Choose a column to highlight",
#     ['Column A', 'Column B', 'Column C']
# )

# # Create a random dataframe based on slider value
# df = pd.DataFrame(
#     np.random.randn(rows, 3),
#     columns=['Column A', 'Column B', 'Column C']
# )

# st.write("Here is a random dataframe:")
# st.dataframe(df)

# st.write("Line chart of the data:")
# st.line_chart(df)

# # Show selected column from dropdown
# st.write(f"You selected: {column_option}")
# st.write(df[column_option])


# title of project
# graph and its descripton
# recomendations
# logo 








# img = Image.open("ee.png") # Open the image file
# st.image(img, width=200) # Display the image with a specified width


# # Set page title and favicon
# st.set_page_config(
#     page_title="My Streamlit App",
#     page_icon="ee.png"  # Path to your image
# )

# Page config
# st.set_page_config(page_title="My App", page_icon="ee.png")

# Use columns to place logo on the left
# col1, col2 = st.columns([1, 10])

# size = st.slider("Logo size", 50, 200, 100)


# with col1:
#      st.markdown(
#     f"""
#     <img src="ee.png" 
#          style="width:{size}px; height:{size}px; border-radius:50%;">
#     """,
#     unsafe_allow_html=True
# )
# with col2:
#     st.title("My Streamlit App")
#     st.markdown("**Welcome to my dashboard!**")
