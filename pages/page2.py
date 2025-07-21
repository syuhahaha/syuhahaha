import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("학생 성적 데이터 시각화")  # 페이지 제목

# 예시 데이터 (이미지의 CSV 내용)
data = {
    "이름": ["홍길동", "김영희", "이철수", "박민수", "최지은"],
    "수학": [85, 90, 70, 95, 60],
    "영어": [78, 88, 65, 92, 72],
    "과학": [92, 84, 75, 89, 68]
}
df = pd.DataFrame(data)

st.subheader("학생별 성적 데이터")
st.dataframe(df)  # 데이터 미리보기

# 과목별 성적 막대그래프
st.subheader("학생별 과목 성적 막대그래프")
fig, ax = plt.subplots()
df.set_index("이름").plot(kind="bar", ax=ax)
ax.set_ylabel("점수")
ax.set_title("학생별 과목 성적")
st.pyplot(fig)

# 학생별 총점 산점도
st.subheader("학생별 총점 산점도")
df["총점"] = df[["수학", "영어", "과학"]].sum(axis=1)
fig2, ax2 = plt.subplots()
ax2.scatter(df["이름"], df["총점"], color='green')
ax2.set_xlabel("이름")
ax2.set_ylabel("총점")
ax2.set_title("학생별 총점 산점도")
st.pyplot(fig2)

# 각 기능별로 주석이 달려 있습니다.