import streamlit as st

# Student Details
st.header("Student Details")

name = st.text_input("Student Name:")
branch = st.text_input("Branch:")

# University Selection
universities = ["ANDHRA UNIVERSITY","Acharya Nagarjuna University", "sastry University", "Andhra University", "Damondaram Sanjivayya National Law University", "Dr. B.R. Ambedkar University","NTR Health University", "Darvidian University", "Gandhi Insitute of technology"]
university = st.selectbox("University:", universities)

if university == "ANDHRA UNIVERSITY":
    colleges = ["AMAL DEGREE COLLEGE", "MR COLLEGE FOR MEN", "GAYATRI VIDYA PARISHAD COLLEGE FOR DEGREE AND PG COURSES", "ST JOSEPHS DEGREE COLLEGE FOR WOMEN",""]
    college = st.selectbox("College:", colleges)
elif university == "Stanford University":
    colleges = ["School of Humanities and Sciences", "School of Engineering", "Graduate School of Business"]
    college = st.selectbox("College:", colleges)
elif university == "Massachusetts Institute of Technology":
    colleges = ["School of Science", "School of Engineering", "Sloan School of Management"]
    college = st.selectbox("College:", colleges)

# College Selection
st.header("College Selection")

if college is not None:
    st.write(f"You have selected {college}.")

    # Display additional information about the college
    if college == "College of Letters and Science":
        st.write("The College of Letters and Science is the largest of the colleges at UC Berkeley.")
    elif college == "College of Engineering":
        st.write("The College of Engineering is the second largest of the colleges at UC Berkeley.")
    elif college == "Haas School of Business":
        st.write("The Haas School of Business is one of the top business schools in the world.")
    elif college == "School of Humanities and Sciences":
        st.write("The School of Humanities and Sciences is the largest of the schools at Stanford University.")
    elif college == "School of Engineering":
        st.write("The School of Engineering is one of the top engineering schools in the world.")
    elif college == "Graduate School of Business":
        st.write("The Graduate School of Business is one of the top business schools in the world.")

    # Display a link to the college's website
    st.write(f"[Visit the {college} website](https://{college}.edu)")
