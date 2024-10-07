import streamlit as st
import pandas as pd
import numpy as np

# Streamlit 앱 제목
st.title('KBO 팀 우승 확률 예측기')

# KBO 팀명 리스트
teams = [
    '두산 베어스', 'LG 트윈스', '롯데 자이언츠', 
    '키움 히어로즈', 'KIA 타이거즈', '삼성 라이온즈', 
    'SSG 랜더스', '한화 이글스', 'NC 다이노스'
]

# 랜덤 데이터 생성
num_teams = len(teams)
np.random.seed()  # 시드를 설정하여 매번 다른 랜덤 값 생성

# 랜덤 성적 데이터 생성
data = {
    '팀': teams,
    '승률': np.round(np.random.uniform(0.400, 0.700, num_teams), 3),
    '득점': np.random.randint(400, 800, num_teams),
    '실점': np.random.randint(400, 800, num_teams),
    '홈런': np.random.randint(70, 200, num_teams),
    'ERA': np.round(np.random.uniform(3.00, 5.50, num_teams), 2)
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




