# Scenario
# A dictionary stores service → status.
# python
# services = {
# "nginx": "running"
# "ssh"
# :
# "running"
# }
# TASK
# Write a Python script that:
# 1. Checks if "docker" exists as a key in the dictionary
# 2. If it does not exist, add "docker" with value "running"
# 3. Print the updated dictionary
# RULES
# • X No loops
# • X No functions
# • X No try/except
# • V Use if, dictionary membership (in), and assignment
services = {"nginx": "running","ssh":"running"}

if "docker" not in services:
    services["docker"] = "running"

print(services)
