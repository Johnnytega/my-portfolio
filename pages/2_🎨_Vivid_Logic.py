import streamlit as st
import random
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vivid Logic Studio", page_icon="🎨", layout="wide")

# --- HEADER ---
st.markdown('<h1 style="text-align: center; color: #00F0FF;">VIVID LOGIC STUDIO</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center;">Where Code Meets Creativity</h3>', unsafe_allow_html=True)
st.write("---")

# --- DIGITAL CARD SHOWCASE ---
col_card1, col_card2 = st.columns(2)
with col_card1:
    if os.path.exists("CREATIVE_FRONT.png"):
        st.image("CREATIVE_FRONT.png", caption="Studio Identity (Front)")
with col_card2:
    if os.path.exists("CREATIVE_BACK.png"):
        st.image("CREATIVE_BACK.png", caption="Studio Identity (Back)")

st.write("---")

# --- NEW PROJECT: THE BRAND ALCHEMIST ---
st.header("✨ Project: The Brand Alchemist")
st.write("Stuck on a brand idea? Enter your business type, and my algorithm will generate a color palette and style guide for you.")

# Input
col1, col2 = st.columns(2)
with col1:
    brand_name = st.text_input("Brand Name", "Oceanic Tech")
with col2:
    industry = st.selectbox("Industry", ["Technology", "Food/Cafe", "Fashion", "Health/Wellness", "Corporate"])

if st.button("🔮 Generate Brand Identity"):
    st.subheader(f"Brand Identity for: {brand_name}")
    
    # Python Logic for Design (The "Brain")
    if industry == "Technology":
        primary = "#00F0FF" # Cyan
        secondary = "#1E1E1E" # Dark Grey
        accent = "#FFFFFF"
        font = "Roboto Mono / Orbitron"
        vibe = "Futuristic, Clean, Innovative"
    elif industry == "Food/Cafe":
        primary = "#6F4E37" # Coffee
        secondary = "#F5F5DC" # Beige
        accent = "#DAA520" # Gold
        font = "Playfair Display / Lora"
        vibe = "Cozy, Organic, Premium"
    elif industry == "Fashion":
        primary = "#FF007F" # Hot Pink
        secondary = "#000000" # Black
        accent = "#FFD700" # Gold
        font = "Bodoni / Montserrat"
        vibe = "Bold, Chic, Trendy"
    elif industry == "Health/Wellness":
        primary = "#2E8B57" # Sea Green
        secondary = "#F0FFF0" # Honeydew
        accent = "#87CEEB" # Sky Blue
        font = "Open Sans / Lato"
        vibe = "Calm, Trusted, Fresh"
    else: # Corporate
        primary = "#003366" # Navy
        secondary = "#B0C4DE" # Light Steel
        accent = "#C0C0C0" # Silver
        font = "Helvetica / Arial"
        vibe = "Professional, Serious, Stable"

    # Display the Result as a "Mood Board"
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f"**Primary Color**")
        st.color_picker("Main", primary, disabled=True)
        st.code(primary)
    
    with c2:
        st.markdown(f"**Secondary Color**")
        st.color_picker("Sub", secondary, disabled=True)
        st.code(secondary)
        
    with c3:
        st.markdown(f"**Accent Color**")
        st.color_picker("Pop", accent, disabled=True)
        st.code(accent)

    st.info(f"📝 **Recommended Font Pairing:** {font}")
    st.success(f"⚡ **Brand Vibe:** {vibe}")

st.write("---")

# --- PORTFOLIO SHOWCASE ---
st.header("📂 Visual Gallery")

tab1, tab2 = st.tabs(["🖼️ Graphic Design", "🤖 AI Generated Textures"])

with tab1:
    st.write("A selection of brand systems and logos.")
    # If you have other images, add them here. For now, we reuse the cards as a placeholder.
    if os.path.exists("CREATIVE_FRONT.png"):
        st.image("CREATIVE_FRONT.png", width=300)

with tab2:
    st.write("High-resolution assets generated via prompt engineering.")
    if os.path.exists("bg_creative.jpg"):
        st.image("bg_creative.jpg", caption="Holographic Texture 01")

# --- SERVICES ---
st.write("---")
st.markdown("### Ready to create something vivid?")
st.markdown("[**Start a Project on WhatsApp**](https://wa.me/2349132218713?text=Hi%20Vivid%20Logic%2C%20I%20loved%20the%20Brand%20Alchemist%20demo.)")
