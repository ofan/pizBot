# coding: utf-8
# Configuration file for pizBot
# This is a normal python source file.

if __name__=='__main__':
    print "This file is the config file for pizBot\nDon't run this file directly.\nRead README to obtain more information."
    exit()

"""
Notes:
pizBot supports connecting to multiple servers at a time.
All irc servers to connect are stored in a list,every element in the list is a
dictionary,which contains the information for a single server.

Keys description:
'server'   : Server's address,leading '!' suggests that the server is ignored 
             by pizBot,it's useful when you want to temporarily block a server.
             Leading with white spaces is not allowed.
'short'    : The short name of the server.
'port'     : The remote port number.
'nick'     : Nick to use.
'pass'     : Password for the server,many irc services take this as your
             registered user's password,it's convenient for identification.
'channels' : A comma-separated list of channels to join.The last character
             must NOT be a comma.
"""
Networks=[
        {'server'   : 'irc.freenode.net',
         'short'    : 'freenode',
         'port'     : 6667,
         'nick'     : 'pizzz',
         'pass'     : 'none',
         'channels' : '#ofan-bot'},
        {'server'   : 'irc.oftc.net',
         'short'    : 'oftc',
         'port'     : 6667,
         'nick'     : 'pizzz',
         'pass'     : 'none',
         'channels' : '#ofan-bot'}
        ]
