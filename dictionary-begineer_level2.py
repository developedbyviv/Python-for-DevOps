# Scenario
# A dictionary stores environment → URL mappings.

# env_urls = {
# "dev":
# "dev. example.com",
# "prod": "example.com"
# }
# TASK
# Write a Python script that:
# 1. Checks if "stage" exists as a key in the dictionary
# 2. If it does not exist, add "stage" with value "stage. example.com"
# 3. Print the updated dictionary
# RULES
# • X No loops
# • X No functions
# • X No try/except
# • X No dictionary methods like update()
# Use if, dictionary membership (in), and assignment

env_urls = {
"dev": "dev.example.com",
"prod": "example.com"
}

if "stage" not in env_urls:
    env_urls["stage"] = "stage.example.com"

print(env_urls)