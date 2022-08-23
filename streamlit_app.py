
Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
1 of 10
inputs streamlit
Inbox
Juliette Mayorga
	
Attachments10:46 PM (40 minutes ago)
	
to me

Attachments area
	
	
	

import streamlit as st

st.set_page_config(
    page_title='Training 3',
    layout='wide'
)

def two_columns():
    return st.columns(2)

options = ['abc', 'def', 'ghi', 123, 456, '789']

input_objects = [
    "st.selectbox('selectbox', options)",
    "st.multiselect('multiselect', options)",
    "st.radio('radio', options)",
    "st.button('button')",
    "st.checkbox('checkbox')",
    "st.slider('slider')",
    "st.select_slider('select_slider', options)",
    "st.text_input('text_input')",
    "st.number_input('number_input')",
    "st.text_area('text_area')",
    "st.date_input('date_input')",
    "st.time_input('time_input')",
    "st.color_picker('color_picker')",
    "st.file_uploader('file_uploader')",
    "st.download_button('download_button', 'downloaded')"
]

st.header("Input Objects")

col1, col2 = two_columns()
col1.markdown('#### Object')
col2.markdown('#### Stored Value')

for input_obj in input_objects:
    col1, col2 = two_columns()
    
    with col1:
        value = eval(input_obj)
    with col2:
        '.'
        value

inputs.py
Displaying inputs.py.
