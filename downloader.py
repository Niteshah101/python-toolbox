import sys
import requests


#Download large file in chunk
def download(link):
    chunk_size = 1024*8 #8KB
    total_size = 0
    try:
        
        with open("download", "wb") as f:
            r = requests.get(link, timeout=10, stream=True, allow_redirects=True)
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                total_size += len(chunk)
            print(f"Download success: download  {total_size/1024} KB")
    except(requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
        print("Error occured: ", e)


def main():
        try:
            print(f"Example use:  python3 {sys.argv[0].split("/")[-1]} <url_link> ")
            url_input = sys.argv[1]
            download(url_input)
        except Exception as e:
             print("Error:", e)

main()