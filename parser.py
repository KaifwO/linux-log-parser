import json

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

threshold = config["failed_threshold"]

ips = {}

with open("sample.log", "r") as file:
    for line in file:
        if "sshd" in line and "failed" in line:
            parts = line.split()
            ip = parts[-1]

            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1

alerts = []

print("\nAnalyse sécurité SSH :\n")

for ip, count in ips.items():
    status = "OK"

    if count >= threshold:
        status = "ALERTE BRUTE FORCE"

    alerts.append({
        "ip": ip,
        "attempts": count,
        "status": status
    })

    print(status, ":", ip, "→", count)

with open("report.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("\nRapport exporté dans report.json")