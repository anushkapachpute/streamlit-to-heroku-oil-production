import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import  Image
pickle_in=open("model.pkl","rb")
classifier=pickle.load(pickle_in)
def Oil_production_rate(Viscocity,Permeability,Anisotropy,oil_Saturation,Porosity,injection_rate):
    prediction=classifier.predict([[Viscocity,Permeability,Anisotropy,oil_Saturation,Porosity,injection_rate]])
    print(prediction)
    return prediction

def main():
    st.title("Oil Production")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">predict Oil Production rate</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Viscocity=float(st.number_input("Viscocity"))
    Permeability=float(st.number_input("Permeability"))
    Anisotropy=float(st.number_input("Anisotropy"))
    oil_Saturation=float(st.number_input("oil Saturation"))
    Porosity=float(st.number_input("Porosity"))
    injection_rate=float(st.number_input("injection rate"))
    result=""
    if st.button('Predict'):
        result=Oil_production_rate(Viscocity,Permeability,Anisotropy,oil_Saturation,Porosity,injection_rate)
        st.success('Oil production rate is{}'.format(result))
if __name__=='__main__':
    main()


