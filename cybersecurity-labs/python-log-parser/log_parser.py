# Python Log Parser - Failed Login Detection

log_file = "sample_log.txt"

failed_attempts = 0
failed_users = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed login attempt" in line:
            failed_attempts += 1

            parts = line.split("user:")
            if len(parts) > 1:
                username = parts[1].strip()

                if username in failed_users:
                    failed_users[username] += 1
                else:
                    failed_users[username] = 1

print("===== Log Analysis Report =====")
print("Total Failed Login Attempts:", failed_attempts)
print("\nFailed Attempts by User:")

for user, count in failed_users.items():
    print(user, ":", count)
