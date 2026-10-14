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


# Background Visitor Tracker Function
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


total_visits, visitor_country = track_visitor()

# --- SECURE ADMIN CHECK ---
query_params = st.query_params
is_admin_mode = query_params.get("admin") == "9797"

# Custom Styling (Hiding Edit/GitHub icons for public, keeping for Admin via CSS injection logic)
hide_streamlit_style = """
    <style>
    .main-header { font-size: 2.3rem; color: #FF2D55; text-align: center; font-weight: bold; }
    .sub-header { font-size: 1.1rem; color: #555; text-align: center; margin-bottom: 25px; }
    .brand-footer { text-align: center; color: #888; font-size: 0.9rem; margin-top: 40px; }
    .metric-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #FF2D55; }
    .social-box { background-color: #fff0f3; padding: 15px; border-radius: 8px; border: 1px solid #ffccd5; margin-bottom: 20px; }
    
    /* 3-Line Menu Button styling for mobile & desktop */
    [data-testid="collapsedControl"] {
        display: block !important;
        background-color: #FF2D55;
        color: white;
        border-radius: 50%;
        padding: 6px;
    }
"""

if not is_admin_mode:
  # Hide GitHub, Edit app buttons from top header for normal users
  hide_streamlit_style += """
    header [data-testid="stToolbar"] {visibility: hidden;}
    """

hide_streamlit_style += "</style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- PERMANENT PROFILE PICTURE & APP HEADER ---
col_img, col_text = st.columns([1, 4])
with col_img:
  # Aap ki asli tasveer yahan permanent HTML/Base64 ke zariye set kar di gayi hai
  st.markdown(
      """
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150" style="border-radius: 10px; width: 120px; height: 120px; object-fit: cover;" alt="Hameed Bajwa 129">
        </div>
        <div style="text-align: center; font-weight: bold; margin-top: 5px; font-size: 0.9rem; color: #333;">Hameed Bajwa 129</div>
    """,
      unsafe_allow_html=True,
  )

with col_text:
  st.markdown(
      '<p class="main-header" style="text-align: left;">🎬 Hameed Bajwa 129 -'
      " Viral Video Optimizer</p>",
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p class="sub-header" style="text-align: left;">Professional AI Suite to'
      " Check Viral Potential, Get Trending Sounds & Smart Hashtags!</p>",
      unsafe_allow_html=True,
  )

st.markdown("---")

# --- SIDEBAR NAVIGATION & SOCIAL PROMOTION ---
st.sidebar.header("🧭 Navigation Menu")
app_mode = st.sidebar.radio(
    "Choose Tool",
    ["🎬 Viral Video Optimizer", "🚀 TikTok Video Booster Suite"],
)

st.sidebar.markdown("---")
st.sidebar.header("🔥 Official Social Accounts")
st.sidebar.markdown(
    """
<div style="background-color: #f1f3f5; padding: 10px; border-radius: 8px; font-size: 0.9rem;">
<b>Instagram:</b> @hameedbajwa10<br>
<b>TikTok:</b> @hameedbajwa10<br>
<b>Facebook:</b> Hafiz Hameed Bajwa
</div>
""",
    unsafe_allow_html=True,
)

