"""
Configuration and UI Theme Settings for Guardian Health Insurance.
Contains styling rules, dummy content, brand configurations, and custom CSS
for transforming default Streamlit layouts into a premium portal.
"""

import streamlit as st

# ==========================================
# 🛡️ BRAND & COMPANY CONFIGURATIONS
# ==========================================
COMPANY_NAME = "Guardian Health Insurance"
TAGLINE = "Protecting Your Health, Securing Your Future"
CONTACT_EMAIL = "support@guardianhealth.com"
CONTACT_PHONE = "+1-800-555-0199"
OFFICE_ADDRESS = "101, Corporate Heights, Sector 62, Noida, Uttar Pradesh, 201301"
SUPPORT_HOURS = "Mon - Sat: 9:00 AM - 6:00 PM IST"
GOOGLE_MAPS_EMBED_URL = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3502.404847953255!2d77.37123987550019!3d28.61761897567406!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390ce5a230a2a197%3A0xe962df32c96c4d44!2sSector%2062%2C%20Noida%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"

# ==========================================
# 🎨 COLOR PALETTE DESIGN TOKENS
# ==========================================
COLOR_PRIMARY = "#0C2340"    # Deep Corporate Navy
COLOR_SECONDARY = "#1E88E5"  # Active Accent Sky Blue
COLOR_BACKGROUND = "#F5F7FA" # Clean Neutral Gray Page Background
COLOR_WHITE = "#FFFFFF"      # Card Backgrounds
COLOR_TEXT = "#333333"       # Dark Gray Body Text
COLOR_MUTED = "#757575"      # Light Gray Muted Text
COLOR_ACCENT = "#FF7043"     # Coral Orange (Popular Plan / Warning Badges)
COLOR_SUCCESS = "#2E7D32"    # Emerald Green (Healthy Badge / Low Risk)
COLOR_WARNING = "#EF6C00"    # Dark Orange (Overweight / Medium Risk)
COLOR_DANGER = "#C62828"     # Deep Crimson (Obese / High-Critical Risk)

# ==========================================
# 📝 STATIC CONTENT (LANDING & PAGES)
# ==========================================
# Testimonials Dummy Data
TESTIMONIALS = [
    {
        "name": "Arjun Sharma",
        "role": "Software Engineer, Bengaluru",
        "rating": 5,
        "feedback": "Guardian Health Insurance made estimating my premium so transparent. The rule explanations helped me understand exactly where my premium comes from. The PDF quote was perfect for my records."
    },
    {
        "name": "Priya Patel",
        "role": "Business Owner, Ahmedabad",
        "rating": 5,
        "feedback": "The multi-step calculator is exceptionally user-friendly. Being able to compare plans side-by-side with rule-based breakdowns is exactly what premium calculations should look like."
    },
    {
        "name": "Dr. Rajesh Verma",
        "role": "Medical Practitioner, Mumbai",
        "rating": 4,
        "feedback": "As a doctor, I highly appreciate the inclusion of BMI checks and lifestyle adjustments in the calculator. Extremely robust and realistic insurance pricing structure."
    }
]

# FAQ - Minimum 8 Questions
FAQS = [
    {
        "q": "How is my premium calculated in this system?",
        "a": "Our premium calculator uses a 100% deterministic, rule-based actuarial engine. It starts with a base price depending on your chosen plan, and applies surcharges for health risks (e.g., smoking, heart disease) and discounts for healthy lifestyles (regular exercise, existing insurance)."
    },
    {
        "q": "What are the default insurance plans available?",
        "a": "We offer three plans: Basic (₹5 Lakhs cover), Silver (₹10 Lakhs cover), and Gold (₹20 Lakhs cover). The Gold plan is our most comprehensive and popular choice."
    },
    {
        "q": "What is the legal validity of the generated PDF quotation?",
        "a": "This quote is an estimate generated using predefined rule-based logic for educational and analytical purposes. It should not be considered an official commercial insurance quote."
    },
    {
        "q": "How does BMI affect my insurance premium?",
        "a": "BMI is calculated using your height and weight. Underweight (<18.5) attracts a 5% surcharge, overweight (25-29.9) attracts a 10% surcharge, and obese (>=30) attracts a 25% surcharge. A healthy BMI (18.5-24.9) incurs no surcharge."
    },
    {
        "q": "Do I get a discount for policy duration?",
        "a": "Yes! Standard policy terms are 1 year. Opting for a 2-year duration grants a 5% discount, while a 3-year commitment yields a 10% discount on the total gross premium."
    },
    {
        "q": "What is considered a high-risk occupation in the calculator?",
        "a": "Jobs involving aviation, heavy construction, deep-sea diving, and mining are classified as high-risk occupations. They carry a 15% surcharge due to elevated occupational hazards."
    },
    {
        "q": "Can I view my premium calculation history?",
        "a": "Yes. Once you register and log in, all your premium calculations are securely stored in our database. You can view them on your Dashboard and download the detailed PDF reports at any time."
    },
    {
        "q": "Is my personal and health data secure?",
        "a": "Absolutely. Passwords are saved as securely hashed strings using the SHA-256 algorithm with individual salts. Database interactions use parameterized queries to prevent SQL injections."
    }
]

