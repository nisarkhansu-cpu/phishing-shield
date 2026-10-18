import pandas as pd
import re
from datetime import datetime
from urllib.parse import urlparse
from openpyxl.styles import Font

def check_phishing(url):
    reasons=[]; score=0
    domain=urlparse(url).netloc.lower()
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        reasons.append("IP address"); score+=3
    if "@" in url:
        reasons.append("@ trick"); score+=3
    if domain.endswith(('.tk','.ml','.ga','.cf','.gq')):
        reasons.append("Suspicious TLD"); score+=3
    if url.count('-')>2:
        reasons.append("Many hyphens"); score+=2
    if any(x in url.lower() for x in ["faceb00k","g00gle","micros0ft"]):
        reasons.append("Typo-squatting"); score+=3
    if score>=3: return "PHISHING", ", ".join(reasons), score
    elif score>=1: return "SUSPICIOUS", ", ".join(reasons), score
    else: return "SAFE", "-", score

def check_domain_age(url):
    domain=urlparse(url).netloc
    if any(x in domain for x in ['.tk','.ml','.ga']): return "New / Suspicious"
    return "Old / Trusted"

print("=== V4.1 Fix Edition ===")
emails=pd.read_csv("emails.csv", header=None, names=["email"])
links=pd.read_csv("links.csv", header=None, names=["url"])

email_data=[[e, "LEAKED" if "test" in e else "SAFE", "Demo Breach" if "test" in e else "-", datetime.now().strftime("%Y-%m-%d")] for e in emails["email"]]
link_data=[]
for u in links["url"]:
    status,reason,score=check_phishing(str(u))
    age=check_domain_age(str(u))
    link_data.append([u,status,reason,age,score,datetime.now().strftime("%Y-%m-%d")])

email_report=pd.DataFrame(email_data, columns=["email","status","details","date"])
link_report=pd.DataFrame(link_data, columns=["url","status","reason","domain_age","risk_score","date"])

with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    email_report.to_excel(writer, sheet_name="Email_Leaks", index=False)
    link_report.to_excel(writer, sheet_name="Phishing_Links", index=False)
    pd.DataFrame([["Total Emails", len(email_report)], ["Total Links", len(link_report)], ["Phishing Found", len(link_report[link_report['status']=='PHISHING'])]]).to_excel(writer, sheet_name="Dashboard", index=False, header=False)
    
    # Auto column width fix
    for sheet in writer.sheets.values():
        for col in sheet.columns:
            max_len=max(len(str(cell.value)) if cell.value else 0 for cell in col)
            sheet.column_dimensions[col[0].column_letter].width = max_len + 4
        for cell in sheet[1]:
            cell.font=Font(bold=True)

print("✅ Fixed Report Ready! Ab ### nahi aayega, report clean hogi.")