# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File document manipulation related methods.
move_file(srcfile, dstfile)   # 移动文件
copy_file(srcfile, dstfile)   # 拷贝文件
sizeConvert(size)  # 格式化文件大小，参数是文件的bytes大小
hashFile(file)   # hash文件，得到一个16进制的指纹
MD5File(file)   # MD5校验，返回MD5值
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/29 17:41"
__all__ = ["__version__", "move_file", "copy_file", "sizeConvert", "hashFile", "MD5File"]
__version__ = "1.0.1"
import os
import shutil
import hashlib


def move_file(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        raise EOFError("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile,dstfile)
        print "move %s -> %s complete"%( srcfile,dstfile)


def copy_file(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        raise EOFError("%s not exist!")
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
            print "create folder '%s'" % fpath
        try:
            shutil.copy2(srcfile, dstfile)
            print "OK! copy %s -> %s complete" % (srcfile, dstfile)
        except:
            raise


def sizeConvert(size):
    K, M, G = 1024.0, 1024.0 ** 2, 1024.0 ** 3
    if size >= G:
        return str(round(size / G, 2)) + 'GB'
    elif size >= M:
        return str(round(size / M, 2)) + 'MB'
    elif size >= K:
        return str(round(size / K, 2)) + 'KB'
    else:
        return str(size) + 'Bytes'


__CHUNKSIZE = 102400  # 速度比较快的一个值，每次读取100K
def hashFile(file):
    '''
    对文件进行hash，得到一个16进制的指纹数据
    '''
    h = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(__CHUNKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def MD5File(file):
    '''
    对文件进行MD5校验
    '''
    h = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(__CHUNKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()