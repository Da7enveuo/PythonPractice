# Practice creating tools to use
import paramiko

#from paramiko import SSHClient
ip = str(input("Please enter the target ip address: "))
user = str(input("Please enter the name of the user: "))
pword = str(input("Please enter the password of the user: "))
pkeypath = str(input("Please enter the path to the private key if available(type n if not): "))
class ssh():
    
    def __init__(self, ip, user, pword, pkeypath):
        self.ip = ip
        self.user = user
        self.pword = pword
        self.pkeypath = pkeypath
    def sshcon(self):
        targ = paramiko.SSHClient()
        targ.load_system_host_keys()
        try:
            priv = paramiko.RSAKey.from_private_key(pkeypath)
        except:
            priv = None
            print('priv_key set to none')
            targ.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.pkeypath == 'n':
                print('got this far')
                targ.connect(self.ip, username=self.user, password=self.pword)
            else:
                targ.connect(self.ip, self.user, pkey=self.pkeypath)
        except:
            print('That priv key file/ pword is incorrect.')
            targ.close()
            print('Ending session...')
            return
            
        command = None
        while command != 'exit':
            print('success')
            command = input()
            if command == 'exit':
                targ.close()
                break
            stdin, stdout, stderr = targ.exec_command(command)
            exit_code = stdout.read().decode('ascii').strip("\n")
            print(exit_code)
            print(stderr.read())
a = ssh(ip, user, pword, pkeypath)
a.sshcon()
