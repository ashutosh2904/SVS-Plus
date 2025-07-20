# 🔐 SVS+ – Smart Vulnerability Scanner Plus

A Python-based CLI tool that scans open ports, grabs banners, detects service versions, and checks for known vulnerabilities — with AI-mode stubs and HTML/JSON/TXT report export.

> 🚀 Built with ❤️ by Ashutosh Choudhary – aspiring cybersecurity engineer

---

## 🚀 Features

- 🔍 Port scanning using TCP sockets
- 📜 Banner grabbing from services (FTP, SSH, HTTP, etc.)
- 🔎 Version & service extraction
- ⚠️ Vulnerability severity tagging: **High / Medium / Low**
- 📤 Exports results to **TXT**, **JSON**, and **HTML**
- 🧠 AI Mode stub for future GPT/LLM integration
- 📊 Console-friendly output with colored formatting

---

## 🛠️ Installation

```bash
git clone https://github.com/ashutosh2904/SVS-Plus.git
cd SVS-Plus
pip install -r requirements.txt


# 🖥️ Usage

# Basic scan (default ports 1–1024, console output)
python core/scanner.py --ip scanme.nmap.org

# Custom port range and export format
python core/scanner.py --ip scanme.nmap.org --ports 20-80 --output json

# Save HTML report
python core/scanner.py --ip scanme.nmap.org --ports 20-80 --output html

# Enable AI stub mode
python core/scanner.py --ip scanme.nmap.org --ai-mode

#📁 Folder Structure

SVS-Plus/
├── core/
│   ├── scanner.py           ← Main CLI scanner
│   ├── utils.py             ← Banner parsing + severity logic
│   ├── reporter.py          ← TXT + JSON report export
│   ├── html_reporter.py     ← HTML report builder
│   ├── ai_stub.py           ← AI prompt generator (stub only)
│   ├── banner_grabber.py    ← Banner extraction logic
│   └── version_db.json      ← Known vulnerable versions DB
├── reports/                 ← Auto-generated reports
├── screenshots/             ← Screenshots for README
├── requirements.txt         ← Python dependencies
├── README.md
└── .gitignore

#📜 License
free to use, share, and learn from 🔓
Just don’t use this scanner on unauthorized networks. 💻⚖️

#✍️ Author
Ashutosh Choudhary
🧑‍💻 B.Tech CSE | Cybersecurity Learner |
