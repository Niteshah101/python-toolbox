import requests
import argparse

parser = argparse.ArgumentParser(description="Argument for directory enumeration")

parser.add_argument(
    '-d',
    '--domain',
    required=True,
    help="domain name"

)

parser.add_argument(
    '-w',
    '--wordlist',
    required=True,
    help="for wordlist"
)

parse = parser.parse_args()
wordlist_arg = parse.wordlist
domain_arg = parse.domain


directory = open(wordlist_arg).read()
directories = directory.splitlines()

for dir in directories:
    urlpath = f"http://{domain_arg}/{dir}"
    try:
        r = requests.get(urlpath)
        if r.status_code == 200:
            print(f"200 Ok Found - {urlpath}")
    except requests.exceptions.RequestException:
        pass
    