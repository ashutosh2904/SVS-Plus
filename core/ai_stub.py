# core/ai_stub.py

def generate_prompt(service, version):
    prompt = (
        f"You're a cybersecurity expert.\n"
        f"Explain the known vulnerabilities and risks of the following service:\n"
        f"Service: {service}\n"
        f"Version: {version}\n"
        f"Also suggest 1–2 possible mitigations if known vulnerabilities exist.\n"
    )
    return prompt
