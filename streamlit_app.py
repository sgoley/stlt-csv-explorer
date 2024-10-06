import streamlit as st
import pandas as pd
import numpy as np


with st.container():
    st.title("CSV File Selector and Filter")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display basic information about the dataset
        st.write(f"Uploaded file: {uploaded_file.name}")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")


with st.sidebar:
    if uploaded_file is not None:
        filter_column_1 = st.selectbox(
            key="filter_c_1",
            label="Select the first column to filter by",
            options=df.columns.tolist(),
        )
        filter_value_1 = st.multiselect(
            key="filter_v_1",
            label="Select the value to filter by",
            options=np.unique(df[filter_column_1]),
            default=np.unique(df[filter_column_1])[0],
        )

        filter_column_2 = st.selectbox(
            key="filter_c_2",
            label="Select the second column to filter by",
            options=df.columns.tolist(),
        )
        filter_value_2 = st.multiselect(
            key="filter_v_2",
            label="Select the value to filter by",
            options=np.unique(df[filter_column_2]),
            default=np.unique(df[filter_column_2])[0],
        )


with st.container():
    if uploaded_file is not None:
        filtered_df = df
        if filter_value_1 != []:
            filtered_df = filtered_df[filtered_df[filter_column_1].isin(filter_value_1)]
        if filter_value_2 != []:
            filtered_df = filtered_df[filtered_df[filter_column_2].isin(filter_value_2)]

        st.write(filtered_df)


# debug the filter values
# with st.container():
#     filter_column_1
#     filter_value_1
#     filter_column_2
#     filter_value_2
