import subprocess

cmd = 'sudo nmap -sn 192.168.1.0/24'
response_original = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE)


response_original = str(response_original.stdout)
print(response_original)

print(response_original.split('\n'))