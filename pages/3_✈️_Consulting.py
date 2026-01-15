import streamlit as st
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Consulting", page_icon="✈️", layout="wide")

# --- HEADER ---
st.title("✈️ Global Strategy & Visa Consulting")
st.markdown("*Bridging the gap between Nigeria and the World.*")
st.write("---")

# --- SECTION 1: MARKET PULSE (LAGOS vs NEW YORK) ---
st.header("📈 Market Pulse: Lagos vs. New York")
st.write("Real-time tracking of key assets for international clients.")

col1, col2, col3, col4 = st.columns(4)

# SIMULATED DATA (Replace with API later)
usd_ngn = 1650 + random.randint(-5, 5)
btc_price = 98000 + random.randint(-200, 200)
dangote = 240 + random.randint(-2, 2)
nvidia = 145 + random.randint(-1, 1)

with col1:
    st.metric(label="🇺🇸 USD/NGN (Black Market)", value=f"₦{usd_ngn}", delta="-0.5%")
with col2:
    st.metric(label="🌍 BTC/USD", value=f"${btc_price:,}", delta="+1.2%")
with col3:
    st.metric(label="🇳🇬 Dangote Cement", value=f"₦{dangote}", delta="0%")
with col4:
    st.metric(label="🇺🇸 NVIDIA Corp", value=f"${nvidia}", delta="+0.8%")

if st.button("🔄 Refresh Rates"):
    st.rerun()

st.write("---")

# --- SECTION 2: THE VISA AUTOMATION BOT (NEW) ---
# This is the section that was missing!
col_v1, col_v2 = st.columns([3, 1])
with col_v1:
    st.header("🤖 Visa Automation Bot")
    st.write("I build custom automation scripts to secure appointment slots. This bot monitors scheduling portals 24/7, detecting openings instantly.")
    st.caption("Tech Stack: Python, Selenium, Webdriver Manager")
with col_v2:
    st.write("") # Spacer to align button
    st.write("") 
    # This button links to your new repo
    st.markdown("[![GitHub](https://img.shields.io/badge/View%20Code-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/Johnnytega/visa-scheduler-bot)")

st.info("⚠️ **Note:** This tool reduces wait times by 90% by automatically detecting open slots.")

st.write("---")

# --- SECTION 3: SERVICES ---
st.header("💼 How Can I Help You?")

with st.expander("Travel & Visa Assistance"):
    st.write("• US/Canada Visa Application Support")
    st.write("• Appointment Scheduling Automation")
    st.write("• Flight Booking & Itinerary Planning")

with st.expander("Business Advisory"):
    st.write("• Business Registration (CAC)")
    st.write("• Market Entry Strategy (Nigeria)")
    st.write("• Tech Stack Consultation for Startups")

# --- CALL TO ACTION ---
st.write("---")
st.markdown("### Ready to move?")
st.markdown("[**Book a Consultation on WhatsApp**](https://wa.me/2349132218713?text=Hi%20Johnny%2C%20I%20saw%20your%20consulting%20dashboard.)")

