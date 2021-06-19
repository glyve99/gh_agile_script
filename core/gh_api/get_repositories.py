from github import Github
from github.Repository import Repository
from github.Organization import Organization

def get_repositories(repos_names: list[str], client: Github) -> list[Repository]:

    repo_list = []

    for repo_name in repos_names:
      repo = client.get_repo(repo_name)
      repo_list.append(repo)
    
    return repo_list