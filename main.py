# Command line tool for Downloading files from github
# https://github.com/Aniket965/github-files-downloader
# @aniket965

import re

import requests
from github import Github
from termcolor import colored

g = Github("usrname", "password")
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


def get_content_download_url(filepath, branch, filename):
    return "https://raw.githubusercontent.com/" + filepath + "/" + branch + "/" + filename


def list_files_and_dir_from_url(url):
    for content in g.get_repo(full_name_or_id="Aniket965/github-files-downloader").get_contents(path="/"):
        ref = re.search(r'ref=\w+', content.url, re.M | re.I).group()
        file_content = requests.get(
            get_content_download_url("Aniket965/github-files-downloader", ref[4:], content.name))
        file = open("ani" + content.name, "w")
        print("Downloading!!    " + content.name)
        file.write(file_content.text)
        file.close()


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
