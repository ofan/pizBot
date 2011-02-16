#!/usr/bin/python2
#-*-coding:utf-8-*-
import socket
server = 'irc.freenode.net'
port = 6667
nick = 'tyty'
realname=nick
channel='#ofan-bot,#ubuntu-cn'

irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
irc.connect((server,port))
irc.recv(4096)
irc.send('NICK '+nick+'\r\n')
irc.send('USER '+nick+' t t t :'+realname+'\r\n')
irc.send('JOIN '+channel+'\r\n')
irc.send('PRIVMSG '+channel+' :Hello.\r\n')
while True:
    data = irc.recv(4096)
    if data.find('PING')!=-1:
        irc.send('PONG '+data.split()[1]+'\r\n')
    elif data.find('PRIVMSG')!=-1:
        source = data.split('!')[0].replace(':','')
        message = ':'.join(data.split(':')[2:])
        destination=''.join(data.split(':')[:2]).split(' ')[-2]
        if destination==nick:
            destination='PRIVATE'
        print '(',destination,')',source+':',message
