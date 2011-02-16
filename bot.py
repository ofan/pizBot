#!/usr/bin/python2
#-*-coding:utf-8-*-
import socket,config

# Sockets list
Irc=[]
# End Of Message
EOM='\r\n'
# Buffer size
BuffSize=4096

for serv in config.Networks:
    if serv['server'][0]=='!':
        continue
    irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    irc.connect((serv['server'],serv['port']))
    irc.recv(BuffSize)
    irc.send('PASS '+serv['pass']+EOM)
    irc.send('NICK '+serv['nick']+EOM)
    irc.send('USER '+serv['nick']+' pizBot pizBot pizBot :'+serv['nick']+EOM)
    irc.send('JOIN '+serv['channels']+EOM)
    Irc.append((serv,irc))

while True:
    for profile,irc in Irc:
        data = irc.recv(BuffSize)
        print 'RAW '+data
        if data.find('PING')!=-1:
            print 'Ping from'+profile['short']
            irc.send('PONG '+data.split()[1]+EOM)
        elif data.find('PRIVMSG')!=-1:
            source = data.split('!')[0].replace(':','')
            message = ':'.join(data.replace('\r','').replace('\n','').split(':')[2:])
            destination=''.join(data.split(':')[:2]).split(' ')[-2]
            if destination==profile['nick']:
                destination='PRIVATE'
            print '(',destination,')',source+':',message
