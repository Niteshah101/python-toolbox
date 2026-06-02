import hashlib
import sys

def compute_hash(text, algorithm):
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.hexdigest()


def check_hash(target_hash, wordlist, algorithm="md5"):
    try:
        with open(wordlist, 'r') as f:
            for index_number, line in enumerate(f, start=1):
                value = line.strip()
                c_hash = compute_hash(value, algorithm) 
                if not value:
                    continue
                if c_hash == target_hash.lower():
                    return value, index_number
                
            print("There is no has found with this wordlist")
    except FileNotFoundError:
        print("File not found")


def main():

    if len(sys.argv) < 3:
        print(f"Example use: python3 {sys.argv[0].split("/")[-1]} <hash_value> <wordlist_path> <algorithm>")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist = sys.argv[2]
    algorithm = sys.argv[3] if len(sys.argv) > 3 else "md5"

    result, number = check_hash(target_hash,wordlist, algorithm)
    print(f"Hashed value: [{result}] found in {number} tries")
    

main()

                

            
