employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
n = len(employees)
for i in range(n):
    print("name: "+employees[i]["name"] , "job: "+employees[i]["job"] , "city: "+employees[i]["address"]["city"])
message="the country of second employee is "
print( message + employees[1]["address"]["country"])