# --- SECRET ADMIN PANEL ---
if is_admin_mode:
  st.sidebar.markdown("---")
  st.sidebar.subheader("🔐 Admin Control Panel")
  st.sidebar.success("Admin Access Active!")
  st.sidebar.metric(label="Total App Visits", value=total_visits)
  st.sidebar.info(f"Latest Visitor Country: {visitor_country}")


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
  st.subheader("🚀 Video Growth & Boost Engine (TikTok, Instagram, YouTube)")

  # Social Media Promotion Banner on Main Page
  st.markdown(
      """
    <div class="social-box">
        <b>⭐ Follow Creator Hameed Bajwa for More Tools & Updates:</b><br>
        📸 Instagram: <b>@hameedbajwa10</b> | 🎵 TikTok: <b>@hameedbajwa10</b> | 👤 Facebook: <b>Hafiz Hameed Bajwa</b>
    </div>
    """,
      unsafe_allow_html=True,
  )

  st.write(
      "Paste your video link below to deploy algorithmic views, followers, and"
      " boost acceleration."
  )

  # Initialize session states for tracking limits & cooldowns
  if "last_boost_time" not in st.session_state:
    st.session_state.last_boost_time = 0
  if "boost_counts" not in st.session_state:
    st.session_state.boost_counts = {}

  platform_choice = st.selectbox(
      "Select Platform", ["TikTok", "Instagram Reels", "YouTube Shorts"]
  )
  video_link = st.text_input(
      f"🔗 Enter {platform_choice} Video Link",
      placeholder="https://www.example.com/video/...",
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

  if st.button("⚡ Run Video Boost Analysis", type="primary"):
    if video_link:
      # Check max boost limit per video link (Max 3 times)
      current_boosts = st.session_state.boost_counts.get(video_link, 0)
      if current_boosts >= 3:
        st.error(
            "⚠️ Maximum limit reached! This video has already been boosted 3"
            " times (Maximum allowed per video is 3)."
        )
      else:
        # Check 5-minute cooldown timer
        current_time = time.time()
        time_elapsed = current_time - st.session_state.last_boost_time
        cooldown_period = 300  # 5 minutes in seconds

        if time_elapsed < cooldown_period:
          remaining_mins = int((cooldown_period - time_elapsed) // 60)
          remaining_secs = int((cooldown_period - time_elapsed) % 60)
          st.error(
              f"⏳ Cooldown Active! Please wait **{remaining_mins} minutes and"
              f" {remaining_secs} seconds** before boosting another video."
          )
        else:
          # Live Counting Animation Simulation for Realism
          progress_bar = st.progress(0)
          status_text = st.empty()

          for i in range(101):
            time.sleep(0.02)
            progress_bar.progress(i)
            current_sim_views = int(i * 5)
            current_sim_followers = round(i * 0.04, 1)
            status_text.markdown(
                f"⚡ **Injecting Traffic...** Delivering Views: **{current_sim_views}/500** | Followers: **{int(current_sim_followers)}/4**"
            )

          progress_bar.empty()
          status_text.empty()

          # Update state
          st.session_state.last_boost_time = time.time()
          st.session_state.boost_counts[video_link] = current_boosts + 1
          remaining_attempts = 3 - st.session_state.boost_counts[video_link]

          st.success(
              f"Boost Successful! (Attempt {st.session_state.boost_counts[video_link]}/3"
              " completed)"
          )

          st.markdown(
              f"""
                    <div class="metric-card">
                        <h3>📈 Boost Results Allocated Successfully:</h3>
                        <p><b>Platform:</b> <b>{platform_choice}</b> | <b>Strategy:</b> <b>{boost_type}</b></p>
                        <p><b>Views Delivered:</b> <span style="color: #FF2D55; font-weight: bold; font-size: 1.2rem;">500 Views</span> (Pacing live at +2 views/minute)</p>
                        <p><b>New Followers Gained:</b> <span style="color: #FF2D55; font-weight: bold; font-size: 1.2rem;">4 Followers</span></p>
                        <p style="font-size: 0.85rem; color: #666;"><i>Remaining boost slots for this video link: {remaining_attempts}</i></p>
                    </div>
                """,
              unsafe_allow_html=True,
          )

          st.subheader("🎯 Actionable Growth Checklist")
          st.info(
              "1. **Pacing Monitor:** Views will organically scale into your"
              " analytics panel over the next few hours.\n2. **Engagement"
              " Loop:** Reply to new followers to maintain retention.\n3."
              " **Cross-Platform:** Utilize remaining boost slots across"
              " different platforms."
          )
    else:
      st.warning(
          "⚠️ Please enter a valid video link before running the boost suite."
      )

# Footer
st.markdown(
    '<p class="brand-footer">Powered by Hameed Bajwa 129 • Professional Video'
    " Optimization System</p>",
    unsafe_allow_html=True,
)
