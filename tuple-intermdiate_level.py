# TASK
# Write a Python script that:
# environments = ("dev", "prod")
# 1. Checks if " stage" exists in the tuple
# 2. If "stage" is missing, insert it between "dev" and "prod"
# 3. Print the updated tuple
# !RULES (Strict)
# • X No loops
# • X No list conversion
# • X No set
# • X No sorted ()
# • Only tuple slicing, tuple operations, and if

environments = ("dev", "prod")

if "stage" not in environments:
    # print(environments = environments[0:1] + ("stage",) + environments[1:])
   environments = environments[0:1] + ("stage",) + environments[1:]
   print(environments)