import json
from parser import analyze_ssh

# load config
with open("config.json", "r") as f:
    config = json.load(f)

LOG_PATH = config["LOG_PATH"]
THRESHOLD = config["THRESHOLD"]

def read_log(path):
    with open(path, "r", errors="ignore") as f:
        return f.readlines()

def main():
    print("\nAnalyse sécurité SSH :\n")

    logs = read_log(LOG_PATH)

    attempts, alerts = analyze_ssh(logs, THRESHOLD)

    report = {
        "total_ips": len(attempts),
        "attempts": dict(attempts),
        "alerts": alerts
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Rapport exporté dans report.json\n")

    print("Top IPs :")
    for ip, count in sorted(attempts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} -> {count}")

    print("\nAlerts :")
    if alerts:
        for ip, count in alerts.items():
            print(f"[ALERT] {ip} ({count} attempts)")
    else:
        print("No brute force detected.")

if __name__ == "__main__":
    main()