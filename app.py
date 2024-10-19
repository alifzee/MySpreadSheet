import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Spreadsheet App 1.0", layout="wide")
st.title("📊 Spreadsheet App 1.0")

# Initialize the DataFrame
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame('', index=range(100), columns=[f'Column {i+1}' for i in range(100)])

# Function to resize columns
def resize_columns(widths):
    return f"<style>{''.join([f'th:nth-child({i+1}) {{ width: {width}px; }}' for i, width in enumerate(widths)])}</style>"

# Function to resize rows
def resize_rows(heights):
    return f"<style>{''.join([f'tr:nth-child({i+1}) {{ height: {height}px; }}' for i, height in enumerate(heights)])}</style>"

# Sidebar for menus
with st.sidebar:
    st.header("File Menu")
    file_option = st.selectbox("Choose an option", ["Save File", "Open New File", "Exit"])
    
    st.header("FUNC Menu")
    func_option = st.selectbox("Choose a function", ["Add Row", "Add Column", "Average Row", "Average Column"])
    
    if func_option == "Add Row":
        st.session_state.data.loc[len(st.session_state.data)] = [''] * 100
    elif func_option == "Add Column":
        st.session_state.data[f'Column {len(st.session_state.data.columns) + 1}'] = [''] * len(st.session_state.data)
    elif func_option == "Average Row":
        row_index = st.number_input("Select Row to Average (1-100)", 1, 100) - 1
        average_value = st.session_state.data.iloc[row_index].astype(float).mean()
        st.write(f"Average of Row {row_index + 1}: {average_value}")
    elif func_option == "Average Column":
        col_index = st.number_input("Select Column to Average (1-100)", 1, 100) - 1
        average_value = st.session_state.data.iloc[:, col_index].astype(float).mean()
        st.write(f"Average of Column {col_index + 1}: {average_value}")

# User can resize column widths and row heights
column_widths = []
for i in range(100):
    width = st.slider(f"Width for Column {i+1} (px)", 50, 300, 100, key=f'col_width_{i}')
    column_widths.append(width)

row_heights = []
for i in range(100):
    height = st.slider(f"Height for Row {i+1} (px)", 20, 100, 40, key=f'row_height_{i}')
    row_heights.append(height)

# Create a container to hold the input fields
cell_inputs = []

# Create a grid of text inputs for the spreadsheet
for i in range(100):
    row_inputs = []
    for j in range(100):
        value = st.text_input(f"Cell ({i+1},{j+1})", value=st.session_state.data.iloc[i, j], key=f"cell_{i}_{j}")
        row_inputs.append(value)
    cell_inputs.append(row_inputs)

# Update the DataFrame with the current values from the input fields
for i in range(100):
    for j in range(100):
        st.session_state.data.iloc[i, j] = cell_inputs[i][j]

# Apply custom CSS styles for resizing
st.markdown(resize_columns(column_widths), unsafe_allow_html=True)
st.markdown(resize_rows(row_heights), unsafe_allow_html=True)

# Display the DataFrame as a table
st.dataframe(st.session_state.data.style.set_table_attributes('style="width: 100%;"'))

# Placeholder for file operations
if file_option == "Save File":
    st.success("File saved successfully (placeholder).")
elif file_option == "Open New File":
    st.success("New file opened (placeholder).")
elif file_option == "Exit":
    st.stop()

# Footer
st.markdown("<footer style='text-align: center;'>یہ ایک سادہ اسپریڈشیٹ ایپ ہے۔</footer>", unsafe_allow_html=True)
