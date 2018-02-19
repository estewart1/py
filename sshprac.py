import paramiko
import sys

ip = 'ec2-52-32-95-162.us-west-2.compute.amazonaws.com'
port = 22
username = 'ec2-user'
key = paramiko.RSAKey.from_private_key_file("/Users/solomondellapenna/py/abc.pem")
cmd = 'nc -zv 169.254.169.254 80'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,pkey=key)

stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)
if 'succeeded' in resp:
    ssh.exec_command('echo $PATH')
