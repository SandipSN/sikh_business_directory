from supabase import create_client, Client
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

url: str = SUPABASE_URL
key: str = SUPABASE_KEY

supabase: Client = create_client(url, key)

def insert_record(category, sub_category, name, city, nation, address, link, telephone, email, verified, latitude, longitude, user_email, approved_by):

    data = supabase.table("sikh_business_directory").insert({ 
        'Category': category, 
        'Sub Category': sub_category,
        'Name': name,
        'City': city,  
        'Nation': nation, 
        'Address': address, 
        'Link': link, 
        'Telephone': telephone, 
        'Email': email,
        'Verified': verified,
        'LATITUDE': latitude,
        'LONGITUDE': longitude,
        'User Email': user_email,
        'Approved By': approved_by
        }
       
    ).execute()
    
    assert len(data.data) > 0


def fetchdb(verified):
    data = supabase.table("sikh_business_directory").select("*").eq("Verified", verified).execute()

    if data != 0:
        return data
    else:
        return 'insert data'



def update(updates, id):
    data = supabase.table("sikh_business_directory").update(updates).eq("ID", id).execute()

    if data != 0:
        return data
    else:
        return 'insert data'
