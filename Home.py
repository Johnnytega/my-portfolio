import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Tega Johnny | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS (Responsive & Tech Vibe) ---
# This checks screen size. If mobile, it shrinks the text to fit.
st.markdown("""
<style>
    /* Desktop Style (Big & Spaced Out) */
    .main-header {
        font-size: 60px; 
        font-weight: 700; 
        color: #ffffff; 
        text-align: center; 
        letter-spacing: 15px; 
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    
    .sub-header {
        font-size: 20px; 
        color: #00F0FF; 
        text-align: center; 
        letter-spacing: 2px;
        margin-bottom: 40px;
    }

    .card {
        background-color: #1E1E1E; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #333; 
        text-align: center;
    }
    .card:hover {
        border-color: #00F0FF; 
        box-shadow: 0 0 10px #00F0FF;
    }

    /* Mobile Style (Screen narrower than 600px) */
    @media (max-width: 600px) {
        .main-header {
            font-size: 30px; /* Smaller font to fit phone screen */
            letter-spacing: 3px; /* Tighter spacing so words don't break */
        }
        .sub-header {
            font-size: 16px;
            margin-bottom: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
# Notice: No manual spaces (&nbsp;). The CSS handles the layout now.
st.markdown('<div class="main-header">Tega Johnny</div>', unsafe_allow_html=True)
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
    <div style='text-align: center; color: grey; padding-top: 20px;'>
        © 2026 Tega Johnny • Built with Python & Streamlit
    </div>
    """, 
    unsafe_allow_html=True
)
