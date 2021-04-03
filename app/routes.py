from app import app
from flask import render_template, request, json, jsonify
import requests
from app.consume_models import Consume

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<username>')
def detail(username):
    user_detail = Consume().user_detail(username)
    repos = Consume().user_repo(username)

    branches = []
    commits = []
    languages = []

    for repo in repos:
        branch = Consume().repo_branches(username, repo['name'])
        commit = Consume().repo_commits(username, repo['name'])
        language = Consume().repo_languages(username, repo['name'])
        
        branches.append(branch)
        commits.append(commit)
        languages.append(language)

    repo_detail = zip(repos, branches, commits, languages)
    return render_template('detail.html', user_detail=user_detail, repo_detail=repo_detail)

@app.route('/search')
def search():
    if len(request.args) > 0:
        username = request.args['username']
        result = Consume().search(username)

        content = []
        for user in result['items']:
            detail = Consume().user_detail(user['login'])
            content.append(detail)
    else:
        content = None    
    return render_template('result.html', content=content, search=username)