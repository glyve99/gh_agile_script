import os
import sys

from github import Github
from core.pdf_gen.main import generate_pdf
from core.gh_api.get_repositories import get_repositories
from core.gh_api.get_report_by_repos import get_report_by_repos


###Env vars
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('GH_TOKEN')
###


def main():

    client = Github(TOKEN)
    comma_separated_repos = sys.argv[1]
    repos_names = comma_separated_repos.split(',')
    repos = get_repositories(repos_names, client)
    reports = get_report_by_repos(repos, client)
    print(reports)
    generate_pdf([list(report.values()) for report in reports])

if __name__ == '__main__':
    main()