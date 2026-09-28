import streamlit as st
import secrets
import time

# Page configuration
st.set_page_config(
    page_title="OTP Generator",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 OTP Generator")
st.write("Generate and verify a secure 6-digit OTP.")

# Initialize session state
if "otp" not in st.session_state:
    st.session_state.otp = None

if "otp_time" not in st.session_state:
    st.session_state.otp_time = None

# OTP validity time
OTP_VALIDITY = 5 * 60  # 5 minutes


# Generate OTP function
def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


# Generate OTP button
if st.button("🔄 Generate OTP", use_container_width=True):

    st.session_state.otp = generate_otp()
    st.session_state.otp_time = time.time()

    st.success("OTP generated successfully!")


# Display OTP and verification section
if st.session_state.otp:

    # Calculate remaining time
    elapsed_time = time.time() - st.session_state.otp_time
    remaining_time = OTP_VALIDITY - elapsed_time

    if remaining_time > 0:

        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)

        st.info(
            f"🔑 Your OTP is: **{st.session_state.otp}**"
        )

        st.warning(
            f"⏳ OTP expires in: **{minutes:02d}:{seconds:02d}**"
        )

        st.divider()

        # OTP input
        user_otp = st.text_input(
            "Enter OTP",
            placeholder="Enter 6-digit OTP",
            max_chars=6
        )

        # Verify OTP
        if st.button("✅ Verify OTP", use_container_width=True):

            if not user_otp:
                st.warning("Please enter the OTP.")

            elif user_otp == st.session_state.otp:
                st.success("🎉 OTP Verified Successfully!")

            else:
                st.error("❌ Invalid OTP. Please try again.")

    else:
        st.error("⏰ OTP has expired. Please generate a new OTP.")

        if st.button("🔄 Generate New OTP", use_container_width=True):
            st.session_state.otp = generate_otp()
            st.session_state.otp_time = time.time()
            st.rerun()