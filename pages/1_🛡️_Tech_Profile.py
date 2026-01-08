import streamlit as st

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

# --- 2 COLUMN LAYOUT ---
col_left, col_right = st.columns([1, 2])

with col_left:
    # --- SKILLS SECTION (The "Arsenal") ---
    st.header("🛠️ Technical Arsenal")

    st.write("**Python & Automation**")
    st.progress(90)  # 90% Bar

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
    # --- LIVE PROJECT DEMO ---
    st.header("💻 Live Code Demo: Secure Hash Generator")
    st.write("I don't just talk about code; I write it. Try this tool I built right now:")

    # A simple Interactive Tool
    import hashlib

    user_input = st.text_input("Enter text to hash (e.g., a password):", type="password")
    hash_type = st.selectbox("Select Hash Algorithm:", ["SHA-256", "MD5", "SHA-512"])

    if user_input:
        if hash_type == "SHA-256":
            result = hashlib.sha256(user_input.encode()).hexdigest()
        elif hash_type == "MD5":
            result = hashlib.md5(user_input.encode()).hexdigest()
        elif hash_type == "SHA-512":
            result = hashlib.sha512(user_input.encode()).hexdigest()

        st.code(f"{hash_type} Hash:\n{result}", language="bash")
        st.success("✅ Hash Generated Successfully")
    else:
        st.info("Enter text above to see the cryptographic hash.")

    st.write("---")

    # --- PROJECT LIST ---
    st.subheader("📂 Key Projects")

    with st.expander("BadUSB Payload Script (DuckyScript)"):
        st.write("Developed custom scripts for HID attacks to test physical security perimeters.")
        st.markdown("[View on GitHub](https://github.com/Johnnytega)")

    with st.expander("Automated Network Scanner (Python)"):
        st.write("Built a Python tool using Scapy to map local networks and identify open ports.")
        st.markdown("[View on GitHub](https://github.com/Johnnytega)")

# --- CONTACT CTA ---
st.write("---")
st.center = st.columns(1)
st.markdown("<h3 style='text-align: center;'>Need a Secure System?</h3>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center;'><a href='https://wa.me/2349132218713?text=Hi%20Tega%2C%20I%20saw%20your%20Tech%20Profile.'>Chat on WhatsApp</a></div>",
    unsafe_allow_html=True)