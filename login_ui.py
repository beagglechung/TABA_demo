import streamlit as st

def login(username, password):
    saved_username = "admin"
    saved_password = "1234"

    if username == saved_username and password == saved_password:
        return True
    else:
        return False

def main():
    st.title("로그인 페이지")

    input_username = st.text_input("아이디를 입력하세요")
    input_password = st.text_input("비밀번호를 입력하세요", type="password")

    if st.button("로그인"):
        if login(input_username, input_password):
            st.success("로그인 성공!")
        else:
            st.error("로그인 실패. 아이디 또는 비밀번호가 다릅니다.")

if __name__ == "__main__":
    main()
