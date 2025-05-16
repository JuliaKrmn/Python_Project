import requests
import json
import os
import jsonschema
from jsonschema import validate



class GitHub: 
        
# Getting json file from folder 
    @staticmethod
    def load_expected_commits():
        with open(os.path.join("resources", "expected_commits.json"), "r") as f:
            return json.load(f)
    
    @staticmethod
    def load_emojis_expected_schema():
        with open(os.path.join("resources", "emojis_schema.json"), "r") as f:
            return json.load(f)

    #commit_api = requests.get (f" https://api.github.com/repos/{owner}/{repo}/commits")
    # def get_user_defunkt(self):
    #     r = requests.get("https://api.github.com/users/defunkt")
    #     body = r.json()

    #     return body
    
    # def get_non_exist_user(self):
    #     r = requests.get("https://api.github.com/users/defjuliakorman")
    #     body = r.json()

    #     return body

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(f"https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body
    
    def nonexisting_emoji_status(self):
        return requests.get("https://api.github.com/emojis_usa")
        # return r.status_code 
 
    #This two  functions wokr with one API
   #---------------------------------------------  
    
    def recieve_emojis(self):
        r = requests.get(f"https://api.github.com/emojis")
        body = r.json()

        return body
    
    def get_emojis_status(self):
        r = requests.get("https://api.github.com/emojis")
        return r.status_code


   
   #This three  functions wokr with one API
   #--------------------------------------------- 
    def commits_url(self, owner, repo): #This is a function for universal use in other functions related to the same API
        return f"https://api.github.com/repos/{owner}/{repo}/commits"

    def search_commits(self, owner, repo): #Returns all .json body
        r = requests.get(self.commits_url(owner, repo))
        return r.json()

    def search_status_code(self, owner, repo): #Returns status only
        r = requests.get (self.commits_url(owner, repo))
        return r.status_code 
    
    def commits_work_with_parameters (self, owner, repo, author): #Returns search with parameters
        r = requests.get (self.commits_url(owner, repo), params = {"author": author, "commiter": author})
        return r  
    
    def commits_where_head_is(self, owner, repo, sha):
        r = requests.get (self.commits_url(owner, repo) + f"/{sha}/branches-where-head")
        return r
    #-----------------------------------------------------   



        
    