import streamlit as st
from streamlit_option_menu import option_menu 

# Python 파일의 이름을 import
import architech, electric, gas, fireprotection, hazard, kfs, law_1

# 페이지 설정
st.set_page_config(page_title="KFPA Manual", page_icon="emb.png")

# 분야에 따른 앱 실행
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.image('remove.png')
        st.header("예방안전본부 Chatbot :open_book:")
        st.divider()

        with st.sidebar:   
            st.image('manualimage.PNG')
            st.header("About")
            st.markdown("매뉴얼 내용과 KFS 기반으로 답변합니다")
            st.markdown("[안전점검매뉴얼 11판 994 Page]")
            st.write("")
            st.header("Select Manual")
            app = option_menu(
                menu_title='안전점검 매뉴얼',
                options=['분야를 선택하세요', '건축 피난','전기','가스','소방시설','위험물', 'KFS', '법(건축 및 가스)'],
                icons=['','buildings','plug', 'cloud-fog2','shield','droplet-fill','book', 'journal-text'],
                menu_icon='list-task',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#cfe0de"},
        "nav-link-selected": {"background-color": "#e6f9f7"},}                
                )
            st.image('KV1.png')
        
        if app == '분야를 선택하세요':
            st.markdown("***:red[Sidebar]*** 에서 분야를 선택해주세요!")
        else:
            # 선택된 분야에 따라 해당 앱 실행
            if app == "건축 피난":
                architech.app()
            if app == "전기":
                electric.app()    
            if app == "가스":
                gas.app()
            if app == "소방시설":
                fireprotection.app()
            if app == "위험물":
                hazard.app()
            if app == "KFS":
                kfs.app()
            if app == "법(건축 및 가스)":
                law_1.app()

if __name__ == "__main__":
    app = MultiApp()
    app.run()         
