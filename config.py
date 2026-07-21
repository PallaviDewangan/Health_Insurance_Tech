"""
config.py
----------------------------------------------------
Global configuration for SecureLife Insurance System
----------------------------------------------------
"""

from pathlib import Path

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

APP_NAME = "SecureLife Insurance"

APP_VERSION = "1.0.0"

COMPANY_NAME = "SecureLife Insurance Pvt. Ltd."

PROJECT_TITLE = "Medical Insurance Premium Estimation System"

COPYRIGHT = "© 2026 SecureLife Insurance Pvt. Ltd."

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_NAME = "insurance.db"

DATABASE_PATH = BASE_DIR / DATABASE_NAME

ASSETS_DIR = BASE_DIR / "assets"

REPORTS_DIR = BASE_DIR / "reports"

# ==========================================================
# UI COLORS
# ==========================================================

PRIMARY_COLOR = "#0B4F9C"

SECONDARY_COLOR = "#1565C0"

SUCCESS_COLOR = "#2ECC71"

WARNING_COLOR = "#F39C12"

DANGER_COLOR = "#E74C3C"

BACKGROUND_COLOR = "#F5F7FB"

CARD_COLOR = "#FFFFFF"

TEXT_COLOR = "#1F2937"

# ==========================================================
# INSURANCE PLANS
# ==========================================================

INSURANCE_PLANS = {

    "Basic Care": {
        "coverage": 500000,
        "base_price": 5000
    },

    "Family Care": {
        "coverage": 1000000,
        "base_price": 10000
    },

    "Premium Care": {
        "coverage": 2000000,
        "base_price": 18000
    }

}

# ==========================================================
# BMI RANGES
# ==========================================================

BMI_CATEGORY = {

    "Underweight": (0, 18.5),

    "Normal": (18.5, 24.9),

    "Overweight": (25, 29.9),

    "Obese": (30, 100)

}

# ==========================================================
# RISK LEVELS
# ==========================================================

RISK_LEVELS = [

    "Low",

    "Moderate",

    "High"

]

# ==========================================================
# PDF SETTINGS
# ==========================================================

PDF_AUTHOR = "SecureLife Insurance"

PDF_SUBJECT = "Medical Insurance Premium Report"

PDF_TITLE = "Premium Estimation Report"

# ==========================================================
# DEFAULT ADMIN
# ==========================================================

DEFAULT_ADMIN = {

    "username": "secure_admin",

    "password": "Secure@2026"

}