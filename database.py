from deta import Deta
import streamlit as st

DETA_KEY_BIZ = st.secrets["DETA_KEY_BIZ"]

deta = Deta(DETA_KEY_BIZ)

db = deta.Base("biz_dir")

def insert_record(biz_id, category, sub_category, name, city, nation, address, link, telephone, email, verified, latitude, longitude):
    return db.put({ 
        'Biz ID': biz_id, 
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
        'LONGITUDE': longitude
        })

def fetchdb(query):
    res = db.fetch(query)
    return res.items