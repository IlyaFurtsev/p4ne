import paramiko, time

buff_size=10000
timeout=1

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect('10.31.72.160',username='restapi',password='j0sg1280-7@',look_for_keys=False,allow_agent=False)
session = ssh_connection.invoke_shell()
time.sleep(timeout)
session.send('terminal length 0\n')
time.sleep(timeout)
log=session.recv(buff_size)
time.sleep(timeout)
session.send('\nshow interfaces\n')
time.sleep(timeout*3)
log=session.recv(buff_size).decode()
llog=log.split('\n')


for i in llog:
    if 'Gigabit' in i:
        print(i)
    elif 'Loopback' in i:
        print(i)
    elif 'packets input' in i:
        print(i)
    elif 'packets output' in i:
        print(i)
    else: continue