# ==========================================
# 🎨 CUSTOM STYLING (GLOBAL CSS INJECTIONS)
# ==========================================
def inject_custom_css():
    """
    Injects custom styles into Streamlit to modify fonts, buttons, cards,
    and sidebars, removing default designs for a premium website feel.
    """
    st.markdown(f"""
    <style>
        /* Import Outfit and Inter Font Families */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

        /* Global Typography Setups */
        html, body, [class*="css"], .stApp {{
            font-family: 'Inter', sans-serif;
            background-color: {COLOR_BACKGROUND};
            color: {COLOR_TEXT};
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Outfit', sans-serif;
            color: {COLOR_PRIMARY};
            font-weight: 700;
        }}

        /* Hide Streamlit Default UI Elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        .stDeployButton {{display:none;}}

        /* Navigation Bar Styles */
        .navbar-container {{
            background-color: {COLOR_PRIMARY};
            padding: 15px 30px;
            border-bottom: 3px solid {COLOR_SECONDARY};
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 8px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }}
        
        .navbar-brand {{
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 800;
            color: white !important;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .navbar-tagline {{
            font-size: 12px;
            font-weight: 400;
            color: #CFD8DC;
            margin: 0;
        }}

        /* Customized Cards & Containment UI */
        .card {{
            background-color: {COLOR_WHITE};
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(12, 35, 64, 0.05);
            border: 1px solid rgba(12, 35, 64, 0.08);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }}
        
        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(12, 35, 64, 0.1);
            border-color: {COLOR_SECONDARY};
        }}

        /* Highlighting cards (Gold Plan / Popular choices) */
        .card-popular {{
            border: 2px solid {COLOR_ACCENT} !important;
            position: relative;
        }}
        
        .popular-badge {{
            position: absolute;
            top: -12px;
            right: 20px;
            background-color: {COLOR_ACCENT};
            color: white;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }}

        /* Interactive Metrics Cards (KPIs) */
        .kpi-container {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 16px;
            background: white;
            border-radius: 10px;
            border-left: 5px solid {COLOR_SECONDARY};
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        
        .kpi-val {{
            font-size: 28px;
            font-weight: 800;
            color: {COLOR_PRIMARY};
            margin-top: 5px;
        }}
        
        .kpi-label {{
            font-size: 13px;
            color: {COLOR_MUTED};
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        /* Custom Buttons */
        .stButton>button {{
            background-color: {COLOR_SECONDARY};
            color: white !important;
            border-radius: 8px;
            border: none;
            padding: 10px 24px;
            font-weight: 600;
            font-family: 'Outfit', sans-serif;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(30, 136, 229, 0.2);
            width: 100%;
        }}
        
        .stButton>button:hover {{
            background-color: {COLOR_PRIMARY};
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 14px rgba(12, 35, 64, 0.3);
        }}
        
        .stButton>button:active {{
            transform: translateY(0);
        }}

        /* Secondary actions button style override */
        div[data-testid="stFormSubmitButton"] button, .btn-secondary {{
            background-color: {COLOR_PRIMARY} !important;
        }}
        
        div[data-testid="stFormSubmitButton"] button:hover, .btn-secondary:hover {{
            background-color: {COLOR_SECONDARY} !important;
        }}

        /* Metric Badges for BMI & Risk statuses */
        .badge-status {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 12px;
            text-transform: uppercase;
            text-align: center;
        }}
        
        .badge-healthy {{
            background-color: #E8F5E9;
            color: {COLOR_SUCCESS};
        }}
        
        .badge-warning {{
            background-color: #FFF3E0;
            color: {COLOR_WARNING};
        }}
        
        .badge-danger {{
            background-color: #FFEBEE;
            color: {COLOR_DANGER};
        }}

        /* Hero Banner Design */
        .hero-banner {{
            background: linear-gradient(135deg, {COLOR_PRIMARY} 0%, #17375E 100%);
            border-radius: 16px;
            padding: 50px 40px;
            color: white;
            margin-bottom: 35px;
            box-shadow: 0 10px 25px rgba(12, 35, 64, 0.25);
            position: relative;
            overflow: hidden;
        }}
        
        .hero-title {{
            font-size: 38px;
            font-weight: 800;
            margin-bottom: 15px;
            color: white !important;
            line-height: 1.2;
        }}
        
        .hero-subtitle {{
            font-size: 18px;
            font-weight: 300;
            color: #ECEFF1;
            max-width: 650px;
            line-height: 1.6;
        }}

        /* Custom table styling */
        .custom-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 14px;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}
        
        .custom-table th {{
            background-color: {COLOR_PRIMARY};
            color: white;
            text-align: left;
            padding: 12px 15px;
            font-weight: 600;
        }}
        
        .custom-table td {{
            padding: 10px 15px;
            border-bottom: 1px solid #EEEEEE;
            color: {COLOR_TEXT};
        }}
        
        .custom-table tr:last-of-type td {{
            border-bottom: 2px solid {COLOR_PRIMARY};
        }}

        /* Custom footer layout */
        .footer-container {{
            background-color: {COLOR_PRIMARY};
            padding: 30px 20px;
            border-top: 4px solid {COLOR_SECONDARY};
            color: #B0BEC5;
            border-radius: 8px;
            margin-top: 50px;
            font-size: 13px;
        }}
        
        .footer-link {{
            color: white !important;
            text-decoration: none;
        }}
        
        .footer-link:hover {{
            color: {COLOR_SECONDARY} !important;
            text-decoration: underline;
        }}
        
        .footer-disclaimer {{
            font-size: 11px;
            color: #90A4AE;
            border-top: 1px solid #37474F;
            margin-top: 20px;
            padding-top: 15px;
            text-align: center;
        }}
    </style>
    """, unsafe_allow_html=True)
