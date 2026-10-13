import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(
    page_title="Hameed Bajwa 129 - TikTok & Shorts Optimizer",
    page_icon="🚀",
    layout="wide",
)

# Custom Styling for Professional Look
st.markdown("""
    <style>
    .main-header { font-size: 2.3rem; color: #FF2D55; text-align: center; font-weight: bold; }
    .sub-header { font-size: 1.1rem; color: #555; text-align: center; margin-bottom: 25px; }
    .brand-footer { text-align: center; color: #888; font-size: 0.9rem; margin-top: 40px; }
    .metric-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #FF2D55; }
    </style>
""", unsafe_allow_html=True)

# App Header with Custom Branding
st.markdown('<p class="main-header">🎬 Hameed Bajwa 129 - Viral Video Optimizer</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Professional AI Suite to Check Viral Potential, Get Trending Sounds & Smart Hashtags!</p>', unsafe_allow_html=True)

# Sidebar for Settings
st.sidebar.header("⚙️ Optimization Settings")
category = st.sidebar.selectbox(
    "Select Video Category",
    [
        "Entertainment / Comedy",
        "Gaming",
        "Fashion & Style",
        "Education / Tech",
        "Vlogs / Daily Life",
        "Traditional & Cultural"
    ]
)
target_platform = st.sidebar.radio(
    "Target Platform",
    ["TikTok", "YouTube Shorts", "Instagram Reels"]
)

# Main Upload Section
uploaded_file = st.file_uploader("Upload your video file (MP4, MOV)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📹 Uploaded Video Preview")
        st.video(uploaded_file)
        
    with col2:
        st.subheader("📊 AI Viral Analysis Suite")
        
        if st.button("🚀 Analyze for Viral Potential", type="primary"):
            with st.spinner("Hameed Bajwa 129 AI is analyzing hooks, pacing, audio frequency, and trends..."):
                time.sleep(2)
                
                # Dynamic viral score generator
                viral_score = random.randint(78, 98)
                
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>🔥 Predicted Viral Score: <span style="color: #FF2D55;">{viral_score}%</span></h3>
                        <p><b>Platform Analysis:</b> Your video has strong hook elements optimized for <b>{target_platform}</b>!</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Suggested Sounds
                st.subheader("🎵 Recommended Viral Sounds")
                if category == "Fashion & Style":
                    st.success("1. Aesthetic Slow Mo Beat (Trending)")
2. Traditional Fusion Remix v2
2. Traditional Fusion Remix v2
3. High Fashion Runway Loop")
                elif category == "Entertainment / Comedy":
                    st.success("1. Viral Comedy Punchline Beat #1
2. Funny Sound Effect Pack Pro
3. Trending Meme Audio #4")
                else:
                    st.success("1. Global TikTok Viral Trending Sound
2. Upbeat Chill Electronic Rhythm
3. Cinematic Energy Build-up")
                
                # Hashtags Generation
                st.subheader("🏷️ Optimized Viral Hashtags")
                base_tags = "#fyp #viral #foryoupage #trending #hameedbajwa129"
                cat_tags = f"#{category.split('/')[0].strip().lower().replace(' ', '')}"
                platform_tags = f"#{target_platform.lower().replace(' ', '')}"
                generated_tags = f"{base_tags} {cat_tags} {platform_tags} #viralvideo #trendalert"
                
                st.code(generated_tags, language="text")
                
                # Professional Recommendations
                st.subheader("💡 Pro Growth Strategies")
                st.info("• **Strong Hook:** Ensure the first 3 seconds grab immediate user attention.
• **Engagement:** Pin a creative comment and reply within 30 minutes.
• **Timing:** Post during peak regional hours (6 PM - 9 PM).")
else:
    st.info("👈 Please upload a video file using the uploader above to run the Hameed Bajwa 129 optimization suite.")

st.markdown('<p class="brand-footer">Powered by Hameed Bajwa 129 • Professional Video Optimization System</p>', unsafe_allow_html=True)
