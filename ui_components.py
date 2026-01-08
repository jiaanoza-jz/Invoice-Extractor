import streamlit as st
import base64
from streamlit.components.v1 import html

def apply_custom_ui():
    """Applies the 2026 Bento-Glass Design."""
    st.markdown("""
        <style>
        .stApp {
            background-color: #0b0e14;
            background-image: 
                radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.4) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(88, 28, 135, 0.3) 0px, transparent 50%),
                radial-gradient(at 50% 0%, rgba(15, 23, 42, 0.9) 0px, transparent 50%);
            background-attachment: fixed;
            color: #e2e8f0;
        }

        [data-testid="stVerticalBlockBorderWrapper"]:has(div[class*="st-key-glass-"]) {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px) saturate(180%);
            border-radius: 28px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 35px;
            margin-bottom: 30px;
        }

        .main-title {
            font-size: 4.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, #fff 40%, #64748b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        .stButton>button {
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
            color: white;
            border-radius: 14px;
            height: 3.5em;
            font-weight: 700;
            width: 100%;
            border: none;
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3);
        }

        footer, header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def scroll_to_bottom():
    """Forced JavaScript Scroll to the main page bottom."""
    js_code = """
        <script>
            setTimeout(function() {
                const mainArea = window.parent.document.querySelector('section.main');
                if (mainArea) {
                    mainArea.scrollTo({ top: mainArea.scrollHeight, behavior: 'smooth' });
                }
            }, 500);
        </script>
    """
    
    html(js_code, height=0)

def render_header():
    st.markdown('<h1 class="main-title">DocuMind AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#94a3b8; font-size:1.2rem; margin-bottom:60px;">Intelligent Extraction for Bills, Challans & Letters</p>', unsafe_allow_html=True)

def display_pdf(uploaded_file):
    base64_pdf = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" style="border:none; border-radius:20px;"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)