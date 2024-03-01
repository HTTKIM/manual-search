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
    assistant_id = "asst_KqyzQbzlJtvmp0IfRKX91iaP"

    # 메세지 불러오기
    thread_messages = client.beta.threads.messages.list(thread_id, order="asc")

    # 페이지 제목
    st.subheader(":blue[KFS 기준] :gray[검색 Chatbot]")

    # 메세지 역순으로 가져와 UI 에 입력
    for msg in thread_messages.data:
        with st.chat_message(msg.role):
            st.write(msg.content[0].text.value)

    # 입력창에 입력을 받아 입력된 내용으로 메세지 생성        
    prompt = st.chat_input("[KFS] 질문을 입력하세요!")
    if prompt:
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=prompt
        )
        
        # 입력한 메세지 UI에 표시
        with st.chat_message(message.role):
            st.write("[KFS] " + message.content[0].text.value)
        
        # Run 돌리기
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )
        
        counter = 0  # 상태 확인 카운터 초기화
        with st.spinner('답변을 생성하고 있습니다...'):
            while run.status != 'completed':
                run = client.beta.threads.runs.retrieve(
                    thread_id=thread_id,
                    run_id=run.id
                )
                if run.status == 'completed':
                    break
                if counter % 5 == 0:  # 매 10회 확인마다 run의 상태를 출력
                    print(f"\t\t{run}")
                counter += 1
                time.sleep(1)  # 상태 확인 간 3초 대기
        
        # While 문 완료 후 메세지 불러오기
        messages = client.beta.threads.messages.list(
            thread_id=thread_id   
        )
        
        # 마지막 메세지 UI에 추가하기
        with st.chat_message(messages.data[0].role):
            st.write(messages.data[0].content[0].text.value)
