import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint


User_input = input("Enter the github username:")

g = Github()
user = g.get_user(User_input)

for repo in user.get_repos():
    print(repo)

request = requests.get('https://api.github.com/users/' + User_input + '/repos')
json = request.json()
for i in range(0, len(json)):
  print("Project Number:", i+1)
  print("Project Name:", json[i]['name'])
  print("Project URL:", json[i]['svn_url'], "\n")
#output
'''Enter the github username:Abhaymithrachintaparthi
Repository(full_name="Abhaymithrachintaparthi/abhay")
Repository(full_name="Abhaymithrachintaparthi/computer")
Repository(full_name="Abhaymithrachintaparthi/git")
Repository(full_name="Abhaymithrachintaparthi/python_answers")
Project Number: 1
Project Name: abhay
Project URL: https://github.com/Abhaymithrachintaparthi/abhay 

Project Number: 2
Project Name: computer
Project URL: https://github.com/Abhaymithrachintaparthi/computer 

Project Number: 3
Project Name: git
Project URL: https://github.com/Abhaymithrachintaparthi/git 

Project Number: 4
Project Name: python_answers
Project URL: https://github.com/Abhaymithrachintaparthi/python_answers'''
