import streamlit as st
import time
# import pandas as pd

st.write("# ANIMAL GPT")
# st.write("Hello *wo")

# st.write("st.success('Done!')")
# st.success('Done!')

animal_shelter = ['고양이', '강아지', '토끼', '새']

animal = st.text_input('INPUT')

with st.spinner('Wait for it...'):
    # time.sleep(5)
    if animal:
        have_it = animal.lower() in animal_shelter
        '그거 있음' if have_it else '그건 없음!!!'
