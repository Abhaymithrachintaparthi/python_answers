employee={"name":"tim","age":30,"birthday":"1990-03-10","job":"DevOps Engineer"}
employee["job"] = "Software Engineer"
del employee["age"]
for i,j in employee.items():
    print(i,':',j)
