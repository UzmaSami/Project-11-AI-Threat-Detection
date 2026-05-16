import datetime

def send_alert(log_entry, threat_score):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"""
    ========================================
     SECURITY ALERT
    ========================================
    Time      : {timestamp}
    Log Entry : {log_entry}
    Threat Score: {threat_score}
    Action    : Immediate investigation required!
    ========================================
    """)

# Test alert
if __name__ == "__main__":
    send_alert(
        log_entry="IP: 172.16.0.1 | Failed Logins: 30 | Bytes: 999999",
        threat_score="HIGH"
    )