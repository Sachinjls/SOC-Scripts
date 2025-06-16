# failed_ssh_counter.py

# File path (adjust if different)
log_path = "/var/log/auth.log"

# What we're looking for
search_text = "Failed password"

# Counter variable
fail_count = 0

try:
    with open(log_path, "r") as f:
        for line in f:
            if search_text in line:
                fail_count += 1

    print(f"🔐 Total failed SSH login attempts: {fail_count}")

except FileNotFoundError:
    print(f"[!] Log file not found: {log_path}")
