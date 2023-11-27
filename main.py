import streamlit as st
import openpyxl
import requests

def save_workbook(filename, url):
    # Download the current Excel file from the cloud storage
    response = requests.get(url)
    with open('temp.xlsx', 'wb') as f:
        f.write(response.content)

    # Load the downloaded file into an openpyxl workbook
    wb = openpyxl.load_workbook('temp.xlsx')
    worksheet = wb.active

    # Append user input to the worksheet
    worksheet.append([student_name, branch, email, selected_university, selected_college])

    # Save the updated workbook back to the cloud storage
    wb.save('temp.xlsx')
    response = requests.put(url, data=open('temp.xlsx', 'rb').read(), headers={'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})

    # Delete the temporary file
    os.remove('temp.xlsx')


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
    save_workbook(r"https://docs.google.com/spreadsheets/d/1Wv3fCL3PjdBNHZXFu4uu_t76fjeprwOd/edit?usp=drive_link&ouid=117306722142764576579&rtpof=true&sd=true", cloud_storage_url)



    # Display success message
    st.success("Student details submitted successfully!")
