from datetime import datetime

with open("daily_log.txt", "w") as f:
    f.write(f"Last run at: {datetime.utcnow().isoformat()} UTC\n")
