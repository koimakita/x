import streamlit as st

# CSS for better styling
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #111;
}
.css-18e3th9 {
    padding: 10px;
    border-radius: 15px;
    background-color: #333;
}
.css-1cpxqw2 {
    margin: 20px 0px;
}
button.css-qbe2hs {
    background-color: #1DA1F2;
    color: #fff;
    border: none;
    border-radius: 20px;
    padding: 10px 20px;
    margin: 10px 0px;
}
</style>
""", unsafe_allow_html=True)

st.title('Twitter風SNSアプリ')

# Handling Tweet inputs and display
if 'tweets' not in st.session_state:
    st.session_state.tweets = []

tweet = st.text_input("何をつぶやく？", max_chars=280)
if st.button('ツイート'):
    if tweet:
        st.session_state.tweets.append(tweet)
        st.success("ツイートが投稿されました！")
    else:
        st.error("ツイートは空では投稿できません。")

st.subheader("タイムライン")
for t in reversed(st.session_state.tweets):
    st.markdown(f"<div style='background-color: #333; padding: 10px; border-radius: 15px;'>{t}</div>", unsafe_allow_html=True)
