'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")
file = st.file_uploader("Upload a file: (excel, csv, or json only)", type = ["xlsx", "csv", "json"])
if file:
    filetype = pl.get_file_extension(file.name)
    df = pl.load_file(file, filetype)
    shown = df
    columns = pl.get_column_names(df)
    selected = st.multiselect("Select columns to display: ", columns, default = columns)
    if st.toggle("Filter Data"):
        cols = pl.get_columns_of_type(df, "object")
        filter_column = st.selectbox("Select column to filter: ", cols)
        if filter_column:
            values = pl.get_unique_values(df, filter_column)
            value = st.selectbox("Select value to filter on: ", values)
            shown = df[df[filter_column] == value][selected]
    else:
        shown = df[selected]
    st.dataframe(shown)
    st.dataframe(shown.describe())