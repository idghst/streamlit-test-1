import streamlit as st
import time

def stream_data(data):
    for word in data.split(" "):
        yield word + " "
        time.sleep(0.02)

animal_shelter = ['고양이', '강아지', '토끼', '새']

st.set_page_config(
    page_title="Animal Chat",
    page_icon="🤖"
)

st.title(":red[Animal] Chat")

if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = None

if "processComplete" not in st.session_state:
    st.session_state.processComplete = None

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant", 
                                    "content": "안녕하세요! 동물을 맞춰보세요!"}]
# if 'messages' not in st.session_state:
#     st.session_state['messages'] = [{"role": "assistant", 
#                                     "content": "안녕하세요! 주어진 문서에 대해 궁금하신 것이 있으면 언제든 물어봐주세요!"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if query := st.chat_input("질문을 입력해주세요."):
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        have_it = query.lower() in animal_shelter
        response = '정답!!' if have_it else '오답!!!!'
        st.write_stream(stream_data(response))

    st.session_state.messages.append({"role": "assistant", "content": response})
