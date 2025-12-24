# DevOps Scenario (Realistic)

# disk_usage = 65
# TASK (Intermediate)
# Write a script that:
# • If disk usage > 80 → "Disk CRITICAL"
# • If disk usage between 60 and 80 (inclusive) → "Disk WARNING"
# • Else → "Disk OK"
# Rules:
# • Use if / elif / else
# • Be explicit with conditions
# • No loops

disk_usage = 65

if disk_usage > 80:
    print("DISK CRITICAL")
elif 60 <= disk_usage <= 80:
    print("Disk WARNING")
else:
    print("Disk OK")