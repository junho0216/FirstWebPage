import streamlit as st
import pandas as pd

# Streamlit 앱 제목
st.title('KBO 팀 우승 확률 예측기')

# KBO 팀 데이터 (예시 데이터)
data = {
    '팀': [
        '두산 베어스', 'LG 트윈스', '롯데 자이언츠', 
        '키움 히어로즈', 'KIA 타이거즈', '삼성 라이온즈', 
        'SSG 랜더스', '한화 이글스', 'NC 다이노스'
    ],
    '승률': [0.600, 0.550, 0.500, 0.520, 0.480, 0.530, 0.600, 0.450, 0.490],
    '득점': [600, 550, 500, 520, 480, 510, 600, 450, 490],
    '실점': [500, 520, 550, 510, 540, 500, 480, 580, 500],
    '홈런': [150, 120, 100, 130, 90, 110, 160, 80, 95],
    'ERA': [3.50, 4.00, 4.50, 3.80, 4.10, 3.70, 3.40, 5.00, 4.20]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 런 디퍼런스 계산
df['런 디퍼런스'] = df['득점'] - df['실점']

# 우승 확률 계산 함수
def calculate_championship_probability(row):
    return (row['승률'] * 0.4 + 
            (row['런 디퍼런스'] / max(df['런 디퍼런스'])) * 0.3 + 
            (row['홈런'] / max(df['홈런'])) * 0.2 - 
            (row['ERA'] / max(df['ERA'])) * 0.1)

# 우승 확률 계산
df['우승 확률'] = df.apply(calculate_championship_probability, axis=1)

# 결과 출력
st.subheader('팀별 우승 확률')
st.write(df[['팀', '우승 확률']])

# 우승 확률 시각화
st.bar_chart(df.set_index('팀')['우승 확률'])



