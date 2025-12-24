# You are writing a server health check script.

# disk_usage = 85
# TASK (Beginner)
# Write a Python script that:
# • If disk usage is more than 80 → print "Disk CRITICAL"
# • Else → print "Disk OK"
# A Rules:
# • Use only if / else
# • No loops
# • No advanced logic

disk_usage = 85

if disk_usage > 80:
    print("DISK CRITICAL")
else:
    print("Disk OK")
