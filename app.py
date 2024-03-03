import streamlit as st
import numpy as np
import pandas as pd


import pickle 
pickle_in = open('Km.pkl' , 'rb')

Km = pickle.load(pickle_in)

def Student_Segmentation (cgpa , iq):

    cgpa =float(cgpa)
    iq   =float(iq )

    prediction = Km.predict([[cgpa , iq]])

    print(prediction[0])
    return prediction[0]

def main():
    st.title("Student Segmentation")   
    html_temp = """
    <div style = "background-color : tomato; padding : 10px">
    <h2 style = "color:white ; text-align:centre;> Student Segmentation ML App</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html= True)
    cgpa = st.text_input('cgpa', "")
    iq   = st.text_input('iq  ', "")


    result = ""

    if st.button("predict"):
        result = Student_Segmentation (cgpa , iq)
        if result == 0 :
            result = 'Low Performance Student'
        elif result ==1 : 
            result  ='High performance Students' 
        elif result == 2 :
            result  = 'Chilling Students'
        else :
            result = "HardWorking Students"
       
    st.success("The Output is {}".format(result))    
    if st.button("About"):
        st.text("Let's Learn")

        st.text("Built With Streamlit")
 

if __name__ == '__main__' :
    main()