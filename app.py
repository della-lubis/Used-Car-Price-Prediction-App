import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app

# ==============================
# HEADER / TITLE
# ==============================
html_temp = """
    <div style="background-color:#3872fb;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Used Car Price Prediction App</h1>
        <h4 style="color:white;text-align:center;">Car Valuation System</h4>
    </div>
"""

# ==============================
# DESCRIPTION
# ==============================
desc_temp = """
### Used Car Price Prediction App

This app is designed to predict the **resale price of a used car** based on its specifications such as mileage, engine size, fuel type, brand, transmission, and more.

#### Dataset Description
This dataset contains 10,000 realistic entries of used cars with features such as:
- Mileage  
- Engine size  
- Make year  
- Previous owners  
- Fuel type  
- Transmission  
- Brand  
- Color  
- Service history  
- Accidents reported  
- Insurance status  

#### App Content
- Input Form for Car Specifications  
- Machine Learning Model Prediction  
"""

# ==============================
# MAIN APP
# ==============================
def main():

    stc.html(html_temp)
    
    menu = ['Home', 'Machine Learning']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Welcome to the Homepage")
        st.markdown(desc_temp)

    elif choice == "Machine Learning":
        run_ml_app()


if __name__ == '__main__':
    main()
