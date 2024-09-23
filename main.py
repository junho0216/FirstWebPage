import streamlit as st
 
# 타이틀 적용 예시
st.title('좌표평면')

# 특수 이모티콘 삼입 예시
#  emoji: htts://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('좌표평면 그래프 :sparkles:')

# Header 적용
st.header('헤더는 섹션의 제목 :sparkles:')

#Subheader 적용
st.subheader('subheader는  섹션의 부제목')



#캡션 적용
st.caption('캡션은 짧은 설명을 추가하는 것!')

#코드 표시
sample_code='''
def function():
   print('hello,  world')
'''
st.code(sample_code, language="python")

# 일반 테스트
st.text('일반적인 텍스트를 입력해 보았습니다.')




# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다')
# 컬러코드: blue, green, orange, red, violet
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")


#LaTex 수식 지원
#복잡한 수학공식, 기호 등을 웸 페이지에서 깔끔한 수식으로 변환
st.latex(r'\sqrt{x^2+y^2}=1')
