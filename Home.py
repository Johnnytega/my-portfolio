import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Tega Johnny | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS (For that Tech Vibe) ---
st.markdown("""
<style>
    .main-header {font-size: 60px; font-weight: 700; color: #ffffff; text-align: center; letter-spacing: 5px;}
    .sub-header {font-size: 25px; color: #00F0FF; text-align: center; margin-bottom: 50px;}
    .card {background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 1px solid #333; text-align: center;}
    .card:hover {border-color: #00F0FF; box-shadow: 0 0 10px #00F0FF;}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div class="main-header">T E G A &nbsp;&nbsp;&nbsp;&nbsp; J O H N N Y</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Multidisciplinary Tech Professional</div>', unsafe_allow_html=True)

st.write("---")

# --- THE SELECTOR DASHBOARD (3 Columns) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🛡️ Cybersecurity & Python")
    st.write("Specializing in Network Defense, Cryptography, and Python Automation.")
    if st.button("Go to Tech Profile"):
        st.switch_page("pages/1_🛡️_Tech_Profile.py")

with col2:
    st.success("🎨 Vivid Logic Studio")
    st.write("Digital Art, Brand Identity, and AI-Powered Visual Strategy.")
    if st.button("Visit Creative Studio"):
        st.switch_page("pages/2_🎨_Vivid_Logic.py")

with col3:
    st.warning("✈️ Global Consulting")
    st.write("Visa Logistics, Travel Support, and Tech Consultation Services.")
    if st.button("Consulting Services"):
        st.switch_page("pages/3_✈️_Consulting.py")

st.write("---")

# --- FOOTER ---
st.markdown(
    """
    <div style='text-align: center; color: grey;'>
        © 2026 Tega Johnny • Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)