# Failed Login Log Parser (Python)

A Python script to scan authentication logs for failed SSH login attempts and extract suspicious IP addresses.

## How It Works

- Reads a Linux-style auth log file (in this project it read '/var/log/auth.log')
- Identifies lines with 'Failed password'
- Extracts and prints source IPs using regex

## Sample Output

[!] Failed login attempt from IP: 192.168.1.5
[!] Failed login attempt from IP: 203.0.113.99
[!] Failed login attempt from IP:10.0.0.12

## Lessons Learned

- Python file handling
- Regular expressions for log parsing
- Brute-force login detection logic
- Basics of Linux authentication logging

## How to Run

```bash
python3 log_parser.py
