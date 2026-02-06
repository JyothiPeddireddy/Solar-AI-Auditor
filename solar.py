# ============================================================
# 🌞 SOLAR AI AUDITOR 2026
# ============================================================






import streamlit as st
import os
import requests
from google import genai
# import google.generativeai as genai
from PIL import Image
from io import BytesIO
# import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time





# ============================================================
# 1. SETUP
# ============================================================

# Gemini API Key (Ensure it is valid) 

API_KEY = "AIzaSyBBde7P7DrLsvAODAwdiItGEU-GQnUA67k" 


# Initialize Gemini Client
client = genai.Client(api_key=API_KEY)

# Streamlit Page Configuration
st.set_page_config(
    page_title="Solar AI Assistant",
    layout="wide"
)





# ============================================================
# UI THEME (ONLY UI CHANGES)
# ============================================================


st.markdown("""
<style>

/* App Background - Soft Blue Tint */
.stApp {
    background-color: #f0f7ff !important;
}

/* Header Styling */
.header-box {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
    padding: 30px 40px;
    border-radius: 20px;
    color: white;
    box-shadow: 0px 10px 30px rgba(99, 102, 241, 0.2);
    margin-bottom: -50px;
    text-align: left;
}

.header-box h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
    margin-bottom: 5px;
}

/* Glass Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.8) !important;
    backdrop-filter: blur(10px);
    border-radius: 25px;
    padding: 30px;
    box-shadow: 0px 15px 35px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.5);
    transition: transform 0.3s ease;
    margin-top: 20px;
}

.glass-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 20px 40px rgba(0, 0, 0, 0.1);
}

/* KPI Text */
.glass-card h3 {
    color: #1e293b !important;
    font-size: 1.5rem !important;
    display: flex;
    align-items: center;
    gap: 10px;
}

.glass-card h1 {
    color: #0f172a !important;
    font-size: 2.8rem !important;
    font-weight: 700 !important;
    margin: 15px 0;
}

/* Badge */
.badge {
    background: #e0f2fe;
    color: #0369a1;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
}

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background-color: white !important;
#     border-right: 1px solid #e2e8f0;
# }
/* Sidebar - Soft Blue Gradient to match your Image */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f0f7ff 0%, #e0f2fe 100%) !important;
    border-right: 1px solid #d1e9ff !important;
}

/* Sidebar Widgets (Dropdowns/Inputs) Styling */
section[data-testid="stSidebar"] .stSelectbox, 
section[data-testid="stSidebar"] .stNumberInput {
    background-color: rgba(255, 255, 255, 0.6) !important;
    border-radius: 12px !important;
    border: 1px solid #d1e9ff !important;
}

/* Sidebar Labels for better readability */
section[data-testid="stSidebar"] label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

/* Progress Bar */
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    border: none !important;
    background-color: transparent !important;
    font-weight: 600 !important;
    color: #475569 !important;
    padding: 10px 25px !important;
    border-radius: 12px !important;
    margin-right: 10px !important;
    transition: all 0.3s ease !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
    color: white !important;
    box-shadow: 0px 5px 15px rgba(6, 182, 212, 0.4) !important;
    border-radius: 12px !important;
}

div[data-baseweb="tab-highlight"] {
    background-color: transparent !important;
}

/* Chat Input */
.stChatInputContainer {
    border-radius: 15px !important;
    border: 1px solid #e2e8f0 !important;
    background-color: #f8fafc !important;
}

/* 🔥 FIXED Generate Image Button (REAL STREAMLIT STRUCTURE) */
.ai-btn div[data-testid="stButton"] > button {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
    color: white !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 12px 28px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
}

.ai-btn div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.25);
}
/* 🚀 FORCE STYLE ALL STREAMLIT BUTTONS */
.stButton > button {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
    color: white !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 12px 28px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.25) !important;
}

/* 🎤 Mic Button Styling */
.mic-btn {
    position: relative;
    margin-top: -58px;
    float: right;
    margin-right: 10px;
    z-index: 999;
}

.mic-btn button {
    background: linear-gradient(90deg, #6366f1, #06b6d4) !important;
    border-radius: 50% !important;
    width: 42px !important;
    height: 42px !important;
    font-size: 18px !important;
    padding: 0 !important;
}

</style>
""", unsafe_allow_html=True)







