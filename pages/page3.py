import streamlit as st
import numpy as np

st.title("주사위 실험기")

# 1. 주사위 개수 슬라이더 (최대 200개)
dice_num = st.slider("주사위 개수 선택", min_value=1, max_value=200, value=10)

# 2. 주사위 굴리기 버튼
if st.button("주사위 굴리기"):
    # 주사위 굴리기 (1~6 사이의 정수 난수 생성)
    results = np.random.randint(1, 7, size=dice_num)
    avg = np.mean(results)
    st.write(f"주사위 결과: {results}")
    st.success(f"주사위 평균: {avg:.2f}")
else:
    st.info("주사위 개수를 선택하고 '주사위 굴리기' 버튼을 눌러주세요.")