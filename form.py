import streamlit as st
import database as db
from PIL import Image

# form

st.set_page_config(page_title="SBR: Submission Form")
st.title("Sikh Business Directory")
st.write("## Submission Form")
st.write("---")

st.subheader("Enter Details of Business")

#with st.form(key="form1", clear_on_submit=False):
    

name = st.text_input("Enter the Business's Name")

category = st.selectbox(
                "Enter Category",
                ("Arts & Crafts", "Clothing", "Education", "Entertainment & Events", "Finance", "Food & Drink", "Gurudwara", "Health & Fitness", "Home & Garden", "Legal", "Technology",  "Travel", "Vehicle", "Other")
                )

if category == "Other": 
    otherOption = st.text_input("Please type in an appropriate category:")
    sub_category = "none"

else:
    sub_category = "none" # default sub_category

# sub-categories

if category == "Arts & Crafts": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Paintings & Illustrations", "Shastar", "Music", "Logo Design", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2
        
if category == "Education": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("School", "Universtity Society", "Tuition", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Entertainment & Events": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Photography", "Wedding Planning", "Venue Hire", "Car Hire", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Finance": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Accountants", "Financial Advice", "Financial Services", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Food & Drink": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Cakes", "Sweets", "Pure Veg", "Non Veg", "Supermarket", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Health & Fitness": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Gym", "Martial Arts", "Supplements", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Home & Garden": 

    sub_category = st.selectbox(
                    "Enter Sub Category", 
                    ("Architects", "Real Estate Agents", "Builders", "Plumbing", "Gas & Electric", "Landscapers", "Other"),
                    key="1"
                    )
    
    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Technology": 

    sub_category = st.selectbox(
                    "Enter Sub Category",
                    ("Websites, UI/UX", "Phone Repair", "Other"),
                    key="2"
                    )

    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

if category == "Vehicle": 

    sub_category = st.selectbox(
                    "Enter Sub Category",
                    ("Dealerships", "Driving Tuition", "Mechanics", "Other"),
                    key="2"
                    )

    if sub_category == "Other": 
        otherOption2 = st.text_input("Please type in an appropriate sub-category:")
        sub_category = otherOption2

st.write("### Location")
online_only = st.radio("Is your Business Online Only?", ["Yes", "No"])

city = "Online Only"
nation = "Online Only"
address = "Online Only"

if online_only == "Yes":
    pass
else:
    city = st.text_input("Enter City", key="city")
    nation = st.text_input("Enter Nation", key="nation")
    st.markdown("Please use the address format provided on [Google Maps](https://www.google.co.uk/maps)")
    address = st.text_input("Enter Address")


st.write("### Links & Contact Info")

link = st.text_input("Enter Link to Website or Social Media page")

telephone = st.text_input("Enter Business Telephone number")

email = st.text_input("Enter Business Email Address")

verified = 0
latitude = 0
longitude = 0
approved_by = "awaiting approval"

st.write("### Submit")

user_email = st.text_input("Please also enter your email in case we need to follow up for more info")

sure_check = st.slider("How sure are you that the information provided is correct?", 0, 100)

if sure_check == 100:
    
    if st.button("Submit"):
        db.insert_record(category, sub_category, name, city, nation, address, link, telephone, email, verified, latitude, longitude, user_email, approved_by)
        st.success("Submitted for review")

elif sure_check > 0 and sure_check < 100 :
    st.write("Go make sure!")
    
st.markdown("---")

logo = Image.open('logo.png')
st.image(logo, width=36)
st.caption("Provided by the [Azadism Project](https://www.azadism.co.uk/)")
