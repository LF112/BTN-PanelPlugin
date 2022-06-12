#!/usr/bin/python
#coding: utf-8
# +-------------------------------------------------------------------
# | ________________   _____   ______________  _________
# | ___  __ )__  __/   ___  | / /__  ____/_  |/ /__  __/
# | __  __  |_  /      __   |/ /__  __/  __    /__  /
# | _  /_/ /_  /       _  /|  / _  /___  _    | _  /
# | /_____/ /_/        /_/ |_/  /_____/  /_/|_| /_/
# |
# | BTN - 宝塔下一代现代化面板 [ https://github.com/btnext ]
# +-------------------------------------------------------------------
# | Author: LF112 (futiwolf) <lf@lf112.net>
# | Made with love by LF112 [https://lf112.net]
# +-------------------------------------------------------------------
import re
import sys,os

panelPath = os.getenv('BT_PANEL')
if not panelPath: panelPath = '/www/server/panel'

os.chdir(panelPath)
sys.path.append("class/")
import public

class btnext_main:
    # 实例化 BTN
    def __init__(self):
        pass

    def whoami(self, get):
        return {'status': True, 'msg': "I'm BTN, Working for you!"}
    
    #=> BTN 前端数据扩展 | 基于宝塔内部未逻辑未公开调用的数据
    # 获取面板登录状态过期时间
    def getOverTime(self, get):
        return {'status': True, 'data': public.get_session_timeout()} # > 从内部 public 库中读取面板登录状态过期时间
    
    # 获取面板离线模式状态
    def getPanelLocal(self, get):
        return public.returnMsg(True, public.is_local())
    
    # 获取面板开发者模式状态
    def getPanelDevMode(self, get):
        return public.returnMsg(True, public.is_debug())
    
    #=> BTN 前端请求扩展 | 同上 ↑
    # 设置面板登录状态过期时间
    def setOverTime(self, get):
        session_StoragePath = 'data/session_timeout.pl' # > 宝塔内部存储过期时间的文件地址 | '为啥不用数据库啊'
        session_timeout = int(get.time) # > 读取传入的过期时间
        s_time_tmp = public.readFile(session_StoragePath)
        if not s_time_tmp: s_time_tmp = '0' # > 如果文件不存在, 则初始化为 0
        if int(s_time_tmp) != session_timeout:
            if session_timeout < 300: return public.returnMsg(False, '超时时间不能小于 300 秒')
            if session_timeout > 86400: return public.returnMsg(False, '超时时间不能大于 86400 秒')
            public.writeFile(session_StoragePath, str(session_timeout)) # > 写入新的过期时间
            public.restart_panel()  # > 重启面板
            return public.returnMsg(True, '设置完成！')
        else:
            return public.returnMsg(False, '超时时间未改变')
        
    # 设置面板标题
    def setPanelTitle(self, get):
        public.SetConfigValue('title',public.xssencode2(get.webname))
        return public.returnMsg(True, '设置完成！')