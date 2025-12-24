# Task:
# 	•	If CPU < 50 → print "Server is healthy"
# 	•	If CPU between 50–80 → "Server under moderate load"
# 	•	If CPU > 80 → "High CPU usage! Scale required"

# cpu_usage = 80

# if cpu_usage < 50:
#     print(f"Server is healthy")
# elif cpu_usage > 80:
#     print("High CPU usage! Scale required")
# else :
#     print("Server under moderate load")

cpu_usage = 81

if cpu_usage < 50:
    print("Server is healthy")
elif 50 <= cpu_usage <= 80:
    print("Server under moderate load")
else:
    print("High CPU usage! Scale required")