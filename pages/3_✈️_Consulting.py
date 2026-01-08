import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Consulting Services", page_icon="✈️", layout="centered")

# --- HEADER ---
st.title("✈️ Global Consulting & Support")
st.info("Expert guidance for Travel Logistics, Visa Applications, and Personal Finance.")

# --- DIGITAL CARD SHOWCASE ---
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("CONSULT_FRONT.png"):
        st.image("CONSULT_FRONT.png", use_container_width=True, caption="Professional Consultant")
with col2:
    if os.path.exists("CONSULT_BACK.png"):
        st.image("CONSULT_BACK.png", use_container_width=True, caption="Service Menu & Scan")

st.write("---")

# --- PROJECT: DUAL MARKET WATCH ---
st.header("📈 Market Pulse: Global & Local")
st.write("I help clients diversify portfolios across both US Growth Stocks and Nigerian Blue Chips.")

# TAB 1: US MARKETS (The "Tech Bro" Stuff)
st.subheader("🇺🇸 US Market (Growth)")
col_us1, col_us2, col_us3 = st.columns(3)
with col_us1:
    st.metric(label="Apple (AAPL)", value="$185.60", delta="+1.2%")
with col_us2:
    st.metric(label="NVIDIA (NVDA)", value="$720.15", delta="+3.5%")
with col_us3:
    st.metric(label="Tesla (TSLA)", value="$190.05", delta="-0.8%")

st.write("") # Spacer

# TAB 2: NIGERIAN MARKETS (The "Boomer" Stuff)
st.subheader("🇳🇬 NGX Lagos (Stability)")
col_ng1, col_ng2, col_ng3 = st.columns(3)
with col_ng1:
    # Dangote is King for local investors
    st.metric(label="Dangote Cem", value="₦650.00", delta="+0.5%")
with col_ng2:
    # MTN is the steady tech giant
    st.metric(label="MTN Nigeria", value="₦220.50", delta="-0.2%")
with col_ng3:
    # GTCO is the reliable bank
    st.metric(label="GTCO", value="₦38.90", delta="+1.1%")

with st.expander("📊 Consultant's Note (Read More)"):
    st.write("""
    * **For Growth:** US Tech stocks offer high returns but higher volatility.
    * **For Stability:** Nigerian Blue Chips (Dangote, MTN) offer steady dividends.
    * **Strategy:** I recommend a 70/30 split depending on your risk tolerance.
    """)

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

# --- BOOKING FORM ---
st.header("📅 Book a Consultation")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name")
with col2:
    service = st.selectbox("Service Needed", ["Visa Assistance", "Stock/Crypto Setup", "IT Support", "Other"])

message = st.text_area("Briefly describe your issue")

if st.button("Request Appointment"):
    if name and message:
        import urllib.parse
        base_url = "https://wa.me/2349132218713?text="
        msg_text = f"Hi Tega, I am {name}. I need help with {service}. Details: {message}"
        final_link = base_url + urllib.parse.quote(msg_text)
        
        st.success("Request Generated! Click below to send:")
        st.markdown(f"### 👉 [**Click here to Open WhatsApp**]({final_link})")
    else:
        st.error("Please enter your name and a short message.")