# ============================================================
# 2. LOGIC (UNCHANGED)
# ============================================================

def get_efficiency(state):
    """
    Calculates efficiency based on 2026 TOPCon standards
    """
    baseline = 24.5

    impacts = {
        "Clean": 1.0,
        "Dusty": 0.82,
        "Bird Droppings": 0.65,
        "Electrical Damage": 0.12,
        "Physical Damage": 0.35
    }

    curr = baseline * impacts.get(state, 1.0)

    return round(curr, 2), round(curr - baseline, 2)





def generate_visual(prompt, seed):
    """
    Generates solar panel image using Flux model
    """
    clean_prompt = prompt.replace(' ', '%20')

    url = (
        f"https://image.pollinations.ai/prompt/"
        f"{clean_prompt}"
        f"?width=1024&height=1024"
        f"&nologo=true&seed={seed}&model=flux"
    )

    try:
        res = requests.get(url, timeout=25)

        if res.status_code == 200:
            return Image.open(BytesIO(res.content))

        return None

    except:
        return None




# ============================================================
# HEADER SECTION
# ============================================================

st.markdown("""
<div class="header-box">
    <h1>☀️ Solar AI Assistant</h1>
    <p>AI-Powered Solar Panel Health, Efficiency & Visual Intelligence</p>
</div>
""", unsafe_allow_html=True)





# ============================================================
# SIDEBAR INPUTS
# ============================================================

st.sidebar.header("🔧 Solar Input Settings")

# site = st.sidebar.text_input(
#     "📍 Location",
#     "Bapatla, India"
# )
site = st.sidebar.selectbox(
    "📍 Location (Andhra Pradesh)",
    [
        "Visakhapatnam",
        "Vijayawada",
        "Guntur",
        "Nellore",
        "Kurnool",
        "Tirupati",
        "Rajahmundry",
        "Kakinada",
        "Anantapur",
        "Kadapa (YSR Kadapa)",
        "Ongole",
        "Eluru",
        "Srikakulam",
        "Vizianagaram",
        "Chittoor",
        "Machilipatnam",
        "Tenali",
        "Hindupur",
        "Proddatur",
        "Bapatla"
    ]
)
coastal_cities = ["Visakhapatnam", "Nellore", "Machilipatnam", "Kakinada"]
hot_dry = ["Anantapur", "Kurnool", "Kadapa"]
urban = ["Vijayawada", "Guntur", "Tirupati"]

environment = ""

if site in coastal_cities:
    environment = "coastal humidity, sea breeze atmosphere"

elif site in hot_dry:
    environment = "dry climate, strong sunlight, dusty air"

elif site in urban:
    environment = "urban industrial surroundings"




state = st.sidebar.selectbox(
    "⚙️ Panel Condition",
    [
        "Clean",
        "Dusty",
        "Bird Droppings",
        "Electrical Damage",
        "Physical Damage"
    ]
)

seed = st.sidebar.number_input(
    "📷 Camera Seed",
    value=42
)
def plot_efficiency_bar(selected_state):
    conditions = [
        "Clean",
        "Dusty",
        "Bird Droppings",
        "Electrical Damage",
        "Physical Damage"
    ]

    efficiencies = [get_efficiency(c)[0] for c in conditions]

    placeholder = st.empty()

    for i in range(1, len(conditions) + 1):
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=conditions[:i],
            y=efficiencies[:i],
            text=[f"{v}%" for v in efficiencies[:i]],
            textposition="outside",
            marker=dict(
                color=efficiencies[:i],
                colorscale="Turbo",
                line=dict(color="#1e293b", width=1.5)
            ),
            hovertemplate="<b>%{x}</b><br>Efficiency: %{y}%<extra></extra>"
        ))

        fig.update_layout(
            title="⚡ Solar Panel Efficiency Comparison",
            template="plotly_white",
            height=450,
            yaxis=dict(title="Efficiency Output (%)"),
            xaxis=dict(title="Panel Condition")
        )

        placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.25)





