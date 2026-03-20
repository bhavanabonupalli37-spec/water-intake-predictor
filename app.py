import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "weight": [50,60,70,80,90,55,65,75,85,95],
    "height": [150,160,170,175,180,155,165,172,178,182],
    "age": [20,25,30,35,40,22,28,32,38,45],
    "activity_level": [1,2,2,3,3,1,2,3,2,3],
    "temperature": [20,25,30,35,40,22,28,33,36,38],
    "water_intake": [2.0,2.5,3.0,3.5,4.0,2.2,2.7,3.3,3.6,4.2]
}

df = pd.DataFrame(data)

# BMI
df["BMI"] = df["weight"] / ((df["height"]/100)**2)

X = df[["weight","age","activity_level","temperature","BMI"]]
y = df["water_intake"]

model = LinearRegression()
model.fit(X, y)

# UI
st.title("💧 AI-Based Personalized Water Intake Predictor")
st.subheader("Enter your details below 👇")
weight = st.number_input("⚖️ Enter weight (kg)")
height = st.number_input("📏 Enter height (cm)")
age = st.number_input("🎂 Enter age")
activity = st.selectbox("🏃 Activity Level", [1,2,3])
temp = st.number_input("🌡️ Temperature (°C)")

if st.button("Predict"):
    if height > 0:
       bmi = weight / ((height/100)**2)
else:
    st.error("Height cannot be zero")
    bmi = 0   # 👈 important fix
  
    new_data = pd.DataFrame([[weight, age, activity, temp, bmi]],
                            columns=["weight","age","activity_level","temperature","BMI"])
    
    pred = model.predict(new_data)
    water = round(pred[0],2)
    
    st.success(f"Recommended Water Intake: {water} liters 💧")
    st.write("💡 Tip: Drink water throughout the day, not all at once!")

    if water < 2.5:
        st.warning("Drink more water! 😅")
    elif water < 3.5:
        st.info("Good hydration 👍")
    else:
        st.error("High hydration needed 💦")
