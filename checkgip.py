#!/usr/bin/env python
# -*- coding: utf-8 -*-

# checkgip.py

import os, sys
import time
import json
import requests
import socket

g_slackWebhook =  ''
g_settingPath = ''

def checkMain():
    '''
    メインルーチン
    '''
    global g_settingPath
    g_settingPath = os.path.abspath(os.path.dirname(__file__)) + '/checkgip.json'

    loadSettings()

    # グローバルIPを求める
    globalIPAddr = getGlobalIPAddr()

    if (getPrevGlovalIPAddr() == globalIPAddr):
        print 'IP Addr is not change.'
    else:
        print 'IP Addr is change. ' + globalIPAddr
        setPrevGlovalIPAddr(globalIPAddr)
        sendSlackMsg(globalIPAddr)

def sendSlackMsg(globalIPAddr):
    '''
    Slackメッセージ送信
    '''
    msg = ''
    msg = getOSUname() + '\\nglobal IP Addr : ' + globalIPAddr

    payload = json.loads('{"text": "%s"}' % msg)
    r = requests.post(g_slackWebhook, data=json.dumps(payload))
    print r.status_code
    print r.text

def getPrevGlovalIPAddr():
    ''' 
    前回 Global IPアドレスを読み込む
    '''    
    if (os.path.exists(g_settingPath)):
        settingFile = open(g_settingPath, 'r') 
        settingJSON = json.load(settingFile)
        if('prevAddr' in settingJSON):
            return settingJSON['prevAddr']
        else:
            return ''
    else:
        print g_settingPath
        return ''

def loadSettings():
    ''' 
    設定データを読み込み
    '''
    global g_slackWebhook
    settingJSON = {}
    if (os.path.exists(g_settingPath)):
        settingFile = open(g_settingPath, 'r') 
        settingJSON = json.load(settingFile)
        if('slackWebhook' in settingJSON):
            g_slackWebhook = settingJSON['slackWebhook']

def setPrevGlovalIPAddr(prevAddr):
    ''' 
    前回 Global IPアドレスを書き込む
    '''
    settingJSON = {}
    settingJSON['slackWebhook'] = g_slackWebhook
    settingJSON['prevAddr'] = prevAddr
    with open(g_settingPath, 'w') as settingFile:
        json.dump(settingJSON, settingFile)

def getGlobalIPAddr():
    '''
    グローバル IP を取得する 
    '''
    url = 'http://ipcheck.ieserver.net/'
    res = requests.get(url)
    return str(res.text.rstrip('\n'))

def getOSUname():
    '''
    Hostname を取得する
    '''
    return '%s' % socket.gethostname()

if __name__ == '__main__':
    checkMain()