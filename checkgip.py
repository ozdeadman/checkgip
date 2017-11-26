#!/usr/bin/env python
# -*- coding: utf-8 -*-

# checkgip.py

import os
import json
import socket
import requests

g_slack_webhook = ''
g_setting_path = ''

__version__ = "0.1.0.171126"

def checkMain():
    '''
    main routine
    '''
    global g_setting_path
    g_setting_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'checkgip.json')

    # load setting from json
    loadSettings()

    # get global IP Addr
    global_ipaddr = getGlobalIPAddr()
    if (global_ipaddr == ''):
        print 'Internet Connection error.'
        return -1

    if (getPrevGlobalIPAddr() == global_ipaddr):
        print 'IP Addr is not change.'
    else:
        print 'IP Addr is change. ' + global_ipaddr
        setPrevGlobalIPAddr(global_ipaddr)
        sendSlackMsg(global_ipaddr)

    return 0

def loadSettings():
    ''' 
    load settings from json
    '''
    global g_slack_webhook
    setting_json = {}
    if (os.path.exists(g_setting_path)):
        setting_file = open(g_setting_path, 'r') 
        setting_json = json.load(setting_file)
        if('slackWebhook' in setting_json):
            g_slack_webhook = setting_json['slackWebhook']

def sendSlackMsg(global_ipaddr):
    '''
    send message to Slack
    '''
    msg = ''
    msg = getOSUname() + '\\nglobal IP Addr : ' + global_ipaddr

    payload = json.loads('{"text": "%s"}' % msg)
    r = requests.post(g_slack_webhook, data=json.dumps(payload))
    print r.status_code
    print r.text

def getPrevGlobalIPAddr():
    ''' 
    get prre GlobalIPAddr
    '''    
    if (os.path.exists(g_setting_path)):
        setting_file = open(g_setting_path, 'r') 
        setting_json = json.load(setting_file)
        if('prevAddr' in setting_json):
            return setting_json['prevAddr']
        else:
            return ''
    else:
        print g_setting_path
        return ''

def setPrevGlobalIPAddr(prevAddr):
    ''' 
    set prev gloval IP Addr value on setting file
    '''
    setting_json = {}
    setting_json['slackWebhook'] = g_slack_webhook
    setting_json['prevAddr'] = prevAddr
    with open(g_setting_path, 'w') as setting_file:
        json.dump(setting_json, setting_file)

def getGlobalIPAddr():
    '''
    get global IP Addr
    '''
    url = 'http://ipcheck.ieserver.net/'
    try:
        res = requests.get(url)
    except Exception:
        return ''
    return str(res.text.rstrip('\n'))

def getOSUname():
    '''
    get OS hostname
    '''
    return '%s' % socket.gethostname()

if __name__ == '__main__':
    checkMain()
