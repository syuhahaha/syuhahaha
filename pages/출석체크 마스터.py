import streamlit as st
import pandas as pd
import datetime

# -------------------- 초기 설정 --------------------
st.set_page_config(page_title="출결관리 앱", layout="wide")

if "records" not in st.session_state:
    st.session_state.records = []
if "submitted_numbers" not in st.session_state:
    st.session_state.submitted_numbers = []

# -------------------- 시간 기준 --------------------
cutoff_attend = datetime.time(7, 40)
cutoff_class_late = datetime.time(8, 0)
time_options = [datetime.time(7, m) for m in range(0, 60)] + \
               [datetime.time(8, m) for m in range(0, 11)]

# -------------------- 사용자 역할 선택 --------------------
st.sidebar.title("🎭 사용자 선택")
role = st.sidebar.radio("당신의 역할을 선택하세요", ["학생", "교사"])

# -------------------- 학생 화면 --------------------
if role == "학생":
    st.title("📘 학생 출결 체크")

    available_numbers = [i for i in range(1, 31) if i not in st.session_state.submitted_numbers]

    if available_numbers:
        student_number = st.selectbox("🧑 출석번호 선택", available_numbers)
        selected_time = st.selectbox("⏰ 시간 선택", time_options, format_func=lambda t: t.strftime("%H:%M"))

        st.write(f"선택된 시간: {selected_time.strftime('%H:%M:%S')}")

        if selected_time <= cutoff_attend:
            st.success("✅ 정상 출석입니다.")
            status = "정상 출석"
            task = None

        elif cutoff_attend < selected_time <= cutoff_class_late:
            st.warning("🕒 학급지각 (벌점 1점)")
            status = "학급지각"
            task = st.radio("청소 업무를 선택하세요", ["🗑️ 쓰레기통 비우기", "🧹 바닥쓸기", "🧼 바닥밀대"])

        else:
            st.error("🚫 학교지각입니다.")
            status = "학교지각"
            reason = st.radio("지각 사유 선택", ["미인정지각", "질병지각", "인정지각"])
            task = reason

            if reason == "미인정지각":
                st.write("❌ 벌점 2점 부과")

            elif reason == "질병지각":
                st.info("📄 질병 관련 서류를 제출해주세요.")
                try:
                    with open("01. 2025 질병 결석신고서.pdf", "rb") as f:
                        file_data = f.read()
                    st.download_button("📥 질병결석신고서 다운로드", data=file_data, file_name="질병결석신고서.pdf", mime="application/pdf")
                except:
                    st.warning("❗ 질병결석신고서 파일을 찾을 수 없습니다.")

                st.file_uploader("진료확인서를 업로드해주세요", type=["pdf", "jpg", "png"])

            elif reason == "인정지각":
                st.text_area("지각 사유를 작성해주세요")
                try:
                    with open("02-1. 2025 인정출결신고서_경조사_기타.pdf", "rb") as f:
                        file_data = f.read()
                    st.download_button("📥 인정출결신고서 다운로드", data=file_data, file_name="인정출결신고서_경조사_기타.pdf", mime="application/pdf")
                except:
                    st.warning("❗ 인정출결신고서 파일을 찾을 수 없습니다.")

                st.file_uploader("사유 증빙자료를 업로드해주세요", type=["pdf", "jpg", "png"])

        if st.button("제출하기"):
            st.session_state.records.append({
                "날짜": str(datetime.date.today()),
                "출석번호": student_number,
                "출결 상태": status,
                "선택 항목": task,
                "시간": selected_time.strftime('%H:%M:%S')
            })
            st.session_state.submitted_numbers.append(student_number)
            st.success(f"✅ 번호 {student_number} 출결 정보가 저장되었습니다.")
    else:
        st.warning("📌 오늘은 모든 학생이 출결을 제출했습니다.")

# -------------------- 교사 화면 --------------------
elif role == "교사":
    st.title("🧑‍🏫 교사용 관리 화면")

    # 교사 인증
    teacher_code = st.text_input("교사 인증코드를 입력하세요", type="password")
    if teacher_code != "ksms18944":
        st.warning("🚫 올바른 인증코드를 입력해야 교사용 화면이 열립니다.")
    else:
        df = pd.DataFrame(st.session_state.records)

        if not df.empty:
            st.subheader("📅 오늘 제출된 출결 현황")
            st.dataframe(df)

            late_df = df[df["출결 상태"] == "학교지각"]
            if not late_df.empty:
                st.subheader("🚨 8시 이후 지각자 명단")
                st.table(late_df)

            st.download_button("📥 출결기록 CSV 다운로드", data=df.to_csv(index=False), file_name="출결기록.csv")
        else:
            st.info("아직 출결 정보가 제출되지 않았습니다.")
