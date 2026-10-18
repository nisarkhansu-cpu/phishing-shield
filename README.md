# 🛡️ Phishing-Shield Enterprise - 4-in-1 SOC Tool

> An automated Threat Intelligence tool for Security Operations Centers (SOC) - Built with Python

**Live Demo:** This tool successfully detects phishing like `faceb00k-login`, IP based URLs, and `.tk` domains.

### 🚀 Key Features (4-in-1)

**1. Email Leak Checker:** Checks if an email exists in known breach databases
**2. Heuristic Phishing Engine:** 5-rule detection engine
   - IP Address Check
   - @ Symbol Trick
   - Suspicious TLD (.tk, .ml, .ga, .cf)
   - Excessive Hyphens
   - Typo-squatting (faceb00k, g00gle)
**3. Domain Age Analyzer:** Flags newly created domains which are 99% likely to be phishing
**4. Executive Dashboard:** Auto-generates a colorful, formatted 3-sheet Excel report with Risk Score (0-9)

### 📸 Screenshots
Add your report.xlsx screenshots here. Our engine shows:
- `google.com` -> SAFE
- `faceb00k-login-security.com` -> PHISHING
- `192.168.1.1/secure-login` -> PHISHING

### 🛠️ Tech Stack
- Python, Pandas, OpenPyXL, Regex

### ⚙️ How to Run
```bash
pip install pandas openpyxl
python app.py
