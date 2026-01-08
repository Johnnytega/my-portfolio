import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Consulting Services", page_icon="✈️", layout="centered")

# --- HEADER ---
st.title("✈️ Global Consulting & Support")
st.info("Expert guidance for Travel Logistics, Visa Applications, and Personal Tech.")

# --- DIGITAL CARD SHOWCASE ---
import os
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("CONSULT_FRONT.png"):
        st.image("CONSULT_FRONT.png", use_container_width=True, caption="Professional Consultant")
with col2:
    if os.path.exists("CONSULT_BACK.png"):
        st.image("CONSULT_BACK.png", use_container_width=True, caption="Service Menu & Scan")

st.write("---")

# --- SERVICES ACCORDION ---
st.header("How Can I Help You?")

with st.expander("🌍 Visa & Travel Assistance", expanded=True):
    st.write("""
    Navigating visa websites can be frustrating. I handle the technical side for you.
    * **US/UK/Canada Visa Appointment Booking**
    * **Form DS-160 Filling & Review**
    * **Application Tracking & Error Fixing**
    """)

with st.expander("💻 Personal IT & Crypto Support"):
    st.write("""
    Secure your digital assets and fix hardware issues.
    * **Crypto Wallet Setup (Bamboo, Binance, TrustWallet)**
    * **Laptop Troubleshooting (Blue Screen, Slow Performance)**
    * **Software Installation & Updates**
    """)

with st.expander("🎓 Study Abroad Logistics"):
    st.write("""
    * **School Search & Application Support**
    * **Document Organization**
    """)

st.write("---")

# --- BOOKING FORM ---
st.header("📅 Book a Consultation")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name")
with col2:
    service = st.selectbox("Service Needed", ["Visa Assistance", "IT Support", "Crypto Setup", "Other"])

message = st.text_area("Briefly describe your issue")

if st.button("Request Appointment"):
    if name and message:
        # This creates a custom WhatsApp link with their message!
        import urllib.parse

        base_url = "https://wa.me/2349132218713?text="
        msg_text = f"Hi Tega, I am {name}. I need help with {service}. Details: {message}"
        final_link = base_url + urllib.parse.quote(msg_text)

        st.success("Request Generated! Click below to send:")
        st.markdown(f"### 👉 [**Click here to Open WhatsApp**]({final_link})")
    else:
        st.error("Please enter your name and a short message.")