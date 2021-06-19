from github import Github
from datetime import datetime, timedelta

def report_by_repo(repo_name, gh_client: Github):

    res = {}

    repos = list(gh_client.get_organization('EJComp-Unesp').get_repos())
    repo = list(filter(lambda repo: repo.name == repo_name, repos))[0]
    if not repo:
        print('Repository not found.')
    
    res['contributors'] = [c.name for c in repo.get_contributors()]

    one_week_ago = datetime.now() - timedelta(days=7)
    commits = list(repo.get_commits(since=one_week_ago))

    res['commits'] = []
    for commit in commits:
        info = {}
        info['author'] = commit.author.name
        info['url'] = commit.url
        info['comments'] = [{'body': c.body, 'url': c.url} for c in commit.get_comments()]
        info['pull_requests'] = [{'title': p.title, 'url': p.url} for p in commit.get_pulls()]
        res['commits'].append(info)
    print(res)