import streamlit as st
import pickle
import numpy as np


with open('gender_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Gender Classification App")


long_hair = st.selectbox("Does the person have long hair?", [1, 0])
forehead_width_cm = st.number_input("Forehead Width (cm)", min_value=10.0, max_value=20.0, step=0.1)
forehead_height_cm = st.number_input("Forehead Height (cm)", min_value=5.0, max_value=15.0, step=0.1)
nose_wide = st.selectbox("Is the nose wide?", [1, 0])
nose_long = st.selectbox("Is the nose long?", [1, 0])
lips_thin = st.selectbox("Are the lips thin?", [1, 0])
distance_nose_to_lip_long = st.selectbox("Is the distance from nose to lip long?", [1, 0])


if st.button("Predict Gender"):
    features = np.array([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])
    prediction = model.predict(features)
    gender = "Male" if prediction[0] == 1 else "Female"
    st.write(f"The predicted gender is: {gender}")
