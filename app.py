import streamlit as st

# Function to convert length units
def length_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Kilometers": 0.001,
        "Miles": 0.000621371
    }
    return round(value * conversion_factors[to_unit] / conversion_factors[from_unit], 2)

# Function to convert temperature units
def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return round((value * 9/5) + 32, 2)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return round((value - 32) * 5/9, 2)
    return round(value, 2)

# Streamlit App Title
st.title("🔥 Unit Converter App 🔄")

# Select conversion category
category = st.selectbox("📌 Select Conversion Category", ["Length", "Temperature"])

# Length Conversion Section
if category == "Length":
    st.subheader("📏 Length Converter")
    value = st.number_input("🔢 Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("🔄 From Unit", ["Meters", "Feet", "Inches", "Kilometers", "Miles"])
    to_unit = st.selectbox("🔄 To Unit", ["Meters", "Feet", "Inches", "Kilometers", "Miles"])
    
    if st.button("✅ Convert"):
        result = length_conversion(value, from_unit, to_unit)
        st.success(f"🎯 {value:.2f} {from_unit} is {result:.2f} {to_unit}")

# Temperature Conversion Section
elif category == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    value = st.number_input("🔢 Enter value:", format="%.2f")
    from_unit = st.selectbox("🔄 From Unit", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("🔄 To Unit", ["Celsius", "Fahrenheit"])
    
    if st.button("✅ Convert"):
        result = temperature_conversion(value, from_unit, to_unit)
        st.success(f"🎯 {value:.2f} {from_unit} is {result:.2f} {to_unit}")
