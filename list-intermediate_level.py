# Now we raise the difficulty slightly.
# DevOps Scenario (Realistic)

# services = ["nginx", "ssh"]
# TASK (Intermediate - Lists)
# Write a script that:
# • If "docker" is not in the list → add it
# • Print the updated services list
# ! Rules:
# • Use list methods
# • Use if
# • No loops

services = ["nginx", "ssh"]

if "docker" in services:
    print("docker already is in list")
else:
    services.append("docker")

# print(services)