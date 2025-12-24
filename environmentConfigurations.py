# 🧩 Problem 4: Environment Configuration (dictionary)

# Scenario:
# Application environment variables.env_config = {
#     "ENV": "production",
#     "DEBUG": False,
#     "VERSION": "1.2.0"
# }
# Tasks:
# 	1.	Print all key-value pairs
# 	2.	Change version to "1.2.1"
# 	3.	Add "MAINTAINER": "DevOps Team"
# 	4.	If ENV is production, print "Deploy with caution"

# Application environment 
variables_env_config = {
    "ENV": "production",
    "DEBUG": False,
    "VERSION": "1.2.0"
}

# print(variables_env_config);

for key,value in variables_env_config.items():
    print(f"{key}: {value}")

variables_env_config["VERSION"] = "1.2.1";
variables_env_config["MAINTAINER"] = "DevOps Team"

if variables_env_config["ENV"] == "production":
    print("Deploy with caution")




