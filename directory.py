import streamlit as st
import database as db
import pandas as pd 
from st_aggrid import GridOptionsBuilder, AgGrid, JsCode, GridUpdateMode, DataReturnMode
import folium
from streamlit_folium import st_folium
from PIL import Image
import branca

st.set_page_config(page_title="Sikh Business Directory")

banner = Image.open('banner.svg')
st.image(banner)

#st.title("Sikh Business Directory")

st.markdown("---")

data = db.fetchdb({"Verified": 1})
df = pd.DataFrame(data)
directory = df[['Name', 'Link', 'Category', 'Sub Category', 'City', 'Nation', 'Address',  'Telephone', 'Email', 'LATITUDE', 'LONGITUDE']] 

#AgGrid(directory)

gb = GridOptionsBuilder.from_dataframe(directory)
#gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar(columns_panel=False) #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection

# Enable hyperlinks
cellRenderer = JsCode("""
function(params) {return`<a href=${params.value} target="_blank">${params.value}</a>`}"""
)
gb.configure_column("Link", cellRenderer=cellRenderer)

gridOptions = gb.build()

grid_response = AgGrid(
    directory,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    #theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=450, 
    width='100%',
    reload_data=False,
    allow_unsafe_jscode=True
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
selected_df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

loc_data = data[data['LATITUDE'] != 0] # filter data for all records that contain a physical location

#st.write(loc_data)

### MAP

def popup_html(df, row):
    i = row
    name=df['Name'].iloc[i] 
    link=df['Link'].iloc[i]
    category=df['Category'].iloc[i]
    telephone=df['Telephone'].iloc[i]
    
    left_col_color = "#FFFFFF"
    right_col_color = "#FFFFFF"
    
    html = """<!DOCTYPE html>
<html>
<head>
<h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(name) + """
</head>
    <table style="height: 50px; width: 250px;">
<tbody>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Category</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(category) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Link</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(link) + """
</tr>
<tr>
<td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Telephone</span></td>
<td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(telephone) + """
</tr>

</tbody>
</table>
</html>
"""
    return html



try:
    location = selected_df['LATITUDE'].mean(), selected_df['LONGITUDE'].mean() #Specify the center of the map by using the average of latitude and longitude coordinates

    m = folium.Map(location=location, zoom_start=10) #Create a empty folium map object

    for i in range(0,len(selected_df)):
                
        #labels=selected_df['Name'].iloc[i] #Create a lable that is the name of the institution

        html = popup_html(selected_df, i)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)

        folium.Marker([selected_df['LATITUDE'].iloc[i],selected_df['LONGITUDE'].iloc[i]],popup=popup).add_to(m)


except:
    location = loc_data['LATITUDE'].mean(), loc_data['LONGITUDE'].mean()

    m = folium.Map(location=location, zoom_start=3) #Create a empty folium map object

    for i in range(0,len(loc_data)):

        html = popup_html(loc_data, i)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)

        folium.Marker([loc_data['LATITUDE'].iloc[i],loc_data['LONGITUDE'].iloc[i]],popup=popup).add_to(m)


st_data = st_folium(m, height= 350, width=725)

st.markdown("---")
st.markdown("## Submit")
st.markdown("Want to add a business? Use the form linked [here](https://sikh-business-directory-form.streamlit.app/) to submit it for review")

st.markdown("---")

logo = Image.open('logo.png')
st.image(logo, width=36)
st.caption("Provided by the [Azadism Project](https://www.azadism.co.uk/)")
