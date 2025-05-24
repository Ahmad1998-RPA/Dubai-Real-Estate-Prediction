import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("models/dubai_property.pkl")

# Streamlit UI
st.title("🏠 Rent Price Prediction App")

st.markdown("Fill in the details below to predict the rent.")

# Input fields
beds = st.number_input("Number of Beds", min_value=0, step=1) #1
baths = st.number_input("Number of Baths", min_value=0, step=1) #2
area = st.number_input("Area in Sqft", min_value=100) #3
type_ = st.selectbox("Property Type", ['Apartment', 'Penthouse', 'Villa', 'Townhouse', 'Villa Compound','Residential Building', 'Residential Floor', 'Hotel Apartment', 'Residential Plot']) #4
frequency = st.selectbox("Payment Frequency", ["Monthly", "Yearly"]) #6
city = st.selectbox("City", ['Abu Dhabi', 'Ajman', 'Al Ain', 'Dubai', 'Fujairah', 'Ras Al Khaimah', 'Sharjah', 'Umm Al Quwain']) #8
location = st.text_input("Location") #7
rent_category = st.selectbox("Rent Category", ['Medium', 'High', 'Low']) #5

# Predict button
if st.button("Predict Rent"):
    input_data = pd.DataFrame({
        "Beds": [beds],
        "Baths": [baths], 
        "Area_in_sqft": [area],
        "Type": [type_],
        "Frequency": [frequency],
        "City": [city],
        "Location": [location],
        'Rent_category': [rent_category]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Rent: AED {int(prediction):,}")
