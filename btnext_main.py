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
import sys,os

panelPath = os.getenv('BT_PANEL')
if not panelPath: panelPath = '/www/server/panel'

os.chdir(panelPath);
sys.path.append("class/")
import public

class btnext_main:
    # 实例化 BTN
    def __init__(self):
        pass

    def whoami(self, get):
        return {"status": True, "msg": "I'm BTN, Working for you!"}