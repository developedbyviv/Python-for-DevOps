# Scenario
# A tuple stores allowed deployment environments.

# environments = ("dev"
# "stage")
# TASK
# Write a Python script that:
# 1. Checks if "prod" is present in the tuple
# 2. If not present, add "prod"
# 3. Print the updated tuple
# !RULES
# • X No loops
# • X No list conversion
# • V Use tuple operations + if

environments = ("dev",
"stage")

# if "prod" in environments:
#     print("prod is available")
# else:
#     environments = environments + ("prod",)

if "prod" not in environments:
    environments = environments + ("prod",)

print(environments)