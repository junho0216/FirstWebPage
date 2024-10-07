import streamlit as st
import pandas as pd

# Streamlit 앱 제목
st.title('KBO 팀 우승 확률 예측기')

# 데이터 입력 (예시 데이터)
data = {
    '팀': ['팀A', '팀B', '팀C', '팀D'],
    '승률': [0.600, 0.550, 0.500, 0.450],
    '득점': [600, 550, 500, 450],
    '실점': [500, 520, 550, 580],
    '홈런': [150, 120, 100, 80],
    'ERA': [3.50, 4.00, 4.50, 5.00]
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


