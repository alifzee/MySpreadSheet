import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Spreadsheet App 4.0", layout="wide")
st.title("📊 Spreadsheet App 4.0")

# Initialize the DataFrame for a 5x5 grid
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame('', index=range(5), columns=[f'Column {i+1}' for i in range(5)])

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
        if len(st.session_state.data) < 100:  # Limit to max 100 rows
            st.session_state.data.loc[len(st.session_state.data)] = [''] * 5
    elif func_option == "Add Column":
        if len(st.session_state.data.columns) < 100:  # Limit to max 100 columns
            st.session_state.data[f'Column {len(st.session_state.data.columns) + 1}'] = [''] * len(st.session_state.data)
    elif func_option == "Average Row":
        row_index = st.number_input("Select Row to Average (1-5)", 1, 5) - 1
        average_value = st.session_state.data.iloc[row_index].astype(float).mean()
        st.write(f"Average of Row {ro
