import streamlit as st
from PIL import Image
import io
import pandas as pd # Required for the new dashboard
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Tech Profile", page_icon="🛡️", layout="wide")

# --- HEADER ---
st.title("🛡️ Cybersecurity Analyst & Python Dev")

# --- DIGITAL CARD SHOWCASE ---
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
    # --- PROJECT 1: GHOST WRITER ---
    st.header("👻 Project: Ghost Writer (Steganography)")
    st.info("A tool to hide secret messages inside image pixels (LSB Encoding). Ideal for covert communication.")

    # Steganography Logic
    def text_to_bin(data):
        return [format(ord(i), '08b') for i in data]

    def modify_pixels(pixels, data):
        data_list = text_to_bin(data)
        len_data = len(data_list)
        imdata = iter(pixels)
        for i in range(len_data):
            pixels = [value for value in next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3]]
            for j in range(0, 8):
                if (data_list[i][j] == '0') and (pixels[j] % 2 != 0): pixels[j] -= 1
                elif (data_list[i][j] == '1') and (pixels[j] % 2 == 0):
                    if pixels[j] != 0: pixels[j] -= 1
                    else: pixels[j] += 1
            if (i == len_data - 1):
                if (pixels[-1] % 2 == 0):
                    if pixels[-1] != 0: pixels[-1] -= 1
                    else: pixels[-1] += 1
            else:
                if (pixels[-1] % 2 != 0): pixels[-1] -= 1
            pixels = tuple(pixels)
            yield pixels[0:3]
            yield pixels[3:6]
            yield pixels[6:9]

    def encode_enc(newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)
        for pixel in modify_pixels(newimg.getdata(), data):
            newimg.putpixel((x, y), pixel)
            if (x == w - 1): x = 0; y += 1
            else: x += 1
        return newimg

    def decode_dec(image):
        data = ''
        imgdata = iter(image.getdata())
        while (True):
            pixels = [value for value in next(imgdata)[:3] + next(imgdata)[:3] + next(imgdata)[:3]]
            binstr = ''
            for i in pixels[:8]:
                if (i % 2 == 0): binstr += '0'
                else: binstr += '1'
            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0): return data

    # UI Controls
    tab1, tab2 = st.tabs(["🔒 Encode", "🔓 Decode"])
    with tab1:
        uploaded_file = st.file_uploader("Choose Image", type=["png", "jpg"], key="enc")
        secret_text = st.text_input("Message to Hide")
        if uploaded_file and secret_text and st.button("Hide Message"):
            img = Image.open(uploaded_file)
            new_img = encode_enc(img.copy(), secret_text)
            buf = io.BytesIO()
            new_img.save(buf, format="PNG")
            st.download_button("Download Image", buf.getvalue(), "secret.png", "image/png")
    with tab2:
        decode_file = st.file_uploader("Upload Image", type=["png"], key="dec")
        if decode_file and st.button("Reveal"):
            try: st.success(f"Found: {decode_dec(Image.open(decode_file))}")
            except: st.error("No message found.")

    # --- PROJECT 2: NETWORK MONITOR ---
    st.write("---")
    st.header("📡 Live Network Intrusion Monitor")
    st.write("Real-time log analysis of local network traffic. (Requires backend script running).")

    try:
        # Check for the log file
        if os.path.exists("network_log.csv"):
            df = pd.read_csv("network_log.csv")
            # Sort by latest
            df = df.sort_values(by="Timestamp", ascending=False).head(10)
            
            # Flashy Table
            st.dataframe(
                df, 
                column_config={
                    "Status": st.column_config.TextColumn("Threat Level", validate="^(SAFE|SUSPICIOUS|ACTIVE)$"),
                },
                use_container_width=True
            )
            
            # Metrics
            col_n1, col_n2 = st.columns(2)
            with col_n1:
                suspicious = len(df[df['Status'] == 'SUSPICIOUS'])
                st.metric("Suspicious Packets", suspicious, delta="Alert" if suspicious > 0 else "None")
            with col_n2:
                active_dev = df['IP Address'].nunique()
                st.metric("Active Devices", active_dev)
                
            if st.button("🔄 Refresh Logs"):
                st.rerun()
        else:
            st.warning("⚠️ Backend Monitor is offline. Run 'scanner.py' locally to capture traffic.")
            
    except Exception as e:
        st.error(f"Error loading logs: {e}")

# --- CONTACT CTA ---
st.write("---")
st.markdown("<div style='text-align: center;'><a href='https://wa.me/2349132218713'>Chat on WhatsApp</a></div>", unsafe_allow_html=True)
