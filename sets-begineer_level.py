# Scenario
# You are managing server access control.
# • One set represents users who SHOULD have access
# • Another set represents users who CURRENTLY have access
# python
# required _users = {"root", "ubuntu", "devops"
# , "ci"}
# current_users = {"root"
# , "ubuntu", "intern"
# ', "temp" }
# TASK
# Write a Python script that:
# 1. Determines which users must be added to the server
# 2. Determines which users must be removed from the server
# 3. Prints:
# • Users to add
# • Users to remove
# !RULES (VERY STRICT)
# 	•	❌ No loops
# 	•	❌ No functions
# 	•	❌ No list/tuple conversion
# 	•	❌ No dictionary usage
# 	•	❌ No copying sets
# 	•	❌ No manual element-by-element checks
# 	•	❌ No try/except
# 	•	✅ Only:
# 	•	set operations
# 	•	assignment
# 	•	print()
required_users = {"root", "ubuntu", "devops", "ci"}
current_users = {"root", "ubuntu", "intern", "temp" }

