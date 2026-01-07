import streamlit as st
import joblib
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="💰",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    data = joblib.load("insurance_model.joblib")
    return data["model"], data["features"]

model, feature_columns = load_model()

# ---------------- TITLE ----------------
st.title("💰 Insurance Cost Prediction")
st.write("Predict medical insurance cost based on user details")

st.divider()

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("🧾 Enter User Details")

age = st.sidebar.number_input("Age", 1, 100, 30)
bmi = st.sidebar.number_input("BMI", 10.0, 50.0, 25.0)
children = st.sidebar.number_input("Number of Children", 0, 10, 0)

sex = st.sidebar.selectbox("Sex", ["male", "female"])
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# ---------------- INPUT SUMMARY ----------------
st.subheader("📋 Input Summary")

input_summary = pd.DataFrame({
    "Feature": [
        "Age", "BMI", "Number of Children",
        "Sex", "Smoker", "Region"
    ],
    "Value": [
        age, bmi, children,
        sex, smoker, region
    ]
})

st.table(input_summary)

st.divider()

# ---------------- PREPROCESS FUNCTION ----------------
def preprocess_input(feature_columns):
    df = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex": [sex],
        "smoker": [smoker],
        "region": [region]
    })

    df = pd.get_dummies(df, drop_first=True)
    df = df.reindex(columns=feature_columns, fill_value=0)
    return df

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Insurance Cost"):
    input_df = preprocess_input(feature_columns)
    prediction = model.predict(input_df)[0]

    st.success(f"💸 Estimated Insurance Cost: ₹ {prediction:,.2f}")
    st.info("Prediction generated using a Linear Regression model.")

# ---------------- FOOTER ----------------
st.divider()
st.caption("Developed by Vishal Lashkar | Machine Learning Project")
