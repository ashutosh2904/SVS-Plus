# core/reporter.py
import json
import os
from datetime import datetime

def get_report_path(format):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"reports/svs_report_{timestamp}.{format}"

def write_json_report(results, target_ip):
    path = get_report_path("json")
    data = {
        "target": target_ip,
        "scanned_at": datetime.now().isoformat(),
        "results": results
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"📤 JSON report saved to: {path}")

def write_txt_report(results, target_ip):
    path = get_report_path("txt")
    with open(path, "w") as f:
        f.write(f"SVS+ Scan Report for {target_ip}\n")
        f.write("=" * 50 + "\n")
        for item in results:
            f.write(f"Port {item['port']} is OPEN\n")
            f.write(f"Banner: {item['banner']}\n")
            if item['service'] and item['version']:
                f.write(f"Service: {item['service']} | Version: {item['version']}\n")
            if item['vulnerable']:
                f.write("!!! VULNERABLE VERSION DETECTED !!!\n")
                if item['severity']:
                    severity = item['severity'].upper()
                    f.write(f"Severity: {severity}\n")
            f.write("-" * 40 + "\n")
    print(f"📤 TXT report saved to: {path}")
