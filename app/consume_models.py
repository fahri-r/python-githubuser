from flask import render_template, request, json
import requests, random

class Consume:
    def __init__(self):
        self.headers = {
            'Authorization' : 'token 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'
        }

    def search(self, username):
        url = 'https://api.github.com/search/users'
        params = {
            'q' : username
        }
        r = requests.get(url, params = params, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def random_user(self):
        url = 'https://api.github.com/users'
        since = random.randint(0, 30000)

        params = {
            'since' : since,
            'per_page' : 9
        }
        r = requests.get(url, params = params, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def user_detail(self, username):
        url = 'https://api.github.com/users/{}'.format(username)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def followers(self, username):
        url = 'https://api.github.com/users/{}/followers'.format(username)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content

    def following(self, username):
        url = 'https://api.github.com/users/{}/following'.format(username)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content

    
    def random_repo(self):
        url = 'https://api.github.com/repositories'
        since = random.randint(0,30000)
        params = {
            'since' : since
        }
        r = requests.get(url, params=params, headers=self.headers)

        if r.status_code == 200 :
            repos = json.loads(r.content)
            content=[]
            for index, repo in enumerate(repos):
                content.append(repo)
                if index == 8:
                    break

        else:
            content = None
        
        return content
    
    def user_repo(self, username):
        url = 'https://api.github.com/users/{}/repos'.format(username)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def repo_languages(self, username, repo):
        url = 'https://api.github.com/repos/{0}/{1}/languages'.format(username, repo)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def repo_commits(self, username, repo):
        url = 'https://api.github.com/repos/{0}/{1}/commits'.format(username, repo)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content


    def repo_branches(self, username, repo):
        url = 'https://api.github.com/repos/{0}/{1}/branches'.format(username, repo)
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200 :
            content = json.loads(r.content)
        else:
            content = None
        
        return content