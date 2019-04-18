# -*- coding: utf-8 -*-
'''
Created on 2019. 4. 13.

@author: jeong
'''
import telepot

token= "876221220:AAEQWx1k0dlZZR_Q9iUUx5Qlpwn3twxIjb8"

mc = "463263981"

bot = telepot.Bot(token)

bot.sendMessage(mc, u"안녕하세요 cgVot입니다")