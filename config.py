# coding: utf-8
# Configuration file for pizBot
# This is a normal python source file.

if __name__=='__main__':
    print "This file is the config file for pizBot\nDon't run this file directly.\nRead README to obtain more information."
    exit()
class Config:
    # IRC servers to connect,server addresses separated by white spaces
    # Leading '!' in a server address means that the server is ignored by pizBot temporally.
    servers="irc.freenode.net !irc.oftc.net"
    # Ports to use for every server,the order is same as in server list,separated by white spaces
    # Ignored servers' ports will be skipped automatically
    ports="6667 6667"
    # Passwords for every server.Put 'none' if no password for that server
    passwd="none none"
    # Bot's nick name,same rule as above.
    nick="pizzz pizzz"
    
    
