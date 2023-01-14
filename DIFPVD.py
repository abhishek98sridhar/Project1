import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

st.title('Diffusion Changes by Tool')

with st.sidebar:
        st.write("Select FVX Tool")

add_selectbox = st.sidebar.selectbox(
    
    'Select the Product',
    ('FVX23900',
 'FVX23901',
 'FVX23902',
 'FVX23903',
 'FVX23904',
 'FVX23905',
 'FVX23906',
 'FVX23907',
 'FVX23908',
 'FVX23909',
 'FVX23910',
 'FVX23911',
 'FVX23912',
 'FVX23913',
 'FVX23914',
 'FVX23915',
 'FVX23916',
 'FVX23917',
 'FVX23918')

)

dt=pd.read_csv("md1.csv")
dt['DATE-WAFER']=dt['DATE']+" "+dt['Wafer']

# Select Tool
mask=(dt['Tool']==add_selectbox)
fd=dt.loc[mask]
fd=fd.sort_values(by=['DATE'],ascending=False)

#YIELD TRENDS BY DATE SHORT LOT WAFER
fig = px.line(fd, x='DATE-WAFER', y='Value', color='Change',markers=True,width=800, height=400)
fig.update_layout(title=add_selectbox, title_x=1.0)
fig.update_xaxes(showticklabels=False) # Change Y axis with Bin Needed for Trend Chart by Bin

st.plotly_chart(fig)
