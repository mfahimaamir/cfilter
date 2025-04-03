import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode

data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing'],
    'iTEM': ['TV', 'CAL', 'BUS', 'TRAIN', 'TANK', 'TABLE', 'DESK'],
    'Sale': [765, 455, 756, 567, 678, 456, 756]
    
    }

df = pd.DataFrame(data)

    # Create GridOptionsBuilder to customize grid options
gob = GridOptionsBuilder.from_dataframe(df)
# Configure column filters for all columns
for column in df.columns:
    gob.configure_column(column, filter=True)
gridOptions = gob.build()
# Display the table using streamlit-aggrid
AgGrid(df, gridOptions=gridOptions, update_mode=GridUpdateMode.MODEL_CHANGED)
#AgGrid(df)
#AgGrid(df, gridOptions=gridOptions)

