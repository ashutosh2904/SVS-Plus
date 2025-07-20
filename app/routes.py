from flask import Blueprint, render_template, request
import socket
from core.banner_grabber import grab_banner
from core.utils import (
    extract_version_info, is_vulnerable,
    severity_rank, count_severity_levels, get_emoji_for_severity
)
from core.reporter import write_txt_report, write_json_report
from core.html_reporter import write_html_report
from core.ai_stub import generate_prompt
from core.screenshot import take_screenshot

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    results = []
    summary = {}
    error = None
    prompts = []

    if request.method == "POST":
        # Get form inputs
        target_ip = request.form.get("ip")
        port_range = request.form.get("ports", "1-1024")
        output = request.form.get("output", "console")
        ai_mode = request.form.get("ai-mode") == "on"

        # Validate IP
        if not target_ip:
            error = "Target IP is required."
            return render_template("index.html", error=error)

        # Validate port range
        try:
            start_port, end_port = map(int, port_range.split("-"))
        except:
            error = "Invalid port range format. Use something like 20-80."
            return render_template("index.html", error=error)

        # Begin scanning
        for port in range(start_port, end_port + 1):
            try:
                s = socket.socket()
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))

                if result == 0:
                    banner = grab_banner(target_ip, port)
                    service, version = extract_version_info(banner)
                    severity = is_vulnerable(service, version)

                    result_data = {
                        "port": port,
                        "banner": banner,
                        "service": service,
                        "version": version,
                        "vulnerable": bool(severity),
                        "severity": severity
                    }

                    results.append(result_data)

                    # Generate AI prompt (stub)
                    if ai_mode and service and version and severity:
                        prompt = generate_prompt(service, version)
                        result_data["prompt"] = prompt
                        prompts.append(prompt)

                s.close()

            except Exception as e:
                continue  # silently skip to next port

        # Sort and summarize
        results.sort(key=severity_rank, reverse=True)
        summary = count_severity_levels(results)

        # Save report if results found
        if output == "json":
            write_json_report(results, target_ip)
        elif output == "txt":
            write_txt_report(results, target_ip)
        elif output == "html":
            write_html_report(results, target_ip)
            if request.form.get("save-screenshot") == "on":
                take_screenshot("reports/svs_report_latest.html")


    return render_template("index.html", results=results, summary=summary, error=error, prompts=prompts)
