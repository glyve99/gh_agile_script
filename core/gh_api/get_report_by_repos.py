from github import Github
from github.Repository import Repository
from utils.one_week_range import one_week_range

def get_report_by_repos(repos: list[Repository], client: Github) -> list[str]:
    '''
    Get information of a list of repositories.
    '''

    res = []

    for repo in repos:

        info = {}

        repo_name = repo.name
        open_issues = repo.get_issues(state='open')
        closed_issues = repo.get_issues(state='closed', since=one_week_range())
        milestone = repo.get_milestones(state='open')[0]
        pull_requests = repo.get_pulls()

        info['name'] = repo_name
        info['open_issues'] = ', '.join([i.title for i in open_issues])
        info['closed_issues'] = ', '.join([i.title for i in closed_issues])
        info['a'] = 'a'
        info['pull_requests'] = ', '.join([pr.title for pr in pull_requests])
        info['milestone'] = str(round((milestone.closed_issues / (milestone.open_issues + milestone.closed_issues)) * 100, 2))

        res.append(info)
    
    return res