# 🧩 Problem 7: Backup Validation (list + if)

# Scenario:
# Backup files found on server.
# backups = ["db_backup_01.sql", "db_backup_02.sql"]
# Tasks:
# 	•	If list is empty → "Backup missing!"
# 	•	Else → "Backup available"
# 	•	Print number of backups

backups = ["db_backup_01.sql", "db_backup_02.sql"]

if not backups:
    print("Backups not available!")
else:
    print(f"Backup Available! and having {len(backups)} backups.")