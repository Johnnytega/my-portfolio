import streamlit as st
from PIL import Image
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tech Profile", page_icon="🛡️", layout="wide")

# --- HEADER ---
st.title("🛡️ Cybersecurity Analyst & Python Dev")

# --- DIGITAL CARD SHOWCASE ---
import os

col_card1, col_card2 = st.columns(2)
with col_card1:
    if os.path.exists("CARD_FRONT.png"):
        st.image("CARD_FRONT.png", caption="Digital Identity (Front)")
with col_card2:
    if os.path.exists("CARD_BACK.png"):
        st.image("CARD_BACK.png", caption="Scan to Connect")

st.markdown("*Securing Systems | Automating Solutions | Analyzing Data*")
st.write("---")

# --- 2 COLUMN LAYOUT FOR SKILLS ---
col_left, col_right = st.columns([1, 2])

with col_left:
    # --- SKILLS SECTION ---
    st.header("🛠️ Technical Arsenal")

    st.write("**Python & Automation**")
    st.progress(90)

    st.write("**Network Security (Nmap/Wireshark)**")
    st.progress(85)

    st.write("**Cryptography & Linux**")
    st.progress(80)

    st.write("**Web Exploitation (Burp Suite)**")
    st.progress(70)

    st.write("---")
    st.subheader("🎓 Education")
    st.write("B.Sc. Cybersecurity")
    st.caption("Bingham University (In Progress)")

with col_right:
    # --- LIVE PROJECT: GHOST WRITER ---
    st.header("👻 Project: Ghost Writer (Steganography)")
    st.info("A tool to hide secret messages inside image pixels (LSB Encoding). Ideal for covert communication.")


    # Steganography Logic (The Brain)
    def text_to_bin(data):
        """Convert text to binary."""
        return [format(ord(i), '08b') for i in data]


    def modify_pixels(pixels, data):
        """Embed binary data into pixel values."""
        data_list = text_to_bin(data)
        len_data = len(data_list)
        imdata = iter(pixels)

        for i in range(len_data):
            pixels = [value for value in next(imdata)[:3] +
                      next(imdata)[:3] +
                      next(imdata)[:3]]

            # Pixel 1-8 logic (Simplified LSB)
            for j in range(0, 8):
                if (data_list[i][j] == '0') and (pixels[j] % 2 != 0):
                    pixels[j] -= 1
                elif (data_list[i][j] == '1') and (pixels[j] % 2 == 0):
                    if pixels[j] != 0:
                        pixels[j] -= 1
                    else:
                        pixels[j] += 1

            # Marker to keep reading
            if (i == len_data - 1):
                if (pixels[-1] % 2 == 0):
                    if pixels[-1] != 0:
                        pixels[-1] -= 1
                    else:
                        pixels[-1] += 1
            else:
                if (pixels[-1] % 2 != 0):
                    pixels[-1] -= 1

            pixels = tuple(pixels)
            yield pixels[0:3]
            yield pixels[3:6]
            yield pixels[6:9]


    def encode_enc(newimg, data):
        """Driver function to encode data."""
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in modify_pixels(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1
        return newimg


    def decode_dec(image):
        """Driver function to decode data."""
        data = ''
        imgdata = iter(image.getdata())

        while (True):
            pixels = [value for value in next(imgdata)[:3] +
                      next(imgdata)[:3] +
                      next(imgdata)[:3]]
            binstr = ''

            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data


    # UI Controls
    tab1, tab2 = st.tabs(["🔒 Encode (Hide)", "🔓 Decode (Reveal)"])

    with tab1:
        st.write("Upload an image and type a secret message.")
        uploaded_file = st.file_uploader("Choose an Image (PNG/JPG)", type=["png", "jpg", "jpeg"])
        secret_text = st.text_input("Enter Secret Message:")

        if uploaded_file and secret_text:
            if st.button("Hide Message"):
                image = Image.open(uploaded_file)
                new_image = image.copy()
                try:
                    # Run Encoding
                    encoded_image = encode_enc(new_image, secret_text)

                    # Save to memory buffer
                    buf = io.BytesIO()
                    encoded_image.save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    st.success("✅ Message Hidden Successfully!")
                    st.image(encoded_image, caption="Steganographic Image (Looks identical!)")

                    st.download_button(
                        label="⬇️ Download Secret Image",
                        data=byte_im,
                        file_name="secret_image.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"Error: Image might be too small for this text. {e}")

    with tab2:
        st.write("Upload an image to check for hidden messages.")
        decode_file = st.file_uploader("Upload Secret Image", type=["png"])

        if decode_file:
            if st.button("Reveal Message"):
                try:
                    img = Image.open(decode_file)
                    hidden_text = decode_dec(img)
                    st.success(f"🔍 Found Message: {hidden_text}")
                except:
                    st.error("No hidden message found or image corrupted.")

# --- CONTACT CTA ---
st.write("---")
st.center = st.columns(1)
st.markdown(
    "<div style='text-align: center;'><a href='https://wa.me/2349132218713?text=Hi%20Tega%2C%20I%20saw%20your%20Ghost%20Writer%20tool.'>Chat on WhatsApp</a></div>",
    unsafe_allow_html=True)
