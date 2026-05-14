# Linux Log Parser (SSH Brute Force Detector)

A simple Python tool that analyzes Linux SSH logs to detect potential brute force attacks.

## What this project does

This script reads a Linux SSH log file and:
- detects failed login attempts
- counts attempts per IP address
- flags suspicious IPs based on a threshold
- generates a JSON report

Goal: simulate a basic cybersecurity brute-force detection system.

## Configuration

The detection threshold is defined in `config.json`.

Example:

```json
{
  "failed_threshold": 2
}
```

If an IP fails to login 2 times or more → it triggers an alert.

## Usage 

```bash
python parser.py
```

## Output Console 

```
Analyse sécurité SSH :

ALERTE BRUTE FORCE : 192.168.1.10 → 2
OK : 192.168.1.30 → 1
```

## Output file

```json
[
  {
    "ip": "192.168.1.10",
    "attempts": 2,
    "status": "ALERTE BRUTE FORCE"
  },
  {
    "ip": "192.168.1.30",
    "attempts": 1,
    "status": "OK"
  }
]
```