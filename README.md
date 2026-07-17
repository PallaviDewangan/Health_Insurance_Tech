Guardian Health Insurance – Premium Estimation System is a professional, production-style medical insurance premium estimation portal. The system calculates premiums deterministically based on standard actuarial rules using customer demographics, medical history, lifestyle factors, and policy configurations.

IMPORTANT

This application is 100% Rule-Based. It does NOT use Machine Learning models, TensorFlow, Scikit-learn, or any predictive algorithms. This design choice ensures complete transparency, auditability, and regulatory compliance. AI-based estimations are proposed solely as future enhancements.

The system is developed as a Final Year B.Tech CSE (Artificial Intelligence) Major Project designed to demonstrate software architecture, database management, interactive data visualization, and professional custom-themed UI design using Streamlit.

✨ Features
Category	Feature	Description
User Role	👥 Dual Role Access	Separate user experiences for registered customers and portal administrators.
Authentication	🔒 Secure Auth	Hashed authentication using SHA-256 with username-based salting.
Calculator	📋 Multi-Step Form	Organized layout split into Personal, Health, Lifestyle, and Insurance details.
Analytics	📊 Visual Dashboard	Interactive Matplotlib graphics detailing premium allocations and BMI index gauges.
Reporting	📄 ReportLab PDF	Generates print-ready, professional PDF receipts with tabular breakdowns and disclaimers.
Admin Controls	🛠️ Admin Console	Cross-system KPI analysis, User CRUD controls, and premium logs CSV export.
UI/UX	🎨 Custom Theme	Global custom CSS injecting Outfit/Inter typography, rounded card layout, and soft shadows.
🛠️ Technology Stack
Frontend: Streamlit (overridden with custom CSS for corporate layouts and transitions)
Backend Core: Python (Rule-Based Actuarial Engine)
Database: SQLite (relational structure with automatic plan seeding)
Data Manipulation: Pandas (for dashboard rendering, filtering, and data downloads)
Visualizations: Matplotlib (for dashboard data charts and BMI sliders)
Report Engine: ReportLab (compiled PDF quote documents)
Cryptography: Hashlib (SHA-256 password security)
🏗️ Software Architecture Overview
The portal separates layout generation, database interaction, security, and rule processing modules. Below is the software modular workflow:

Mermaid diagram
📂 Folder Structure
The project code follows a modular, clean folder tree layout:

text

Health_Insurance_Tech/
│
├── app.py                # Main UI Router (Handles navigation and page views)
├── database.py           # SQLite connection pools, schema, and queries
├── premium.py            # Actuarial rule-based calculation module
├── auth.py               # Hashing, role authorization, and state controls
├── pdf_report.py         # ReportLab PDF template builder
├── config.py             # Global CSS style parameters and text content
├── setup_folders.py      # Folder initializer and mock assets generator
│
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore exclusions
│
├── insurance.db          # SQLite Database (generated on first execution)
│
├── assets/               # Branding graphics (logo, banners, icons)
├── reports/              # Generated PDF premium quotes
├── screenshots/          # Repository visual guides
└── docs/                 # Documentation and thesis files
🗄️ Database Overview
The relational SQLite database (insurance.db) consists of three structured tables:

users: Stores user profiles, credentials (password hashes), geographical details (city, state), and system access roles (user or admin).
premium_history: Main database tracking logs of premium assessments. Records health inputs, policy choices, calculation date/time, total premiums, and calculated risk indicators.
insurance_plans: Seeds the application's plans:
Basic Plan: ₹500,000 cover, 90% hospitalization coverage, base price ₹5,000.
Silver Plan: ₹1,000,000 cover, 100% hospitalization coverage, base price ₹10,000.
Gold Plan: ₹2,000,000 cover, 100% hospitalization coverage, base price ₹18,000.
🧮 Rule-Based Premium Calculation Engine
Surcharges and discounts are applied incrementally based on medical risks and lifestyle choices:

