import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# ================================================
# Load trained model
# ================================================
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

# ================================================
# MAIN APP
# ================================================
def run_ml_app():

    st.title("Used Car Price Prediction App")
    st.markdown("This app will be used to predict the resale price of a used car.")

    # Informasi atribut
    with st.expander("Attribute Information"):
        st.markdown("""
        - **Make Year**: Tahun mobil dibuat  
        - **Mileage (km/l)**: Konsumsi bahan bakar  
        - **Engine Size (cc)**  
        - **Fuel Type**: Petrol, Diesel, Electric  
        - **Number of Owners**  
        - **Brand**  
        - **Transmission**  
        - **Color**  
        - **Service History**: None / Partial / Full  
        - **Accidents Reported**  
        - **Insurance Valid**: Yes / No  
        """)

    st.subheader("Input Car Specifications")

    # ========================
    # INPUT USER
    # ========================
    make_year = st.number_input("Make Year", min_value=1990, max_value=2023, value=2015)
    mileage = st.number_input("Mileage (km/l)", min_value=5.0, max_value=35.0, value=18.0, step=0.1)
    engine_size = st.number_input("Engine Size (cc)", min_value=600, max_value=6000, value=1500)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
    owners = st.number_input("Number of Previous Owners", min_value=1, max_value=5, value=1)
    brand = st.selectbox("Brand", ["Toyota", "Honda", "BMW", "Hyundai", "Tesla", "Ford", "Volkswagen"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    color = st.selectbox("Color", ["White", "Black", "Silver", "Blue", "Red", "Gray"])
    service = st.selectbox("Service History", ["None", "Partial", "Full"])
    accidents = st.number_input("Accidents Reported", min_value=0, max_value=5, value=0)
    insurance = st.selectbox("Insurance Valid", ["Yes", "No"])

    # Show selections
    with st.expander("Your Selected Specifications"):
        st.write({
            "make_year": make_year,
            "mileage": mileage,
            "engine_size": engine_size,
            "fuel_type": fuel_type,
            "owners": owners,
            "brand": brand,
            "transmission": transmission,
            "color": color,
            "service_history": service,
            "accidents": accidents,
            "insurance": insurance
        })

    # ========================
    # PREDIKSI
    # ========================
    st.subheader("Prediction Result")

    if st.button("Predict Price"):

        # Buat dataframe sesuai model
        input_data = pd.DataFrame([{
            "make_year": make_year,
            "mileage": mileage,
            "engine_size": engine_size,
            "fuel_type": fuel_type,
            "owners": owners,
            "brand": brand,
            "transmission": transmission,
            "color": color,
            "service_history": service,
            "accidents": accidents,
            "insurance": insurance
        }])

        # Load model
        model = load_model("model_grad.pkl")

        # Predict
        prediction = model.predict(input_data)[0]

        st.success(f"Estimated Car Price: **${prediction:,.2f}**")

# Run app
if __name__ == "__main__":
    run_ml_app()
