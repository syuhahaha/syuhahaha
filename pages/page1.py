import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm  # 폰트 매니저 추가

# 실제 존재하는 폰트 파일 경로로 수정
font_path = "./fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)

st.title("Matplotlib 데이터 시각화 예시")
st.markdown("아래는 커스텀 한글 폰트를 적용한 그래프 예시입니다.")

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선', color='blue')
ax.set_title('한글 제목: 사인 그래프', fontproperties=fontprop)
ax.set_xlabel('X축 (시간)', fontproperties=fontprop)
ax.set_ylabel('Y축 (진폭)', fontproperties=fontprop)
ax.legend(prop=fontprop)

st.pyplot(fig)
st.info("그래프의 제목, 축, 범례 모두 커스텀 한글 폰트로 표시됩니다.")