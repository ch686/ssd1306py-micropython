"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
ssd1306操作封装.支持多种英文字库
forked from jdhxyy/ssd1306py-micropython
Authors: ch686 <ch686@126.com>
"""

import machine

import ssd1306py.ssd1306 as ssd1306
import ssd1306py.myfont8 as myfont8
import ssd1306py.myfont16 as myfont16
import ssd1306py.myfont24 as myfont24
import ssd1306py.myfont32 as myfont32
import ssd1306py.cn as cn

_oled = None
_i2c = None
_width = 0
_height = 0


def init_i2c(scl, sda, width, height, i2c=-1):
    """
    初始化i2c接口
    :param scl: i2c的时钟脚
    :param sda: i2c的数据脚
    :param width: oled屏幕的宽度像素
    :param height: oled屏幕的高度像素
    :param i2c: i2c口
    """
    global _oled, _width, _height
    _i2c = machine.I2C(i2c, scl=machine.Pin(scl), sda=machine.Pin(sda))
    _width = width
    _height = height
    _oled = ssd1306.SSD1306_I2C(_width, _height, _i2c)


def clear():
    """清除屏幕"""
    global _oled
    _oled.fill(0)


def show():
    """屏幕刷新显示"""
    global _oled
    _oled.show()


def pixel(x, y):
    """画点"""
    global _oled
    _oled.pixel(x, y, 1)

def set_font():    
    _oled.set_myfont(myfont8.font8, 8)
    _oled.set_myfont(myfont16.font16, 16)
    _oled.set_myfont(myfont24.font24, 24)
    _oled.set_myfont(myfont32.font32, 32)
    
def text(string, x_axis, y_axis, font_size):
    """显示字符串.注意字符串必须是英文或者数字"""
    global _oled
     _oled.draw_text(string, x_axis, y_axis, font_size)

