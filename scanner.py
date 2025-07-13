import socket
from datetime import datetime
from utils import extract_version_info, is_vulnerable
from banner_grabber import grab_banner
from colorama import Fore, Style, init
from reporter import write_txt_report, write_json_report
import argparse
from html_reporter import write_html_report
from ai_stub import generate_prompt
from collections import Counter
from utils import extract_version_info, is_vulnerable, severity_rank, count_severity_levels, get_emoji_for_severity

init(autoreset=True)

# 🎯 Parse CLI arguments like --ip, --ports, --output
def parse_arguments():
    parser = argparse.ArgumentParser(description="Smart Vulnerability Scanner Plus")
    parser.add_argument('--ip', required=True, help='Target IP address or domain')
    parser.add_argument('--ports', default='1-1024', help='Port range to scan (e.g., 20-100)')
    parser.add_argument('--output', default='console', choices=['console', 'txt', 'json', 'html'], help='Output format')
    parser.add_argument('--ai-mode', action='store_true', help='Enable AI analysis stub')

    return parser.parse_args()

if __name__ == "__main__":
    # 📦 Get CLI arguments
    args = parse_arguments()
    target_ip = args.ip
    ai_mode = args.ai_mode
    port_range = args.ports
    output_format = args.output

    # ⛔ Validate port range
    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        print("❌ Invalid port range format. Use format like 20-80.")
        exit(1)

    # 🧾 Header Info
    print("=" * 50)
    print("  SVS+ Port Scanner - Phase 1")
    print("=" * 50)
    print(f"\n🔍 Scanning Target: {target_ip}")
    print(f"📦 Port Range: {start_port} to {end_port}")
    print(f"📄 Output Format: {output_format}\n")

    # 🧠 Initialize scan results list
    scan_results = []

    # ⏱️ Start timer
    start_time = datetime.now()

    # 🔁 Loop through all ports in given range
    for port in range(start_port, end_port + 1):
        try:
            # 🔌 Create socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))

            # ✅ If port is open
            if result == 0:
                print(f"\n{Fore.GREEN}✅ Port {port} is OPEN")

                # 📜 Grab service banner
                banner = grab_banner(target_ip, port)

                # 🟡 Print banner output
                if "No banner" in banner or "Timed out" in banner:
                    print(f"{Fore.YELLOW}📜 Banner: {banner}")
                elif "Error" in banner:
                    print(f"{Fore.RED}📜 Banner: {banner}")
                else:
                    print(f"{Fore.CYAN}📜 Banner: {banner}")

                # 🔍 Extract version info and check vulnerability severity
                service, version = extract_version_info(banner)
                severity = None

                if service and version:
                    print(f"{Fore.MAGENTA}🔎 Detected Service: {service}, Version: {version}")
                    severity = is_vulnerable(service, version)

                    # ⚠️ Print vulnerability status
                    if severity:
                        emoji = {"high": "🔴", "medium": "🟠", "low": "🟡"}.get(severity, "⚠️")
                        color = {"high": Fore.RED, "medium": Fore.YELLOW, "low": Fore.CYAN}.get(severity, Fore.MAGENTA)
                        print(f"{color}{emoji} VULNERABLE: {service} {version} → Severity: {severity.upper()}")

                # 📝 Store result in list
                scan_results.append({
                    "port": port,
                    "status": "open",
                    "banner": banner,
                    "service": service,
                    "version": version,
                    "vulnerable": bool(severity),
                    "severity": severity
                })

            # 🔒 Close socket
            s.close()

        except KeyboardInterrupt:
            print("\n⛔ Scan aborted by user.")
            break
        except socket.gaierror:
            print("❌ Hostname could not be resolved.")
            break
        except socket.error:
            print("❌ Could not connect to server.")
            break

    # 🕔 Calculate total time
    end_time = datetime.now()
    total_time = end_time - start_time

    # 🔢 Sort results by severity (high → low → none)
    scan_results.sort(key=severity_rank, reverse=True)

    # 📊 Count vulnerabilities by severity
    severity_counter = count_severity_levels(scan_results)


    # ✅ Final output
    print(f"\n✅ Scan completed in {total_time}")
    print(f"📊 Total Open Ports: {len(scan_results)}")

    # 🔐 Print vulnerability summary
    print(f"\n🔐 Vulnerability Summary:")
    for level in ["high", "medium", "low"]:
        count = severity_counter.get(level, 0)
        if count > 0:
            emoji = get_emoji_for_severity(level)
            print(f"  {emoji} {level.title()} Severity: {count}")
    if sum(severity_counter.values()) == 0:
        print("  ✅ No known vulnerabilities detected.")

    # 📤 Export report
    if output_format == "json":
        write_json_report(scan_results, target_ip)
    elif output_format == "txt":
        write_txt_report(scan_results, target_ip)
    elif output_format == "html":
        write_html_report(scan_results, target_ip)
    else:
        print("🖥️ Console-only mode selected. No report saved.")

        # 🤖 AI mode logic (stub)
    if ai_mode:
        print("\n🤖 AI Mode Activated – preparing AI prompts...\n")
        for item in scan_results:
            if item['vulnerable'] and item['service'] and item['version']:
                prompt = generate_prompt(item['service'], item['version'])
                print(f"{Fore.CYAN}🧠 Prompt for AI:\n{prompt}")
                print(f"{'-'*40}")
