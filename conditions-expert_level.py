# DevOps Scenario (Expert)

# disk_usage = -5
# TASK (Expert)
# Write a script that:
# • If disk usage is less than O OR greater than 100 → print "Invalid disk data"
# • Else if > 80 → "Disk CRITICAL"
# • Else if 60-80 → "Disk WARNING"
# • Else → "Disk OK"
# A Rules:
# • Order matters
# • Must be safe for production
# • No loops
disk_usage = -5

if disk_usage < 0 or disk_usage > 100:
    print("Invalid disk data")
elif disk_usage > 80:
    print("Disk Critical")
elif 60 <= disk_usage <= 80:
    print("Disk Warning")
else:
    print("Disk OK")