# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File document manipulation related methods.
moveFile(srcfile, dstfile)   # 移动文件
copyFile(srcfile, dstfile)   # 拷贝文件
sizeConvert(size)  # 格式化文件大小，参数是文件的bytes大小
hashFile(file)   # hash文件，得到一个16进制的指纹
MD5File(file)   # MD5校验，返回MD5值
showExplorer(filename)  # 打开指定路径的文件夹并选中文件，如果只是文件夹路径，直接打开。
zip_files(zip_dir, zip_filename=None)  # 按zip格式压缩目标文件夹下面所有文件和文件夹
unzip_files(_file)  # 解压zip文件到指定目录
resource(path)  # 用于Pyinstaller打包使用，所有资源文件路径使用该函数装饰即可
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/29 17:41"
__all__ = ["__version__", "moveFile", "copyFile", "sizeConvert", "hashFile", "MD5File",
           "showExplorer"]
__version__ = "1.0.1"
import os
import shutil
import hashlib
import zipfile


def zip_files(zip_dir, zip_filename=None):
    def __zip(zip_dir):
        for folder, sub_folder, files in os.walk(zip_dir):
            _fpath = folder.replace(zip_dir, "")
            _fpath = _fpath and _fpath + os.sep or ""
            zf.write(folder, _fpath)
            for file in files:
                zf.write(os.path.join(folder, file), _fpath + file)

            for sf in sub_folder:
                __zip(sf)

    if not zip_filename:
        zip_filename = zip_dir + ".zip"
    zf = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
    __zip(zip_dir)
    zf.close()


def unzip_files(_file, unzip_dir=None):
    if not unzip_dir:
        unzip_dir = os.path.dirname(_file)
    try:
        zf = zipfile.ZipFile(_file)
        zf.extractall(unzip_dir)
        zf.close()
    except:
        unpackFiles(_file)


def moveFile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        raise EOFError("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile,dstfile)
        print "move %s -> %s complete"%( srcfile,dstfile)


def copyFile(srcfile, dstfile):
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


def showExplorer(filename):
    '''
    打开指定路径的文件夹并选中文件，如果只是文件夹路径，直接打开。
    '''
    if os.path.isfile(filename):
        subprocess.Popen(r'explorer /select,"%s"' % filename.replace('\\', os.sep))
    elif os.path.isdir(filename):
        try:
            os.startfile(filename)
        except:
            subprocess.Popen(['xdg-open', filename])
    else:
        raise ValueError("%s is not correct, please check." % filename)


# 读取当前文件路径，并且拼接，用于资源文件，所有资源文件路径都是用该函数装饰，它服务于PyInstaller
def resource(path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, path)