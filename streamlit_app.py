import streamlit as st
import pandas as pd
import numpy as np
import time  # matplotlib 제거, time만 사용

# 페이지 제목과 설명
st.title("Streamlit 요소 예시 페이지")  # 페이지 상단 제목
st.header("이 페이지는 다양한 Streamlit 요소를 보여줍니다.")  # 큰 헤더
st.subheader("아래에서 각각의 요소를 확인하세요!")  # 작은 헤더
st.markdown("**Streamlit을 활용하면 다양한 UI 요소를 쉽게 만들 수 있습니다.**")  # 마크다운 텍스트

# 텍스트 입력
name = st.text_input("이름을 입력하세요")  # 텍스트 입력창

# 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, value=25)  # 숫자 입력창

# 텍스트 영역
bio = st.text_area("자기소개를 입력하세요")  # 여러 줄 텍스트 입력

# 체크박스
agree = st.checkbox("개인정보 수집에 동의합니다")  # 체크박스

# 라디오 버튼
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼

# 셀렉트박스
country = st.selectbox("국가를 선택하세요", ["한국", "미국", "일본", "중국"])  # 드롭다운 셀렉트박스

# 멀티 셀렉트
hobbies = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "여행", "음악"])  # 여러 개 선택 가능

# 슬라이더
score = st.slider("점수를 선택하세요", min_value=0, max_value=100, value=50)  # 슬라이더

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드

# 날짜 입력
date = st.date_input("날짜를 선택하세요")  # 날짜 선택

# 시간 입력
time_input = st.time_input("시간을 선택하세요")  # 시간 선택

# 버튼
if st.button("제출하기"):
    st.success("제출되었습니다!")  # 버튼 클릭 시 메시지 표시

# 컬럼 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.write("왼쪽 컬럼입니다.")
with col2:
    st.write("오른쪽 컬럼입니다.")

# Expander (접기/펼치기)
with st.expander("더보기"):
    st.write("이곳에 추가 정보를 넣을 수 있습니다.")

# 데이터프레임 표시
df = pd.DataFrame({
    "이름": ["홍길동", "김철수", "이영희"],
    "나이": [25, 30, 22],
    "국가": ["한국", "미국", "일본"]
})
st.dataframe(df)  # 데이터프레임 테이블 표시

# 차트 예시 (라인차트)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)  # 라인 차트

# 차트 예시 (바차트)
st.bar_chart(chart_data)  # 바 차트

# 차트 예시 (맵)
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.5665, 126.9780],  # 서울 근처 좌표
    columns=['lat', 'lon']
)
st.map(map_data)  # 지도에 데이터 표시

# 이미지 표시
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 외부 이미지 표시

# 코드 블록 표시
st.code("""
def hello():
    print("Hello, Streamlit!")
""", language='python')  # 코드 블록

# 경고, 정보, 에러 메시지
st.warning("이것은 경고 메시지입니다.")  # 경고 메시지
st.info("이것은 정보 메시지입니다.")  # 정보 메시지
st.error("이것은 에러 메시지입니다.")  # 에러 메시지

# 프로그레스 바
progress_bar = st.progress(0)
for percent_complete in range(1, 101):
    time.sleep(0.01)
    progress_bar.progress(percent_complete)

# 스피너
with st.spinner("잠시만 기다려주세요..."):
    time.sleep(1)

# 성공 메시지
st.success("모든 예시가 정상적으로 표시되었습니다!")  # 성공 메시지

# 각 요소에 대한 설명은 각주로 코드에 달려