Actuarial Calculation Rules
Surcharge / Discount Category	Condition	Impact on Premium
Base Price	Plan: Basic / Silver / Gold	₹5,000 / ₹10,000 / ₹18,000
Age Surcharge	<25 / 25-35 / 36-45 / 46-55 / 56-65 / >65	+0% / +10% / +25% / +50% / +75% / +100%
BMI Surcharge	Underweight (<18.5) / Overweight (25-29.9) / Obese (>=30)	+5% / +10% / +25%
Medical Conditions	High Blood Pressure (Systolic > 140 or Diastolic > 90)	+15%
Diabetes	+20%
Heart Disease	+40%
Previous Surgery	+10%
Lifestyle Surcharges	Active Smoker	+30%
Alcohol Consumption (Regular)	+15%
Inadequate Sleep (< 6 hours daily)	+10%
High-Risk Occupations (e.g., Mining, Aviation, Construction)	+15%
Family Coverage	Per Additional Family Member	+30%
Active Lifestyle	Regular Exercise (Moderate / Regular)	-5% (Discount)
Loyalty Program	Has Existing Insurance	-5% (Discount)
Term Commitment	Policy Duration: 2 Years / 3 Years	-5% / -10% (Discount)
🖼️ Screenshots
(Visual documentation will be added here upon completion of user interface rendering)

Placeholder: User Dashboard View
Placeholder: Calculator Flow Step-by-Step
Placeholder: Admin Analytics Control Panel
Placeholder: Sample PDF Quotation Receipt
🛠️ Installation Guide
Follow these steps to set up and run the application locally.

Step 1: Clone the Repository
bash

git clone https://github.com/PallaviDewangan/Health_Insurance_Tech.git
cd Health_Insurance_Tech
Step 2: Establish a Virtual Environment
powershell

# Create virtual environment
python -m venv venv
# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
Step 3: Install Required Dependencies
bash

pip install -r requirements.txt
Step 4: Run Initial Directories Setup
bash

python setup_folders.py
🚀 How to Run the Project
Launch the local web server using Streamlit:

bash

streamlit run app.py
Open http://localhost:8501 in your browser.

🔄 Project Workflow

[ Landing Page ]
     │ (Fixed Navbar with Home, FAQ, About Us, Contact Us)
     ▼
[ Register / Login ] ── (SHA-256 Verification & Role Checking)
     │
     ├──► [ Registered User Role ]
     │        │
     │        ├──► [ User Dashboard ] (Metrics, Current Plans, BMI statuses)
     │        ├──► [ Premium Calculator ] (Multi-section form: Input parameters)
     │        ├──► [ Result View ] (Matplotlib Breakdown Chart, dynamic feedback)
     │        ├──► [ Profile Settings ] (Information updates, Password change)
     │        └──► [ PDF Quote Download ] (Printable, styled quotation report)
     │
     └──► [ Administrator Role ]
              │
              ├──► [ Admin Dashboard ] (Total users, average premiums, popular plans)
              ├──► [ User Management ] (CRUD operations: search, edit, delete users)
              ├──► [ Analytics Panel ] (Risk distribution pie-charts, calculation trends)
              └──► [ Data Exporter ] (Export all records to CSV format)
🔮 Future Scope
AI-Based Premium Prediction: Enhance calculations by training machine learning models (e.g., Random Forest or Gradient Boosting) on historical claims databases to estimate premium adjustments.
Email Notifications: Automatically send PDF quotes and policy updates to users' emails using SMTP integrations.
SMS Alerts: Send instant authentication codes (OTPs) and premium renewal reminders to users via SMS gateways.
Cloud Deployment: Host the application and database securely on AWS (using ECS/RDS) or Microsoft Azure.
Google Maps Hospital Locator: Integrate Maps API to show dynamic cashless network hospital listings nearby.
Payment Gateway Integration: Sandbox billing modules (Razorpay/Stripe) to allow immediate policy purchasing.
Mobile Application: Port layout structures to React Native or Flutter for Android and iOS systems.
Admin Rule Management: Add an admin portal panel allowing configuration of actuarial rules without editing code.
OCR-Based Document Upload: Enable uploading checkup papers and scanning variables using optical character recognition (OCR) models.
Multi-language Support: Support localization (e.g., English, Hindi) for wider consumer accessibility.
🔒 Security Features
Salted Hashing: Password strings are never stored in raw text; passwords are saved as salted SHA-256 hashes.
SQL Injection Prevention: Relational transactions use parameterization to avoid SQL manipulation.
Navigation Role-Guards: User session checking prevents unauthenticated or regular users from viewing admin pages.
Form Verification: Enforces boundary criteria (e.g., Age ranges, positive Height/Weight metrics, correct BP readings).
📄 License
This project is licensed under the MIT License - see the 
LICENSE
 file for details.

👥 Author
Pallavi Dewangan

B.Tech CSE (Artificial Intelligence)
Shri Shankaracharya Institute of Professional Management and Technology
Raipur, Chhattisgarh, India
GitHub: @PallaviDewangan
⚠️ Disclaimer
WARNING

This project is developed for educational purposes as a B.Tech Final Year Major Project. Premium values are generated using predefined rule-based logic and should not be considered official insurance quotations.