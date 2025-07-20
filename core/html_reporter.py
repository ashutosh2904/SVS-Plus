# core/html_reporter.py
import os
from datetime import datetime

def get_html_report_path():
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"reports/svs_report_{timestamp}.html"

def write_html_report(results, target_ip):
    path = get_html_report_path()
    scanned_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ✅ Use this once
    with open(path, "w") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>SVS+ HTML Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f9f9f9; padding: 20px; }}
        h1 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .high {{ background-color: #ffcccc; }}
        .medium {{ background-color: #fff0b3; }}
        .low {{ background-color: #d6f5d6; }}
        .none {{ background-color: #eee; }}
    </style>
</head>
<body>
    <h1>SVS+ Scan Report</h1>
    <p><strong>Target:</strong> {target_ip}</p>
    <p><strong>Scanned At:</strong> {scanned_at}</p>
    <table>
        <tr>
            <th>Port</th>
            <th>Banner</th>
            <th>Service</th>
            <th>Version</th>
            <th>Severity</th>
        </tr>
""")
        for item in results:
            sev = item.get("severity")
            row_class = sev if sev else "none"
            f.write(f"""
        <tr class="{row_class}">
            <td>{item['port']}</td>
            <td>{item['banner']}</td>
            <td>{item['service'] or '-'}</td>
            <td>{item['version'] or '-'}</td>
            <td>{sev.upper() if sev else 'None'}</td>
        </tr>
""")
        f.write("""
    </table>
</body>
</html>
""")
    print(f"🌐 HTML report saved to: {path}")
