# Command line tool for Downloading files from github
# https://github.com/Aniket965/github-files-downloader
# @aniket965

import re

import requests
from github import Github
from pick import pick
from termcolor import colored

g = Github("username", "pass")
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


def download_and_save_from_url(url, filepath, name):
    file_content = requests.get(url)
    file = open(filepath, "w")
    print("Downloading!! " + name)
    file.write(file_content.text)
    file.close()


def list_files_and_dir_from_url(url):
    # for content in g.get_repo(full_name_or_id="Ujjwal-9/Demos").get_contents(path="/"):
    #     ref = re.search(r'ref=\w+', content.url, re.M | re.I).group()
    #     # download_and_save_from_url(
    #     #     get_content_download_url("Aniket965/github-files-downloader", ref[4:], content.name),
    #     #     "ani"+content.name,
    #     #     content.name
    #     # )
    #     #
    #     if content.type == "dir":
    #         print(colored("../" + content.name, "blue"))
    #     else: ed(content.name, "magenta"))
    contents = g.get_repo(full_name_or_id="Ujjwal-9/Demos").get_contents(path="/")
    title = "Select file or directory for downloading files"
    dirs = ["../" + content.name for content in contents if content.type == "dir"]
    files = [content for content in contents if content.type == "file"]
    selected_content, index = pick(
        ["download this directory and containg directories",
         "download this directory only"]
        + dirs + [file.name for file in files], title)
    # print(contents[index])
    i = [file.name for file in files].index(selected_content)
    ref = re.search(r'ref=\w+', files[i].url, re.M | re.I).group()
    download_and_save_from_url(get_content_download_url("Ujjwal-9/Demos", ref[4:], selected_content),
                               "ani" + selected_content, selected_content)

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
