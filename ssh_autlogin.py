import pexpect, sys, curses, yaml


PROMPT = ['# ', '>>> ', '> ', '$ ']
SSH_NEWKEY = "Are you sure you want to continue connecting"
HOST_NOTFOUND = "ssh: Could not resolve hostname test: nodename nor servname provided, or not known"

ID = sys.argv[1]

def ssh_connect(HOST, PASSWORD):
    print(HOST)
    print(PASSWORD)
    connect = pexpect.spawn('ssh ' + HOST)
    for i in range(len(PASSWORD)):
        connect = check_connect(connect, PASSWORD[i])
        if connect == 1:
            return
    connect.interact('$ ')
    res = connect.before
    return res

def check_connect(CONNECT, PASSWORD):
    ret = CONNECT.expect([pexpect.EOF, pexpect.TIMEOUT, HOST_NOTFOUND, SSH_NEWKEY, 'Enter', '[P|p]ass:'])
    print(ret)
    if ret == 0/1:
        print('[-] ERROR Connecting')
        return 1
    if ret == 2:
        print('[-] Host Not Found')
        return 1
    if ret == 3:
        CONNECT.sendline('yes')
        ret = CONNECT.expect([pexpect.TIMEOUT, '[P|p]ass:'])
        if ret == 0/1:
            print('[-] ERROR Connecting')
            return 1
    CONNECT.sendline(PASSWORD)
    return CONNECT


def main():
    with open('ssh_autologin_config.yml', 'r') as yml:
        config = yaml.safe_load(yml)

    HOST = config[ID]['host']
    PASSWORD = config[ID]['pass']

    curses.setupterm()
    term_lines = int(curses.tigetnum("lines"))
    term_cols = int(curses.tigetnum("cols"))
    print(term_lines, term_cols)

    print(ssh_connect(HOST, PASSWORD))
    return

if __name__ == '__main__':
    main()
