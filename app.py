import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Rock Paper Scissor Game",
    page_icon="🎮",
    layout="centered"
)

# Title
st.title("🎮 Rock Paper Scissor Game")
st.write("Play Rock, Paper, Scissor against the computer!")

choices = ["Rock", "Paper", "Scissor"]

# User Choice
user_choice = st.selectbox(
    "Choose your move:",
    choices
)

# Play Button
if st.button("Play"):

    computer_choice = random.choice(choices)

    st.subheader("Results")
    st.write(f"🧑 You chose: **{user_choice}**")
    st.write(f"💻 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("🤝 Match Draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        st.success("🎉 You Win!")
    else:
        st.error("😢 Computer Wins!")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")