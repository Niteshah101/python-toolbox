import requests

input_wordlist = str(input("Enter the path of wordlists: "))
input_domain = str(input("Enter the target domain name: "))

subdomains = open(input_wordlist).read()
sub_domain = subdomains.splitlines()

for sub in sub_domain:
    urlpath = f"http://{sub}.{input_domain}"

    try:
        r = requests.get(urlpath)
        if r.status_code == 200:
            print(f"200 OK - Found: {urlpath}")

    except requests.exceptions.RequestException:
        pass
    