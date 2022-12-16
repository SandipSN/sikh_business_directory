import streamlit as st
import pandas as pd 
import database as db
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import json

names = ["Ranjit Singh", "test 1", "test 2"]
usernames = ["rsingh", "test1", "test 2"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sikh_biz_dir", "akaaal", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    st.title("Staging Area")
    st.subheader("Review record")

    data = db.fetchdb(0)
    json_data = data.json()
    json_data = json.loads(json_data)
    df = pd.json_normalize(json_data, 'data')

    df = df.set_index('ID')

    st.write(df)

    key_in = st.text_input('Paste key for record to verify/reject')

    if key_in == "":

        st.write("Waiting for key...")
    
    else:

        st.markdown("---")

        name = st.metric(label="Name", value=df.loc[key_in, "Name"])

        name_check = st.checkbox('Update?')

        if name_check:
            name = st.text_input("Enter the Business's Name")
        
        st.markdown("---")

        category = st.metric(label="Category", value=df.loc[key_in, "Category"])

        cat_check = st.checkbox('Update?', key="cat_check")

        if cat_check:
            category = st.selectbox(
                        "Enter Category",
                        ("Arts & Crafts", "Clothing", "Entertainment & Events", "Finance", "Food & Drink", "Gurudwara", "Health & Fitness", "Home & Garden", "Legal", "Technology",  "Travel", "Vehicle", "Other")
                        )

            if category == "Other": 
                otherOption = st.text_input("Please type in an appropriate category:")
                sub_category = "none"

            else:
                sub_category = "none" # default sub_category

        
        st.markdown("---")

        sub_category = st.metric(label="Sub Category", value=df.loc[key_in, "Sub Category"])
        
        sub_cat_check = st.checkbox('Update?', key="sub_cat_check")

        if sub_cat_check:

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
                                ("Real Estate Agents", "Builders", "Plumbing", "Gas & Electric", "Landscapers", "Other"),
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

        st.markdown("---")

        st.write("### Location")
        
        city = st.metric(label="City", value=df.loc[key_in, "City"])
        
        city_check = st.checkbox('Update?', key="city_check")
        
        if city_check:

            city = st.text_input("Enter City", key="city")

        nation = st.metric(label="Nation", value=df.loc[key_in, "Nation"])
        
        nation_check = st.checkbox('Update?', key="nation_check")
        
        if nation_check:

            nation = st.text_input("Enter Nation", key="nation")
        
        address = st.metric(label="Address", value=df.loc[key_in, "Address"])
        
        address_check = st.checkbox('Update?', key="address_check")
        
        if address_check:

            st.markdown("Please use the address format provided on [Google Maps](https://www.google.co.uk/maps)")
            address = st.text_input("Enter Address")
        
        st.markdown("---")

        st.markdown("Copy/Paste address into [Google Maps](https://www.google.co.uk/maps), and right click on the marker for these values:")

        latitude = st.metric(label="LATITUDE", value=df.loc[key_in, "LATITUDE"])
               
        latitude_check = st.checkbox('Update?', key="latitude_check")
        
        if latitude_check:

            latitude = st.text_input("Enter the Latitude")
                   
        longitude = st.metric(label="LONGITUDE", value=df.loc[key_in, "LONGITUDE"])
                
        longitude_check = st.checkbox('Update?', key="longitude_check")
        
        if longitude_check:

            longitude = st.text_input("Enter the Longitude")
            
        st.markdown("---")

        st.write("### Links & Contact Info")

        link = st.metric(label="Link", value=df.loc[key_in, "Link"])
        
        link_check = st.checkbox('Update?', key="link_check")
        
        if link_check:

            link = st.text_input("Enter Link to Website or Social Media page")


        telephone = st.metric(label="Telephone", value=df.loc[key_in, "Telephone"])
        
        telephone_check = st.checkbox('Update?', key="telephone_check")
        
        if telephone_check:
            
            telephone = st.text_input("Enter Business Telephone number")
        

        email = st.metric(label="Email", value=df.loc[key_in, "Email"])
        
        email_check = st.checkbox('Update?', key="email_check")
        
        if email_check:
            email = st.text_input("Enter Business Email Address")
            
        st.markdown("---")

        user_email = st.metric(label="Email", value=df.loc[key_in, "User Email"])
            
        st.markdown("---")

        check = st.radio(
            "Verify or Reject Record",
            ('Verify', 'Reject'))

        if check == "Verify":
            verified = 1
        else:
            verified = 2

        sure_check = st.slider(
            'Slide to 100 if you are sure',
            0.0, 100.0)

       
        if sure_check == 100:

            approved_by = st.text_input("Enter Your Username")
            
            if st.button('Confirm'):
                
                updates = json.dumps{ 
                        'Category': str(category), 
                        'Sub Category': str(sub_category),
                        'Name': str(name),
                        'City': str(city),  
                        'Nation': str(nation), 
                        'Address': str(address), 
                        'Link': str(link), 
                        'Telephone': str(telephone), 
                        'Email': str(email),
                        'Verified': int(verified),
                        'LATITUDE': str(latitude),
                        'LONGITUDE': str(longitude),
                        'Approved By': str(approved_by)
                        }
                    
                db.update(updates=updates, id=key_in)   
                st.info("Records Updated!: Verified")

            else:
                st.write("Make Sure to double check") 

        elif sure_check > 0 and sure_check < 100 :
            st.write("Go make sure!")
