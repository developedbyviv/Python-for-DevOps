# 🧩 Problem 3: Immutable Config Values (tuple)

# Scenario:
# Ports that should never change.
# allowed_ports = (22, 80, 443)
# Tasks:
# 	•	Check if port 3306 is allowed
# 	•	Print all allowed ports
# 	•	Explain why tuple is better than list here

allowed_ports = (22, 80, 443)
if 3306 in allowed_ports:
    print("Yes port 3306 is in allowed Ports")
else:
    print("No port 3306 is in allowed Ports")

print(allowed_ports)

