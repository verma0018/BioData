import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Tushar Verma | Biodata",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------- CSS ----------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255,145,77,0.25), transparent 30%),
            radial-gradient(circle at bottom right, rgba(255,255,255,0.08), transparent 30%),
            linear-gradient(135deg, #0b1020 0%, #121c35 50%, #1c2947 100%);
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .glass {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        backdrop-filter: blur(18px);
        border-radius: 28px;
        box-shadow: 0 25px 45px rgba(0,0,0,0.25);
    }

    .hero {
        padding: 2rem;
        margin-bottom: 2rem;
    }

    .tag {
        display: inline-block;
        padding: 0.55rem 1rem;
        border-radius: 999px;
        background: rgba(255,145,77,0.15);
        border: 1px solid rgba(255,145,77,0.3);
        color: #ffb37a;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .title {
        font-size: 4rem;
        font-weight: 800;
        line-height: 1.05;
        margin-bottom: 1rem;
    }

    .subtitle {
        color: rgba(255,255,255,0.75);
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 1.5rem;
        max-width: 650px;
    }

    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin-top: 1rem;
    }

    .chip {
        padding: 0.7rem 1rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        color: #f4f4f4;
        font-size: 0.9rem;
    }

    .profile-wrap {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .profile-frame {
        padding: 0.6rem;
        border-radius: 30px;
        background: linear-gradient(145deg, rgba(255,145,77,0.8), rgba(255,255,255,0.1));
        box-shadow: 0 20px 50px rgba(255,145,77,0.2);
    }

    .section {
        padding: 1.8rem;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.45rem;
        font-weight: 700;
        color: #ffcb9a;
        margin-bottom: 1.2rem;
    }

    .info-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        margin-bottom: 1rem;
        transition: 0.3s ease;
    }

    .info-card:hover {
        transform: translateY(-4px);
        background: rgba(255,255,255,0.08);
    }

    .label {
        font-size: 0.82rem;
        color: #ffb37a;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.4rem;
        font-weight: 600;
    }

    .value {
        font-size: 1rem;
        color: rgba(255,255,255,0.9);
        line-height: 1.7;
    }

    .family-box {
        padding: 1rem;
        border-radius: 18px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        text-align: center;
        min-height: 140px;
    }

    .family-box strong {
        display: block;
        margin-bottom: 0.4rem;
        font-size: 1.05rem;
    }

    .contact-box {
        text-align: center;
        padding: 2rem;
    }

    .contact-item {
        font-size: 1.05rem;
        margin: 0.8rem 0;
        color: rgba(255,255,255,0.9);
    }

    .gallery-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #ffcb9a;
        margin-bottom: 1rem;
    }

    .footer {
        text-align: center;
        margin-top: 2rem;
        color: rgba(255,255,255,0.55);
        font-size: 0.9rem;
    }

    @media (max-width: 900px) {
        .title {
            font-size: 2.7rem;
            text-align: center;
        }

        .subtitle, .chips {
            text-align: center;
            justify-content: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------- Images ----------------------
family = Image.open("images/smile.jpg")
profile = Image.open("images/profile.webp")
travel = Image.open("images/kurta.jpg")
work = Image.open("images/work.jpeg")

# ---------------------- Hero ----------------------
left, right = st.columns([1, 1.5])

with left:
    st.markdown('<div class="profile-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="profile-frame">', unsafe_allow_html=True)
    st.image(profile, use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass hero">', unsafe_allow_html=True)
    st.markdown('<div class="tag">Senior Engineer • SanDisk India</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">Tushar Verma</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">M.Tech graduate from NIT Surathkal, currently working in Bengaluru. A blend of strong values, modern outlook and meaningful ambitions, with interests in travelling, sports, music and automobiles.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '''
        <div class="chips">
            <div class="chip">📍 Bengaluru</div>
            <div class="chip">🎓 NIT Surathkal</div>
            <div class="chip">💼 Senior Engineer</div>
            <div class="chip">🌱 Vegetarian</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Details ----------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Personal Details</div>', unsafe_allow_html=True)

    items = [
        ("Date of Birth", "18 January 2001"),
        ("Height", "6\'0\""),
        ("Religion", "Hindu"),
        ("Lifestyle", "Non-Drinker, Non-Smoker, Vegetarian")
    ]

    for label, value in items:
        st.markdown(f'<div class="info-card"><div class="label">{label}</div><div class="value">{value}</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Education & Career</div>', unsafe_allow_html=True)

    items = [
        ("Education", "M.Tech in Computer Science & Engineering"),
        ("Institute", "NIT Surathkal"),
        ("Occupation", "Senior Engineer"),
        ("Company", "SanDisk India, Bengaluru")
    ]

    for label, value in items:
        st.markdown(f'<div class="info-card"><div class="label">{label}</div><div class="value">{value}</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Family ----------------------
st.markdown('<div class="glass section">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Family</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown('<div class="family-box"><strong>Mr. Sajjan Kumar</strong>Chief Manager<br>Central Bank of India</div>', unsafe_allow_html=True)
with f2:
    st.markdown('<div class="family-box"><strong>Mrs. Parmila Devi</strong>Homemaker</div>', unsafe_allow_html=True)
with f3:
    st.markdown('<div class="family-box"><strong>Dhruv Verma</strong>Brother • 21 Years</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Gallery ----------------------
st.markdown('<div class="glass section">', unsafe_allow_html=True)
st.markdown('<div class="gallery-title">Gallery</div>', unsafe_allow_html=True)

g1, g2 = st.columns(2)
with g1:
    st.image(family, use_container_width=True)
    st.image(work, use_container_width=True)

with g2:
    st.image(travel, use_container_width=True)
    st.image(profile, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------- Bottom ----------------------
left, right = st.columns([1,1])

with left:
    st.markdown('<div class="glass section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Hobbies & Interests</div>', unsafe_allow_html=True)
    st.markdown(
        '''
        <div class="chips">
            <div class="chip">🎵 Singing</div>
            <div class="chip">✏️ Sketching</div>
            <div class="chip">✈️ Travelling</div>
            <div class="chip">🏏 Sports</div>
            <div class="chip">🚗 Automobile Enthusiast</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass contact-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">📧 verma071276@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">📱 +91 7067324323</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Designed with Streamlit ✨</div>', unsafe_allow_html=True)
