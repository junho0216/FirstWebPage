import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
     st.write(':blue[버튼]이 눌렸습니다 :sparkles:')
