# Command line tool for Downloading files from github
# https://github.com/Aniket965/github-files-downloader
# @aniket965

import requests
from termcolor import colored

print(
    colored(
        '''
    Command line tool for Downloading files from github
    https://github.com/Aniket965/github-files-downloader
    @aniket965
        
    Follow Simple Intrustions for Downloading Files!!

    '''
        , 'yellow')
)


def is_private_repo(url):
    return False


def list_files_and_dir_from_url(url):
    headers = {"Authorization": "token "}
    json = {"query": "{ viewer  { login } }"}
    x = requests.post('https://api.github.com/graphql', json=json, headers=headers)

    print(x.json())

repositoryUrl = input("Enter the Url of the Repository 😅\n")

if is_private_repo(repositoryUrl):
    print(colored('this is Repository is private if you have Admin Access you can access it '
                  'by providing the credentials You want to Proceed ?🙂🙃 yes|no'), "cyan")
    if input() == 'yes' or input() == "\n":
        print("Superb!!!")
    else:
        print(
            colored(
                '\n'
                '            Don\'t be Sad!! thanks for using github-files-downloader\n'
                '            '
                , 'blue'
            )
        )
else:
    list_files_and_dir_from_url(repositoryUrl)