# ============================================================
# KPI / METRIC CARDS
# ============================================================

eff, delta = get_efficiency(state)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="glass-card">
        <h3>⚡ Efficiency</h3>
        <h4>{eff}%</h4>
        <div class="badge">{delta}% vs Peak</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="glass-card">
        <h3>📍 Site</h3>
        <h4>{site}</h4>
        <div class="badge">Andhra Pradesh</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="glass-card">
        <h3>🔍 Condition</h3>
        <h4>{state}</h4>
        <div class="badge">AI Detected</div>
    </div>
    """, unsafe_allow_html=True)





# ============================================================
# EFFICIENCY PROGRESS BAR
# ============================================================

st.markdown(
    "<div class='progress-label'>🔋 Efficiency Utilization</div>",
    unsafe_allow_html=True
)

st.progress(
    min(int((eff / 25) * 100), 100)
)   


# ============================================================
# 📊 DYNAMIC EFFICIENCY BAR GRAPH
# ============================================================

st.markdown("### 📊 Solar Energy Efficiency Comparison")

# fig = plot_efficiency_bar(state)
# st.pyplot(fig)
plot_efficiency_bar(state)




st.divider()





# ============================================================
# TABS SECTION
# ============================================================

tab_text, tab_img = st.tabs(
    ["📋 Point-Wise Audit", "🖼️ AI Visualizer"]
)





# ============================================================
# TAB 1: TEXT AUDIT
# ============================================================

with tab_text:

    st.subheader("Maintenance Chat & Bilingual Audit")

    user_query = st.chat_input(
        "Ask a question (e.g., Explain electrical vs physical damage)"
    )

    if user_query:

        with st.spinner("Generating English & Telugu analysis..."):

            sys_msg = (
                "You are a Solar Expert.\n"
                "1. Provide point-wise analysis in English.\n"
                "2. Provide the EXACT SAME analysis in Telugu (తెలుగు).\n"
                "3. Use Markdown bullets (-).\n"
                "4. Keep a BLANK LINE between each bullet.\n"
                "5. STRICTLY NO HINDI.\n"
                "6. Output ONLY the text."
            )

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    config={
                        "system_instruction": sys_msg,
                        "safety_settings": [
                            {
                                "category": "HARM_CATEGORY_HARASSMENT",
                                "threshold": "BLOCK_NONE"
                            }
                        ]
                    },
                    contents=(
                        f"Efficiency: {eff}%. "
                        f"Site: {site}. "
                        f"Condition: {state}. "
                        f"Question: {user_query}"
                    )
                )

                if response.text:
                    st.markdown(response.text)
                else:
                    st.warning("Response blocked. Try another query.")

            except Exception as e:
                st.error(f"Text Error: {e}")





# ============================================================
# TAB 2: IMAGE VISUALIZER
# ============================================================

with tab_img:

    st.subheader("Technical Visual State")

    user_p = st.text_area(
        "Image Prompt",
        value=(
            f"Industrial photo of solar panels in {site} "
            f"with {state}, 8k, realistic technical detail"
        )
    )

    # if st.button("Generate Image"):
    st.markdown("<div class='ai-btn'>", unsafe_allow_html=True)
    generate_btn = st.button("🎨 Generate AI Image")
    st.markdown("</div>", unsafe_allow_html=True)

    if generate_btn:


        with st.spinner("Generating visual..."):

            img = generate_visual(user_p, seed)

            if img:
                st.image(img, use_container_width=True)
            else:
                st.error("Image service busy. Try again shortly.")





# ============================================================
# END OF FILE
# ============================================================