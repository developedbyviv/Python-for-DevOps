# Scenario
# A dictionary represents a server inventory, where:
# • Key → service name
# • Value → service state ("running" /"stopped")

# services = {
# "nginx": "running",
# "ssh": "running",
# "docker": "stopped",
# "redis": "running"
# }
# TASK
# Write a Python script that enforces the following rules:
# 1. "ssh" must always remain "running"
# 2. "docker" and "redis" must both be running, or both be stopped
# 3. If one of ("docker", "redis") is missing, add it with the same status as the other
# 4. Do not modify "nginx" under any condition
# 5. Print the final dictionary

# !RULES (VERY STRICT)
# • X No loops
# • X No functions
# • X No try/except
# • X No dictionary methods (update, setdefault, etc.)
# • X No copying the dictionary
# • X No hardcoding final dictionary
# • X No deleting keys
# • Only:
# • if / elif / else
# • dictionary membership (in)
# • direct key access
# • assignment

services = {
    "nginx": "running",
    "ssh": "running",
    "docker": "stopped",
    "redis": "running"
}

# Rule 1: ssh must always be running
if "ssh" in services:
    if services["ssh"] == "stopped":
        services["ssh"] = "running"

# Rule 2 & 3: docker and redis must be aligned
if "docker" in services and "redis" in services:
    if services["docker"] != services["redis"]:
        services["docker"] = services["redis"]
elif "docker" in services and "redis" not in services:
    services["redis"] = services["docker"]
elif "redis" in services and "docker" not in services:
    services["docker"] = services["redis"]

print(services)