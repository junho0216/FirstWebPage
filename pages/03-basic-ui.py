import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

#버튼 클릭
button = st.button('버튼을 눌러보세요')
if button:
     st.write(':blue[버튼]이 눌렸습니다 :sparkles:')







#파일 다운로드  버튼
#샘플 데이터 생성
dataframe =  pd.DataFrame({
     'first column':['Kor','eng','math','science'],
     'sound colum':[10, 20, 30, 40]
})


#다운로드 버튼 연결
st.download_button(
     label='CSV로 성적표 다운로드',
     data=dataframe.to_csv(),      #dataframe을 csv 형태로 변환
     file_name='sample.csv',
     mime='text/csv'               #데이터 유형
)









#체크 박스
agree = st.checkbox('동의 하십니까?')
if agree:
     st.write('동의 해주셔서 감사합니다:100:')

#라디오 선택 버튼
mbti=st.radio(
     '당신의 MBTI는 무엇입니까?',
     ('ISTJ', 'ENFP', '선택지 없음'))

if mbti == 'ISTJ':
     st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
     st.write('당신은 :green[활동가] 이시네요')
else:
     st.write('당신에 대해 :red[알고 싶어요]:grey_exclamation:')
#텍스트 입력
title = st.text_input(
     label='가고 싶은 여행지가 있나요?',
     placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한  야행지: :violet[{title}]')


#슬라이더
values = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요 :sparkles: ',  # 질문
    min_value=0.0,  # 최소값
    max_value=100.0,  # 최대값
    value=(25.0, 75.0)  # 초기값 (튜플)
)
