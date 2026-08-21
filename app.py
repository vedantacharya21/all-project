import streamlit as st
import qrcode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image
from io import BytesIO

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="centered"
)

# -----------------------------
# Function to Generate QR Code
# -----------------------------
def generate_qr(data, box_size, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=box_size,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    ).convert("RGB")

    return img


# -----------------------------
# UI
# -----------------------------
st.title("🔳 QR Code Generator")
st.write("Generate QR Codes from Text or URLs.")

data = st.text_area(
    "Enter Text or URL",
    placeholder="https://example.com"
)

filename = st.text_input(
    "File Name",
    value="qr_code"
)

box_size = st.slider(
    "QR Size",
    min_value=5,
    max_value=20,
    value=10
)

fill_color = st.color_picker(
    "QR Color",
    "#000000"
)

back_color = st.color_picker(
    "Background Color",
    "#FFFFFF"
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate QR Code", use_container_width=True):

    if data.strip() == "":
        st.warning("Please enter some text or a URL.")

    else:
        try:
            img = generate_qr(
                data,
                box_size,
                fill_color,
                back_color
            )

            st.success("QR Code Generated Successfully!")

            st.image(
                img,
                caption="Generated QR Code",
                use_container_width=True
            )

            # Save image in memory
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Download Button
            st.download_button(
                label="📥 Download QR Code",
                data=buffer.getvalue(),
                file_name=f"{filename}.png",
                mime="image/png",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error: {e}")