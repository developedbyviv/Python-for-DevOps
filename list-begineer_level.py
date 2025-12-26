# You want to verify running services on a server.

# services = ["nginx"
# , "ssh"
# , "docker"]
# TASK (Beginner - Lists)
# Write a script that:
# • If "docker" is in the list → print "Docker is running"
# • Else → print "Docker is NOT running"
# / Rules:
# • Use list + if
# • No loops
# • Simple logic

services = ["nginx"
, "ssh"
, "docker"]

if "docker" in services:
    print("Docker is running")
else:
    print("Docker is not running")


