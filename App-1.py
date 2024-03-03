import streamlit as st

import pickle 

pickle_in = open("km.pkl", "rb")
km = pickle.load(pickle_in)

def student_segmentation(cgpa, iq):
    cgpa = float(cgpa)
    iq = float(iq)

    prediction = km.predict([[cgpa, iq]])
    print(prediction[0])
    return prediction[0]

def main():
    st.title("Student segmentation")
    html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:gray;text-align:center;">Student Segmentation ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    cgpa = st.text_input("cgpa", "type here")
    iq = st.text_input("iq", "type here")
    result = ""
    if st.button("Predict"):
        result = student_segmentation(cgpa, iq)
        if result == 0:
            result = "low performing students"
        elif result == 1:
            result = "High performing students"
        elif result == 2:
            result = "Under performing students"
        else:
            result = "Hardworking students"
    st.success("The output is {}".format(result))

    if st.button("About"):
        st.text("Create web app of student segmentation by streamlit")

if __name__ == '__main__':
    main()