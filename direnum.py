import requests

input_directory = str(input("Enter the wordlist path: "))
input_domain = str(input("Enter the domain name: "))

directory = open(input_directory).read()
directories = directory.splitlines()

for dir in directories:
    urlpath = f"http://{input_domain}/{dir}"
    try:
        r = requests.get(urlpath)
        if r.status_code == 200:
            print(f"200 Ok Found - {urlpath}")
    except requests.exceptions.RequestException:
        pass
    