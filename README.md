# Linux SSH Brute Force Analyzer (V2)

## Description

Simple Python tool that analyzes Linux SSH logs to detect brute force attempts.

This is a **file-based analyzer**:

it reads an existing log file (local or copied from a server)
it does NOT perform live monitoring or remote collection

---

##  Features

- Parses SSH authentication logs
- Detects failed login attempts
- Groups attacks by IP address
- Configurable threshold for brute force detection
- Generates JSON report

---

## Usage :

python main.py
