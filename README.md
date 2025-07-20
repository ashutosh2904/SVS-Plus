# VulnForge 🔨 – A Smart Vulnerability Scanner Engine

A Python-based vulnerability scanner that detects open ports, grabs banners, identifies services and versions, and checks against known vulnerabilities — complete with AI-mode stubs, HTML/JSON/TXT report export, and a clean Flask web UI!

> 🚀 Built with ❤️ by **Ashutosh Choudhary** – aspiring cybersecurity engineer

---

## 🌟 Features

- 🔍 **Fast Port Scanning** (custom port range)
- 📡 **Banner Grabbing** from services (FTP, SSH, HTTP, etc.)
- 🔎 **Service & Version Detection**
- ⚠️ **Vulnerability Severity Mapping** – _High / Medium / Low_
- 🧠 **AI Mode Stub** – designed for GPT integration in future
- 📤 **Report Export** – TXT, JSON, HTML
- 🌐 **Flask Web Interface** – Clean UI built with Bulma CSS
- 🖼️ **HTML Screenshot Capture** – Selenium-based visual reports
- 🎨 **Beautiful Console Output** – Color-coded CLI display

---

## 🛠️ Installation

```bash
git clone https://github.com/ashutosh2904/SVS-Plus.git
cd SVS-Plus
python -m venv venv
source venv/Scripts/activate      # On Windows (use 'source venv/bin/activate' on Linux/Mac)
pip install -r requirements.txt

**************************

#🧪 USAGE (CLI MODE)
# 🔹 Basic scan (default ports 1–1024, console output)
python core/scanner.py --ip scanme.nmap.org

# 🔹 Custom port range + export format
python core/scanner.py --ip scanme.nmap.org --ports 20-80 --output json

# 🔹 Save HTML report
python core/scanner.py --ip scanme.nmap.org --ports 20-80 --output html

# 🔹 Enable AI prompt stub
python core/scanner.py --ip scanme.nmap.org --ai-mode

**************************

# 🌐 TO USE WEB APP
# 📦 Run Flask Web Server

       [python run.py]

Open your browser and navigate to:
http://127.0.0.1:5000

Features in the web UI:

Form to enter IP & ports

Selectable output format (console, txt, json, html)

Optional AI mode

Optional screenshot saving

Beautifully formatted results & summary


**************************

#📁 Folder Structure

SVS-Plus/
├── app/                      # 🔹 Flask app logic
│   ├── __init__.py
│   └── routes.py
├── core/
│   ├── scanner.py           # 🔹 CLI scanner logic
│   ├── utils.py             # 🔹 Banner parsing + vulnerability check
│   ├── reporter.py          # 🔹 TXT + JSON export
│   ├── html_reporter.py     # 🔹 HTML report builder
│   ├── ai_stub.py           # 🔹 Prompt generator stub
│   ├── banner_grabber.py    # 🔹 Banner grabbing logic
│   ├── screenshot.py        # 🔹 Selenium screenshot capture
│   └── version_db.json      # 🔹 Known vulnerable services
├── reports/                 # 📝 Auto-generated reports
├── screenshots/             # 🖼️ HTML report screenshots
├── templates/               # 🖥️ Flask HTML templates (index.html)
├── static/                  # 📁 (optional) custom CSS/assets
├── run.py                   # 🚀 Web app entry point
├── requirements.txt         # 📦 Dependencies
├── .gitignore
└── README.md

**************************

📜 License
Free to use, share, and learn from 🔓
⚠️ Never scan unauthorized networks or targets. Always stay ethical.

✍️ Author
Ashutosh Choudhary
🧑‍💻 B.Tech CSE | Cybersecurity Learner | Tool Builder