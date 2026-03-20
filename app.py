import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 👇 IKADA PASTE CHEYYALI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f7ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💧 AI-Based Personalized Water Intake Predictor")
st.subheader("Enter your details below 👇")

weight = st.number_input("⚖️ Enter weight (kg)", min_value=30, max_value=150, value=60)
height = st.number_input("📏 Enter height (cm)", min_value=100, max_value=220, value=170)
age = st.number_input("🎂 Enter age", min_value=10, max_value=80, value=25)
activity = st.selectbox("🏃 Activity Level", ["Low", "Medium", "High"])
temp = st.number_input("🌡️ Temperature (°C)", min_value=0, max_value=50, value=30)

if activity == "Low":
    activity = 1
elif activity == "Medium":
    activity = 2
else:
    activity = 3

if st.button("💧 Predict Water Intake"):
    if height > 0:
        bmi = weight / ((height/100)**2)

        new_data = pd.DataFrame([[weight, age, activity, temp, bmi]],
                                columns=["weight","age","activity_level","temperature","BMI"])

        pred = model.predict(new_data)
        water = round(pred[0],2)

        st.success(f"Recommended Water Intake: {water} liters 💧")
        st.write("💡 Tip: Drink water throughout the day, not all at once!")
    else:
        st.error("Height cannot be zero")
