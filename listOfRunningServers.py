# Scenario:
# You have services running on a server.

# services = ["nginx", "docker", "ssh", "cron"]

# Tasks:
# 	1.	Print all services
# 	2.	Check if "docker" is running
# 	3.	Add "redis" to the list
# 	4.	Remove "cron"

services = ["nginx", "docker", "ssh", "cron"]

for i in services:
    print(i)

if "docker" in services:
    print(f"Yes! docker is running")
else:
    print(f"No! docker is running")

services.append("redis")
print(services)
services.remove("cron")
print(services)