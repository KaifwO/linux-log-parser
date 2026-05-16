import re
from collections import defaultdict

FAILED_PATTERN = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

def analyze_ssh(log_lines, threshold):
    attempts = defaultdict(int)

    for line in log_lines:
        match = FAILED_PATTERN.search(line)
        if match:
            ip = match.group(1)
            attempts[ip] += 1

    alerts = {
        ip: count
        for ip, count in attempts.items()
        if count >= threshold
    }

    return attempts, alerts