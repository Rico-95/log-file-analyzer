import re

def extract_failed_logins(log_file):
    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    print(f"[!] Failed login attempt from IP: {ip}")

if __name__ == "__main__":
    log_path = input("Enter path to log file (e.g. sample_auth.log): ")
    extract_failed_logins(log_path)
