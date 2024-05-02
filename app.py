import streamlit as st
st.title("Hi! This app is designed for LLM Apps")
st.subheader("App for LLM again...")
st.header("App for LLM again...")
st.text("hello i am garima an aspiring data scientist....")
st.markdown("**hello** *world*") # ** to make it bold and * to italisize
st.caption("Hi this is Mistral app")
json={"a":"1,2,3","b": "4,5,6"}
st.json(json) # Adds json function
st.image("download.png",caption="This is downloadable")
#st.audio("audio.mp3")
#st.video("video.mp4")
#Checkbox
state=st.checkbox("checkbox",value=True)
if state:
    st.write("Hello you are in the app section")
else:
    pass
#Radio buttons
radio_btn=st.radio("Which country do you live in?",options=("US","UK","India"))
#Buttons
def click():
    print("Hello there!")
btn=st.button("Click me!",on_click=click)
#Creating form
form=st.form("Form")
form.text_input("First Name")
form.form_submit_button("Submit")
#2nd method to create form
with st.form("Form 2"):
    st.text_input("First Name")
    st.form_submit_button("Submit")
#Dividing the form in 2 columns
with st.form("Form"):
    col1,col2=st.columns(2)
    col1.text_input("First Name")
    col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    st.form_submit_button("Submit")