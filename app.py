import streamlit as st
import os
import re

st.set_page_config(
    page_title="NALDA Green Hope Ambassador Certificate Portal", 
    page_icon="🌾", 
    layout="centered"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #0f172a !important;
        }
        
        .stApp {
            background: linear-gradient(135deg, #f4f7f5 0%, #e8f1ec 50%, #f1f5f9 100%);
        }
        
        .hero-card {
            background: #ffffff;
            padding: clamp(2.5rem, 6vw, 4rem) clamp(2rem, 5vw, 3.5rem);
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 77, 37, 0.1), 0 0 0 1px rgba(0, 77, 37, 0.05);
            margin-top: 2rem;
            margin-bottom: 2rem;
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .hero-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #004d25 0%, #2e7d32 50%, #81c784 100%);
        }
        
        .agency-tag {
            background-color: #e8f5e9;
            color: #004d25 !important;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            padding: 0.45rem 1.1rem;
            border-radius: 50px;
            display: inline-block;
            margin-bottom: 1.25rem;
            border: 1px solid #c8e6c9;
        }
        
        .portal-heading {
            font-size: clamp(1.85rem, 4vw, 2.6rem);
            font-weight: 800;
            color: #0b3820 !important;
            margin-bottom: 0.75rem;
            letter-spacing: -0.03em;
            line-height: 1.2;
        }
        
        .portal-subtext {
            font-size: clamp(0.95rem, 2vw, 1.1rem);
            color: #475569 !important;
            line-height: 1.6;
            margin-bottom: 2.5rem;
        }
        
        .stTextInput label {
            font-weight: 700 !important;
            color: #1e293b !important;
            font-size: 0.95rem !important;
            margin-bottom: 0.5rem !important;
        }
        
        .stTextInput input {
            border-radius: 14px !important;
            border: 2px solid #cbd5e1 !important;
            padding: 0.95rem 1.2rem !important;
            font-size: 1.05rem !important;
            background-color: #f8fafc !important;
            color: #0f172a !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        
        .stTextInput input:focus {
            border-color: #004d25 !important;
            background-color: #ffffff !important;
            box-shadow: 0 0 0 4px rgba(0, 77, 37, 0.12), 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        }
        
        .stButton>button {
            width: 100%;
            background: linear-gradient(135deg, #004d25 0%, #006837 100%);
            color: #ffffff !important;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 0.95rem 1.2rem;
            border-radius: 14px;
            border: none;
            transition: all 0.25s ease;
            box-shadow: 0 10px 20px -5px rgba(0, 77, 37, 0.3);
            margin-top: 1.25rem;
            min-height: 52px;
        }
        
        .stButton>button:hover {
            background: linear-gradient(135deg, #00381b 0%, #004d25 100%);
            transform: translateY(-2px);
        }
        
        [data-testid="stExpander"] {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02) !important;
        }
        
        [data-testid="stExpander"] summary p,
        [data-testid="stExpander"] details div p,
        [data-testid="stExpander"] ul li {
            color: #1e293b !important;
            font-size: 0.95rem !important;
            line-height: 1.6 !important;
        }
        
        .stAlert p, .stAlert span {
            color: #0f172a !important;
        }
        
        .footer-info {
            text-align: center;
            font-size: 0.85rem;
            color: #64748b !important;
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = os.path.join(BASE_DIR, "certificates")

st.markdown("""
    <div class="hero-card">
        <div style="text-align: center;">
            <div class="agency-tag">National Agricultural Land Development Authority</div>
            <div class="portal-heading">Green Hope Ambassador Certificate Portal</div>
            <div class="portal-subtext">
                Enter your registered email address below to securely access and download your official ambassador certificate.
            </div>
        </div>
""", unsafe_allow_html=True)

with st.form("nalda_standardized_form"):
    email_input = st.text_input(
        "✉️ Registered Email Address", 
        placeholder="e.g., participant@domain.com",
        help="Provide the exact email address used during your training registration."
    )
    submitted = st.form_submit_button("Verify & Download Certificate")

STRICT_EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if submitted:
    clean_email = email_input.strip().lower()
    
    if not clean_email:
        st.warning("Please enter your registered email address.")
    elif not re.match(STRICT_EMAIL_REGEX, clean_email):
        st.error("Please enter a valid email format (e.g., participant@domain.com).")
    else:
        safe_filename = f"{clean_email}.pdf"
        file_path = os.path.abspath(os.path.join(CERT_DIR, safe_filename))
        
        if not file_path.startswith(os.path.abspath(CERT_DIR)):
            st.error("Security validation error detected.")
        elif os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
            
            st.success("Credential successfully verified against NALDA records.")
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="📥 Download Official Certificate (PDF)",
                data=pdf_bytes,
                file_name=f"GREEN_HOPE_Certificate_{clean_email}.pdf",
                mime="application/pdf"
            )
        else:
            st.error("No verified credential record found matching this email address. Please check your spelling or contact helpdesk.")

st.markdown('</div>', unsafe_allow_html=True)

with st.expander("Need Help or Support?"):
    st.markdown("""
    * **Missing Certificate:** Ensure you enter the exact email address used during your training registration.
    * **Technical Support:** Reach out to the NALDA Helpdesk headquarters in Abuja for assistance with credential discrepancies.
    """)

st.markdown("""
    <div class="footer-info">
        &copy; 2026 National Agricultural Land Development Authority (NALDA) &bull; Headquarters, Abuja
    </div>
""", unsafe_allow_html=True)
