import pandas as pd
import pickle
import datetime

# Load model
print("[*] Loading threat detection model...")
with open('models/threat_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Simulate real-time log entries
new_logs = pd.DataFrame({
    'failed_logins':      [0, 25, 1, 30],
    'bytes_transferred':  [400, 100, 500, 999999]
})

print("[*] Analyzing logs for threats...\n")

predictions = model.predict(new_logs)

for i, (pred, row) in enumerate(zip(predictions, new_logs.itertuples())):
    status = "🚨 THREAT DETECTED" if pred == 1 else "✅ Normal"
    print(f"Log Entry {i+1}: Failed Logins={row.failed_logins}, "
          f"Bytes={row.bytes_transferred} --> {status}")

print("\n[+] Threat detection complete.")