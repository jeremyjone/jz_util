# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
拷贝大文件方法，同时进行拷贝验证。
"""
__author__ = "jeremyjone"
__datetime__ = "2019/1/2 13:48"
__all__ = ["__version__", "copyFile", "hashFile"]
__version__ = "1.0.0"
import os
import hashlib
from multiprocessing import Pool, Manager

CHUNKSIZE = 4096


def copyFile(fileName, srcPath, destPath, q):
    # 判断源路径存在
    if not os.path.exists(srcPath):
        print("源文件不存在！")
        return False

    # 判断目标路径存在
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except Exception:
            print("目标路径不存在并且无法创建！")
            return False

    # 构造源文件路径名和目标文件路径名
    srcFileName = srcPath + "/" + fileName
    destFileName = destPath + "/" + fileName

    # 拷贝文件的过程
    with open(srcFileName, "rb") as fr:
        with open(destFileName, "ab") as fw:
            for i in fr:
                fw.write(i)

    # 当完成复制操作，将任务名添加到进程池队列
    q.put(fileName)
    return True


def hashFile(file):
    hl = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
            hl.update(chunk)
    return hl.hexdigest


if __name__ == '__main__':
    srcPath = input("要复制到的路径>>")
    destPath = srcPath + " - 副本"

    n = 2
    tmp_dest = destPath
    while os.path.exists(destPath):
        destPath = tmp_dest + "(%d)" % n
        n += 1

    allFileNames = os.listdir(srcPath)
    allNum = len(allFileNames)
    num = 0

    q = Manager().Queue()  # 进程池中的交互数据需要使用Manager中的队列进行托管
    pool = Pool()
    for i in allFileNames:
        pool.apply_async(func=copyFile, args=(i, srcPath, destPath, q))
    pool.close()

    while num < allNum:
        fileName = q.get()
        num += 1
        rate = num / allNum * 100
        print("Current rate is %.2f%%" % rate)

        # 使用hash验证文件完整性
        srcFileName = srcPath + "/" + fileName
        destFileName = destPath + "/" + fileName
        if hashFile(srcFileName) == hashFile(destFileName):
            print("copy ok!")
        else:
            print("copy failed!")

    pool.join()

    print("Done!")


