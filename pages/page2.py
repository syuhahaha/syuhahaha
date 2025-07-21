import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV 데이터 시각화 페이지")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.subheader("업로드된 데이터 미리보기")
    st.dataframe(df)  # 데이터 미리보기

    # 컬럼 선택 (수치형만 자동 필터)
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X축 컬럼 선택", numeric_cols)
        y_col = st.selectbox("Y축 컬럼 선택", numeric_cols, index=1)

        # 선택된 컬럼으로 시각화
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{x_col} vs {y_col} 산점도")
        st.pyplot(fig)
    else:
        st.warning("시각화를 위해 2개 이상의 수치형 컬럼이 필요합니다.")
else:
    st.info("CSV 파일을 업로드하면 데이터와 시각화가 표시됩니다.")

# 각 기능별로 주석이 달려 있습니다.