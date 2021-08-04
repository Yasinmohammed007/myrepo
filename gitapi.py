from github import Github
import os
from git.repo.base import Repo
import requests

# First create a Github instance:

# using an access token
g = Github("")

headers = {
    'Accept': 'application/vnd.github.v3+json'
}


url_head = 'https://github.com/yasinmohammed007/'


#shell to list time of gitbranhces
#for branch in `git branch -r | grep -v HEAD`;do echo -e `git show --format="%ci %cr" $branch | head -n 1` \\t$branch; done | sort -r

#git branch -r | grep -v HEAD | while read b; do git log --color --format="%ci _%C(magenta)%cr %C(bold cyan)$b%Creset %s %C(bold blue)<%an>%Creset" $b | head -n 1; done | sort -r | cut -d_ -f2- | sed 's;origin/;;g' | head -10
# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    repo_fullname = g.get_repo("yasinmohammed007/"+repo.name)
    print(repo_fullname)
    branch_list = list(repo_fullname.get_branches())
    print(branch_list)
    Repo.clone_from(url_head+repo.name, repo.name)
    print("============================")

for repo in g.get_user().get_repos():
    print(repo.name)
    os.system('cd '+repo.name+';git branch -r | grep -v HEAD | while read b; do git log --color --format="%ci _%C(magenta)%cr %C(bold cyan)$b%Creset %s %C(bold blue)<%an>%Creset" $b | head -n 1; done | sort -r | cut -d_ -f2- | sed \'s;origin/;;g\' | head -10;cd ..')
# response = requests.get('https://api.github.com/user', auth=('yasinmohammed007', ''))
# print(response)
