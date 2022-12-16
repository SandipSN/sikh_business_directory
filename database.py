import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd

#load_dotenv('.env')
#SUPABASE_URL = os.getenv("SUPABASE_URL")
#SUPABASE_KEY = os.getenv("SUPABASE_KEY")
#SB_EMAIL = os.getenv("SB_EMAIL")
#SB_PW = os.getenv("SB_PW")

DETA_KEY_BIZ = 'a0gvjtu3_vU7cwRjwhYUVxFqJnXjZHJvVMwK2wd1y'

SUPABASE_URL= "https://pavtvcohcbdqcbdrexrg.supabase.co"
SUPABASE_KEY= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBhdnR2Y29oY2JkcWNiZHJleHJnIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzExMTYxNTAsImV4cCI6MTk4NjY5MjE1MH0.dRY9h5UbsADLP9dNwppvGqxh6mSDndWZuYUpDza4YVw"

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


# Testing Update

record_to_update = "5d40f57c-1725-434c-a4bd-4661875fbfad"

updates = { 
            'Category': "updated!", 
            'Approved By': "updated!", 
            }
                    
update(updates=updates, id=record_to_update)

#insert_record("Test", "Test", "Test", "Test", "Test", "Test", "Test", 1234,  "Test", 0, 0, 0,  "Test", "Test")