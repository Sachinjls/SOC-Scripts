# SOC-Scripts
Trying to Know Real-world security tools for log parsing, IOC checks, automation
# 🛡️ SOC-Scripts by Sachin VRK

This repository contains real-world SOC (Security Operations Center) tools and scripts built by me to automate threat detection, log analysis, alerting, and incident response tasks.

---

## 📁 Folder Structure

```
SOC-Scripts/
├── Log-Analysis/
│   ├── parse_authlog.py             # Detect brute-force login attempts
│   └── logrotate_cleaner.sh         # Clean old rotated logs
├── Threat-Intel/
│   ├── vt_bulk_hash_check.py        # Bulk check hashes with VirusTotal API
│   └── ioc_feed_parser.py           # Parse external threat feeds (e.g., MISP)
├── Alert-Automation/
│   ├── elk_alert_to_slack.py        # Send ELK alerts to Slack
│   └── wazuh_to_discord.py          # Push Wazuh alerts to Discord
├── Incident-Response/
│   ├── usb_insert_logger.bat        # Log USB insertions on Windows
│   └── suspicious_user_alert.ps1    # Detect suspicious PowerShell users
├── README.md
└── .gitignore
```
