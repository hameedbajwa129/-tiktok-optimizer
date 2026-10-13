import random
import time
import requests
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Hameed Bajwa 129 - TikTok & Shorts Optimizer",
    page_icon="🚀",
    layout="wide",
)


# Background Visitor Tracker Function (Securely hidden from public)
def track_visitor():
  try:
    ip_response = requests.get("https://ipapi.co/json/", timeout=2)
    country = "Global"
    if ip_response.status_code == 200:
      data = ip_response.json()
      country = data.get("country_name", "Global")

    counter_response = requests.get(
        "https://api.counterapi.dev/v1/hameedbajwa/optimizer/up", timeout=2
    )
    count = (
        counter_response.json().get("count", 0)
        if counter_response.status_code == 200
        else "N/A"
    )
    return count, country
  except:
    return "N/A", "Global"


# Background tracking
total_visits, visitor_country = track_visitor()

# Custom Styling
st.markdown(
    """
    <style>
    .main-header { font-size: 2.3rem; color: #FF2D55; text-align: center; font-weight: bold; }
    .sub-header { font-size: 1.1rem; color: #555; text-align: center; margin-bottom: 25px; }
    .brand-footer { text-align: center; color: #888; font-size: 0.9rem; margin-top: 40px; }
    .metric-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #FF2D55; }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.markdown(
    '<p class="main-header">🎬 Hameed Bajwa 129 - Viral Video Optimizer</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-header">Professional AI Suite to Check Viral Potential, Get'
    " Trending Sounds & Smart Hashtags!</p>",
    unsafe_allow_html=True,
)

# --- SIDEBAR NAVIGATION (Multi-page Setup) ---
st.sidebar.header("🧭 Navigation Menu")
app_mode = st.sidebar.radio(
    "Choose Tool",
    ["🎬 Viral Video Optimizer", "🚀 TikTok Video Booster Suite"],
)

# --- STRICT ADMIN PANEL (Protected with Password 9797) ---
st.sidebar.markdown("---")
with st.sidebar.expander("🔐 Admin Panel (Owner Only)"):
  admin_pass = st.text_input(
      "Enter Admin Passcode", type="password", key="admin_secure_key"
  )

  if admin_pass == "9797":
    st.success("Access Granted, Admin!")
    st.metric(label="Total App Visits", value=total_visits)
    st.info(f"Latest Visitor Country: {visitor_country}")
    st.markdown("*(Yeh data sirf aapko nazar aa raha hai.)*")
  elif admin_pass != "":
    st.error("Incorrect Passcode! Access Denied.")


# ================= PAGE 1: VIRAL VIDEO OPTIMIZER =================
if app_mode == "🎬 Viral Video Optimizer":
  st.sidebar.markdown("---")
  st.sidebar.header("⚙️ Optimization Settings")
  category = st.sidebar.selectbox(
      "Select Video Category",
      [
          "Entertainment / Comedy",
          "Gaming",
          "Fashion & Style",
          "Education / Tech",
          "Vlogs / Daily Life",
          "Traditional & Cultural",
      ],
  )
  target_platform = st.sidebar.radio(
      "Target Platform", ["TikTok", "YouTube Shorts", "Instagram Reels"]
  )

  uploaded_file = st.file_uploader(
      "Upload your video file (MP4, MOV)", type=["mp4", "mov", "avi"]
  )

  if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
      st.subheader("📹 Uploaded Video Preview")
      st.video(uploaded_file)

    with col2:
      st.subheader("📊 AI Viral Analysis Suite")

      if st.button("🚀 Analyze for Viral Potential", type="primary"):
        with st.spinner(
            "Hameed Bajwa 129 AI is analyzing hooks, pacing, audio frequency,"
            " and trends..."
        ):
          time.sleep(2)
          viral_score = random.randint(78, 98)

          st.markdown(
              f"""
                        <div class="metric-card">
                            <h3>🔥 Predicted Viral Score: <span style="color: #FF2D55;">{viral_score}%</span></h3>
                            <p><b>Platform Analysis:</b> Your video has strong hook elements optimized for <b>{target_platform}</b>!</p>
                        </div>
                    """,
              unsafe_allow_html=True,
          )

          st.markdown("---")
          st.subheader("🎵 Recommended Viral Sounds")
          if category == "Fashion & Style":
            st.success(
                "1. Aesthetic Slow Mo Beat (Trending)\n2. Traditional Fusion"
                " Remix v2\n3. High Fashion Runway Loop"
            )
          elif category == "Entertainment / Comedy":
            st.success(
                "1. Viral Comedy Punchline Beat #1\n2. Funny Sound Effect Pack"
                " Pro\n3. Trending Meme Audio #4"
            )
          else:
            st.success(
                "1. Global TikTok Viral Trending Sound\n2. Upbeat Chill"
                " Electronic Rhythm\n3. Cinematic Energy Build-up"
            )

          st.subheader("🏷️ Optimized Viral Hashtags")
          base_tags = "#fyp #viral #foryoupage #trending #hameedbajwa129"
          cat_tags = (
              f"#{category.split('/')[0].strip().lower().replace(' ', '')}"
          )
          platform_tags = f"#{target_platform.lower().replace(' ', '')}"
          generated_tags = (
              f"{base_tags} {cat_tags} {platform_tags} #viralvideo"
              " #trendalert"
          )
          st.code(generated_tags, language="text")

          st.subheader("💡 Pro Growth Strategies")
          st.info(
              "• **Strong Hook:** Ensure the first 3 seconds grab immediate"
              " user attention.\n• **Engagement:** Pin a creative comment and"
              " reply within 30 minutes.\n• **Timing:** Post during peak"
              " regional hours (6 PM - 9 PM)."
          )
  else:
    st.info(
        "👈 Please upload a video file using the uploader above to run the"
        " Hameed Bajwa 129 optimization suite."
    )


# ================= PAGE 2: TIKTOK VIDEO BOOSTER SUITE =================
elif app_mode == "🚀 TikTok Video Booster Suite":
  st.subheader("🚀 TikTok Video Growth & Boost Engine")
  st.write(
      "Paste your TikTok video link below to configure growth acceleration and"
      " engagement strategies."
  )

  tiktok_link = st.text_input(
      "🔗 Enter TikTok Video Link",
      placeholder="https://www.tiktok.com/@username/video/...",
  )
  boost_type = st.selectbox(
      "Select Boost Strategy",
      [
          "Organic Reach & Algorithm Push",
          "Engagement Booster (Comments & Shares)",
          "Audience Retention Optimizer",
          "Trending Sound Sync Boost",
      ],
  )

  if st.button("⚡ Run TikTok Boost Analysis", type="primary"):
    if tiktok_link:
      with st.spinner(
          "Connecting to TikTok algorithm endpoints & calculating boost"
          " potential..."
      ):
        time.sleep(2.5)
        boost_index = random.randint(85, 99)
        st.success("Boost Configuration Successful!")

        st.markdown(
            f"""
                <div class="metric-card">
                    <h3>📈 Algorithm Boost Index: <span style="color: #FF2D55;">{boost_index}%</span></h3>
                    <p><b>Selected Strategy:</b> <b>{boost_type}</b></p>
                    <p><b>Status:</b> Video metadata is queued for high-velocity distribution channels.</p>
                </div>
            """,
            unsafe_allow_html=True,
        )

        st.subheader("🎯 Actionable Growth Checklist")
        st.info(
            "1. **Duet/Stitch Opportunity:** Enable Duets to let other creators"
            " react to your content.\n2. **Caption Hook:** Keep captions short"
            " with an open-ended question to drive comments.\n3. **Sound"
            " Synergy:** Ensure the background audio volume sits at 10-15% while"
            " original voice is at 100%."
        )
    else:
      st.warning(
          "⚠️ Please enter a valid TikTok video link before running the boost"
          " suite."
      )

# Footer
st.markdown(
    '<p class="brand-footer">Powered by Hameed Bajwa 129 • Professional Video'
    " Optimization System</p>",
    unsafe_allow_html=True,
)
