import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vivid Logic Studio", page_icon="🎨", layout="wide")

# --- CUSTOM CSS FOR CREATIVE VIBE ---
st.markdown("""
<style>
    .brand-title {font-size: 50px; font-weight: 800; background: -webkit-linear-gradient(45deg, #00F0FF, #FF00FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .service-card {background-color: #222; padding: 20px; border-radius: 15px; border: 1px solid #444;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="brand-title">VIVID LOGIC STUDIO</div>', unsafe_allow_html=True)
st.write("### *Where Code Meets Creativity*")
st.write("Specializing in AI-Generated Art, High-End Branding, and Motion Graphics.")
st.write("---")

# --- PORTFOLIO SHOWCASE ---
st.header("📂 Featured Work")

# Create Tabs for different categories
tab1, tab2, tab3 = st.tabs(["🖼️ Graphic Design", "🤖 AI Art Generation", "🎬 Video Editing"])

with tab1:
    st.subheader("Brand Identity System")
    st.write("A complete digital identity system designed for a modern creative agency.")

    # We display the cards you just made!
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("CREATIVE_FRONT.png"):
            st.image("CREATIVE_FRONT.png", caption="Brand Identity (Front)")
        else:
            st.info("⚠️ Run your card generator script to see the image here!")

    with col2:
        if os.path.exists("CREATIVE_BACK.png"):
            st.image("CREATIVE_BACK.png", caption="Brand Identity (Back)")
        else:
            st.info("⚠️ Image not found.")

with tab2:
    st.subheader("Generative AI Assets")
    st.write("Custom prompt engineering for high-resolution textures and assets.")

    # Display the background you generated
    if os.path.exists("bg_creative.jpg"):
        st.image("bg_creative.jpg", caption="Holographic Abstract Texture (AI Generated)")
    else:
        st.info("⚠️ Place 'bg_creative.jpg' in your folder to see it here.")

with tab3:
    st.subheader("Motion Graphics & Editing")
    st.info("🎥 Video Portfolio coming soon. (This is where you will embed YouTube/Vimeo links later!)")

st.write("---")

# --- SERVICE PACKAGES ---
st.header("✨ Services & Pricing")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("### 🔹 The Starter")
    st.write("**₦15,000 - ₦30,000**")
    st.write("- Basic Logo Design")
    st.write("- 2 Social Media Flyers")
    st.write("- 3 Revisions")
    st.button("Order Starter", key="btn1")

with col_b:
    st.markdown("### 💎 The Professional")
    st.write("**₦50,000 - ₦80,000**")
    st.write("- Full Brand Identity (Logo, Cards, Letterhead)")
    st.write("- 5 Social Media Assets")
    st.write("- AI Art Assets")
    st.button("Order Professional", key="btn2")

with col_c:
    st.markdown("### 🚀 The Agency")
    st.write("**Custom Pricing**")
    st.write("- Video Editing & Motion Graphics")
    st.write("- Full Campaign Strategy")
    st.write("- Priority Support")
    st.button("Contact for Quote", key="btn3")

# --- INSTANT CONTACT ---
st.write("---")
st.markdown("### Ready to create something vivid?")
st.markdown(
    "[**Chat on WhatsApp**](https://wa.me/2349132218713?text=Hi%20Vivid%20Logic%2C%20I%20want%20to%20discuss%20a%20design%20project.)")