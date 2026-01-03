# Scenario
# A dictionary stores service → status for a server.

# services = {
# "nginx": "running",
# "ssh": "running",
# "docker": "stopped"}
# TASK
# Write a Python script that:
# 1. Checks if "docker" exists as a key
# 2. If it exists and its value is "stopped"
# ', change it to "running"
# 3. If "docker" does not exist, add it with value "running"
# 4. Print the updated dictionary
# !RULES (STRICT)
# • X No loops
# • X No functions
# • X No try/except
# • X No update()
# • X No copying dictionary
# •	✅ Use if, dictionary membership, and assignment only


services = {
"nginx": "running",
"ssh": "running",
"docker": "stopped"}

if "docker" in services:
    if services["docker"] == "stopped":
        services["docker"] = "running"
else:
    services["docker"] = "running"

print(services)

