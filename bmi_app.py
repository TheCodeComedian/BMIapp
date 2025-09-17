#taking inputs
import streamlit as st
st.title("This is the Ai-based BMI calculator. Know your health!")
name= st.text_input("What is your name?")
wt= st.number_input("Enter your weight")
ht= st.slider("Enter your height in cm",122,213)
st.write(f"Selected: {ht}")
g= st.selectbox("Choose an option:",["Female","Male"])
st.write(f"Selected: {g}")

#calculating BMI
bmi= round(wt/(ht/100)**2,2)
st.write(f"Hi {name}! With your height {ht}cm and weight {wt}kg, your BMI is: {bmi}")

#getting Ai response
import google.generativeai as GenAi
GenAi.configure(api_key="AIzaSyBwbdz4JyJM7BQKQUH8-0EioH5Y7OzfogY")
Model = GenAi.GenerativeModel(model_name= "gemini-2.5-flash-lite")

if name and wt>0:
    prompt= f"Act like a nutritionist and tell me whether with the given height of {ht}, weight of {wt}, sex of {g} and BMI of {bmi}, the individual seems healthy or not. Just reply in a couple of sentences."
    response= Model.generate_content(prompt)
    st.markdown(response.text)

