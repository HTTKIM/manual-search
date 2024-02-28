import streamlit as st
from streamlit_option_menu import option_menu 

# Python 파일의 이름을 import
import architech, electric, gas

st.set_page_config(
        page_title="Manual List",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():

        with st.sidebar:        
            app = option_menu(
                menu_title='Select Manual',
                options=['건축','전기','가스'],
                icons=['buildings','plug', 'cloud-fog2'],
                menu_icon='list-task',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "건축":
            architech.app()
        if app == "전기":
            electric.app()    
        if app == "가스":
            gas.app()
             
    run()            
         