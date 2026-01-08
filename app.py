import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
from ui_components import apply_custom_ui, render_header, display_pdf, scroll_to_bottom

# 1. Page & AI Setup
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-2.5-flash')

st.set_page_config(page_title="DocuMind AI", layout="wide")
apply_custom_ui()
render_header()

# 2. Bento Grid
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    with st.container(key="glass-input"):
        st.subheader("📁 Document Feed")
        file = st.file_uploader("Upload Image or PDF", type=["jpg", "png", "jpeg", "pdf"], label_visibility="collapsed")
        
        st.markdown('<div style="margin-top:25px;"></div>', unsafe_allow_html=True)
        st.subheader("🧠 Ask the AI")
        # Enter key automatically triggers a rerun in st.text_input
        query = st.text_input("Enter your request...", placeholder="e.g., Extract items from this bill", key="query_input")
        
        st.markdown('<div style="margin-top:10px;"></div>', unsafe_allow_html=True)
        btn_clicked = st.button("🚀 Analyze Now")

with col2:
    with st.container(key="glass-preview"):
        st.subheader("🔍 Preview")
        if file:
            if "pdf" in file.type: display_pdf(file) #
            else: st.image(Image.open(file), use_container_width=True)
        else:
            st.caption("Awaiting document...")

# 3. Execution Logic
# If enter is pressed (query changed) or button is clicked, start analysis
if (btn_clicked or (query and query != st.session_state.get('last_run_query', ''))) and file and query:
    st.session_state['last_run_query'] = query # Prevent looping
    
    with st.status("🤖 DocuMind is thinking...", expanded=True) as status:
        file_parts = [{"mime_type": file.type, "data": file.getvalue()}]
        response = model.generate_content(["Extract info as requested:", file_parts[0], query])
        status.update(label="Analysis Finished!", state="complete")
    
    # 4. Result Display
    with st.container(key="glass-results"):
        st.subheader("📊 Extraction Intelligence")
        st.write(response.text)
    
    # 5. TRIGGER THE SCROLL
    scroll_to_bottom()

elif btn_clicked and not file:
    st.error("Please upload a document first.")