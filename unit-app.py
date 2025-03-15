import streamlit as st

st.title("🌎 Unit Converter App ")
st.markdown("### Convert Length, Weight and Time Instantly")
st.write("Welcome! Select a Category, Enter a Value a get a Converted Results in Real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Mintues to hours":
            return value / 60   
        elif unit == "Hours to mintues":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("📏 Select Convertion", ["Kilometers to miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Convertion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Convertion", ["Seconds to Minutes", "Minutes to seconds","Mintues to hours","Hours to mintues", "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")