from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI
import time

def app():
    load_dotenv()
    API_KEY = os.environ['OPENAI_API_KEY']

    client = OpenAI(api_key=API_KEY)

    # thread id 생성하여 하나로 관리
    if 'thread_id' not in st.session_state:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id  
        
    # thread_id, assistant_id 설정
    thread_id = st.session_state.thread_id
    assistant_id = "asst_qTi5r7qcM3HI065ewDdFhC6B"

    # 메세지 불러오기
    thread_messages = client.beta.threads.messages.list(thread_id, order="asc")

    # 페이지 제목
    st.subheader(":blue[위험물 분야] :gray[안전점검 매뉴얼 Chatbot]")

    # 메세지 역순으로 가져와 UI 에 입력
    for msg in thread_messages.data:
        with st.chat_message(msg.role):
            st.write(msg.content[0].text.value)

    # 입력창에 입력을 받아 입력된 내용으로 메세지 생성        
    prompt = st.chat_input("[위험물] 질문을 입력하세요!")
    if prompt:
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=prompt
        )
        
        # 입력한 메세지 UI에 표시
        with st.chat_message(message.role):
            st.write("[법령(건축 및 가스)] " + message.content[0].text.value)
        

        with client.beta.threads.runs.stream(
            thread_id=thread_id,
            assistant_id=assistant_id,
            event_handler=EventHandler(),
            ) as stream:
            st.write_stream(stream.text_deltas)
            stream.until_done()
