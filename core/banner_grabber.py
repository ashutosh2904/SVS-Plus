import socket

def grab_banner(ip, port, timeout=1):
    try:
        # Create socket and set timeout
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))

        # Try to receive banner
        banner = s.recv(1024).decode().strip()
        s.close()

        if banner:
            return banner
        else:
            return "No banner received"

    except socket.timeout:
        return "Timed out"
    except Exception as e:
        return f"Error: {str(e)}"
