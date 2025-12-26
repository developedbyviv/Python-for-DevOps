# A tuple represents a CI/CD pipeline flow.
# Some stages are optional, some are mandatory, and order is critical.

# pipeline = ("checkout"
# "build", "test", "deploy")
# TASK
# Write a Python script that:
# 1. Ensures " security_scan" is present after "build"
# 2. Ensures "deploy" is always the last element
# 3. If "security_scan" already exists but is in the wrong position, fix it
# 4. Print the final pipeline tuple
# !RULES (VERY STRICT)
# • X No loops
# • X No list conversion
# • X No set
# • X No sorted ()
# • X No hardcoding final tuple
# • X No multiple reassignment lines for the same variable
# • V Only tuple slicing, tuple concatenation, index (), and if
# HINT (Not a solution)
# • You may need to remove an element before inserting it correctly
# • Tuple removal means rebuilding


pipeline = ("checkout",
"build", "test", "deploy")

if "security_scan" in pipeline:
    i = pipeline.index("security_scan")
    pipeline = pipeline[:i] + pipeline[i + 1]

b = pipeline.index("build")
pipeline = pipeline[:b +1] + ("security_scan",) + pipeline[b + 1:]

if pipeline[-1] != "deploy":
    pipeline = pipeline[:-1] + ("deploy",)

print(pipeline)