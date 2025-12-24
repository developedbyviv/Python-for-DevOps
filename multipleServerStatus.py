# 🧩 Problem 5: Multiple Server Status (list + dict + if)

# Scenario:
# You manage multiple servers.
# servers = [
#     {"name": "web-1", "cpu": 45},
#     {"name": "web-2", "cpu": 82},
#     {"name": "db-1", "cpu": 65}
# ]
# Tasks:
# 	•	Loop through servers
# 	•	Print server name and status:
# 	•	CPU > 80 → CRITICAL
# 	•	CPU 50–80 → WARNING
# 	•	else → OK

servers = [
    {"name": "web-1", "cpu": 45},
    {"name": "web-2", "cpu": 82},
    {"name": "db-1", "cpu": 65}
]

for server in servers:
    name = server["name"]
    cpu = server["cpu"]

    if cpu > 80:
        status = "CRITICAL"
    elif 50 <= cpu <=80:
        status = "WARNING"
    else:
        status = "OK"

    print(f"Server: {name} | CPU: {cpu}% | Status: {status}")