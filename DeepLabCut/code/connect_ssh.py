import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname = 'scc1.bu.edu'
password = input("Password:")
client.connect(hostname, username='zackl', password=password)
stdin, stdout, stderr = client.exec_command('ls')

for line in stdout:
    print('... ' + line.strip('\n'))
client.close()