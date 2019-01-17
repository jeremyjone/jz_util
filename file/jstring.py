#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
class JString that handles Chinese and English text strings.
Fixed length thumbnail function is provided.
    e.g.
        The original: "This is Beijing, a very big city."
        It has 33 characters, now, we need only show 12 characters.

        The processing function:
        statements = "This is Beijing, a very big city."
        my_word = JString()
        my_word.trunc_word(statements, 12)  // "This is Be"

        If use Chinese, it's also pretty simple, it just need notice,
        a Chinese character takes up two characters.

hashStr(strInfo)   # hash字符串，得到一个16进制的指纹
"""
from __future__ import unicode_literals
__author__ = 'jeremyjone'
__datetime__ = '2018-11-27 16:04'

import hashlib


class JString(object):

    @staticmethod
    def is_chinese(uchar):
        '''判断一个unicode是否是汉字'''
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
        return False

    @staticmethod
    def is_number(uchar):
        """判断一个unicode是否是数字"""
        if uchar >= u'\u0030' and uchar<=u'\u0039':
            return True
        return False

    @staticmethod
    def is_visible_symbol(uchar):
        """判断一个unicode是否是可见英文字符"""
        if (uchar >= u'\u0020' and uchar <= u'\u002f') \
                or (uchar >= u'\u003a' and uchar <= u'\u0040') \
                or (uchar >= u'\u005b' and uchar <= u'\u0060') \
                or (uchar >= u'\u007b' and uchar <= u'\u007e'):
            return True
        return False

    @staticmethod
    def is_invisible_symbol(uchar):
        """判断一个unicode是否是不可见英文字符"""
        if (uchar >= u'\u0000' and uchar <= u'\u001f') or uchar == u'\u007f':
            return True
        return False

    @staticmethod
    def is_alphabet(uchar):
        """判断一个unicode是否是英文字母"""
        if (uchar >= u'\u0041' and uchar<=u'\u005a') \
            or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return True
        return False

    def is_other(self, uchar):
        """判断是否非汉字，数字和英文字符"""
        if not (self.is_chinese(uchar) or self.is_number(uchar) or self.is_alphabet(uchar)):
            return True
        return False

    # gbk宽度可用于对齐，中文占两个字符位置
    def __word_len(self, u):
        if self.is_invisible_symbol(u):
            return 0
        elif self.is_number(u) or self.is_alphabet(u) or self.is_visible_symbol(u):
            return 1
        return 2

    # 计算文本显示宽度
    def words_len(self, uw):
        i = 0
        for u in uw:
            i += self.__word_len(u)
        return i

    def trunc_word(self, uw, len):
        '''获取指定长度的文本'''
        l = 0
        i = 1
        for u in uw:
            l += self.__word_len(u)
            if l > len:
                return uw[:i-1]
            i += 1
        return uw

    def unicode(self, char):
        '''获取字符的unicode值'''
        return '\u%04x' % ord(char)


def hashStr(strInfo):
    h = hashlib.md5()
    h.update(strInfo.encode())
    return h.hexdigest()
# s = "abcde"
# print(hashStr(s))
# print(hashStr("abcdef"))


def getMD5(text):
    '''md5_handler(str)  # 将文本返回一个md5值'''
    import hashlib
    md5=hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5




if __name__ == '__main__':
    a = u"更新a至1209期"
    # word_test = JString()
    # print a
    # print word_test.trunc_word(a, 10)  # 更新a至120
    # print word_test.words_len(a)  # 13
    #
    # statements = "This is Beijing, a very big city."
    # my_word = JString()
    # print my_word.trunc_word(statements, 12)  # This is Be
    # print my_word.words_len(statements)  # 33

