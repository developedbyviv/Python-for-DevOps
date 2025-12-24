# 🧩 Problem 6: Deployment Decision Logic (if + dict)

# Scenario:
# Deployment rules.
# deployment = {
#     "branch": "main",
#     "tests_passed": True,
#     "approved": False
# }
# Task:
# Deploy only if:
# 	•	branch is "main"
# 	•	tests_passed is True
# 	•	approved is True

# Else print why deployment failed.


deployment = {
    "branch": "main",
    "tests_passed": True,
    "approved": False
}

if(
    deployment["branch"] == "main"
    and deployment["tests_passed"] == True
    and deployment["approved"] == True
):
    print("Deployment Started!")
else:
    print("Deployment Blocked")
    if deployment["branch"] != "main":
        print("- Reason: branch is not main")
    if not deployment["tests_passed"]:
        print("- Reason: tests did not passed")
    if not deployment["approved"]:
        print("Reason: deployment did not approved")
