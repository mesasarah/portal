import streamlit as st
import openpyxl


# Initialize Excel workbook
wb = openpyxl.Workbook()
worksheet = wb.active

# Set page title and subtitle
st.title("Board of Community Development")
st.subheader("Student Details")

# Create form elements for student details
student_name = st.text_input(label="Student Name:")
branch = st.text_input(label="Branch:")
email = st.text_input(label="Email:")

# Dynamic university selection
selected_university = st.selectbox(label="University:", options=["Select University", "University 1", "University 2"])

# Dynamic college selection based on university choice
if selected_university == "University 1":
    college_options = ["College 1A", "College 1B"]
elif selected_university == "University 2":
    college_options = ["College 2A", "College 2B"]
else:
    college_options = []

selected_college = st.selectbox(label="College:", options=college_options)

submitted = st.button(label="Submit")

if submitted:
    # Process user input and store it in Excel
    worksheet.append([student_name, branch, email, selected_university, selected_college])
    wb.save(r"c:\Users\mesaz\OneDrive\Desktop\student.xlsx")


    # Display success message
    st.success("Student details submitted successfully!")
