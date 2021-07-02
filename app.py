import streamlit as st

import matplotlib.pyplot as plt 
import pandas as pd

import logging

import numpy as np
import geopandas as gpd 
import seaborn as sns

# Getting the code
import src.gpdSport as gpdSport

@st.cache(hash_funcs={pd.core.frame.DataFrame: id},allow_output_mutation=True)#allow_output_mutation=True)
def loadFile():
    data = gpdSport.dataSets()
    DATA = data.CreateDF("./data/")
    return DATA, data

DATA, data = loadFile()

ZOOM_LEVEL = int(st.sidebar.slider('Niveau de zzoom?', min_value=8, max_value=15, value=12, step = 1) )
VILLE = st.sidebar.number_input('Code INSEE de la ville (ex 94043)', min_value=0,max_value=100000,value=8409)

if VILLE == 8409:
    st.write("Merci d'entrer un code INSEE valide")
else:
    VILLE = int(VILLE)
    data.CreateVille(VILLE); #
    fig = data.CreateMap(ZOOM=ZOOM_LEVEL,streamlit=True)

    Part1, Part2 = data.createStreamLitOutput()

    st.write(Part1)


    st.write(fig)

    st.write(Part2)
