# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Check Application is running status. Create a PID file to save app's pid.
If you want to run only one program instance, it will be useful.
It provide two methods:
    * write_pid(pid_file) for write pid to file,
    * is_run(pid_file, filename) for check application performance.
        It will return True or False: True is running, False is not.

How to use:
    # ================== #
    pid_file = "C:\\Users\\yours\\Documents\\MyPID\\test.txt"  # Any location
    if not is_run(pid_file, "C:\\test.py"):  # filename must be same to cmd.
        prc = subprocess.Popen("python C:\\test.py")
        write_pid(pid_file, prc.pid)
    # ================== #
    The above code can normally detect the status of the program.

1.0.1 update release:
Add running apps command check, This allows you to determine the details of
most programs.
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/29 18:31"
__all__ = ["__version__", "__document__", "is_run", "write_pid"]
__version__ = "1.0.1"
import os
import psutil
import subprocess


def __read_pid(pid_file):
    if os.path.exists(pid_file):
        with open(pid_file, 'r') as fp:
            pid = fp.read()
        return pid


def write_pid(pid_file, pid):
    # when pid pass in -1, file will save current application pid.
    if pid == -1:
        pid = os.getpid()
    with open(pid_file, 'w') as fp:
        fp.write(str(pid))


def is_run(pid_file, filename):
    '''
    Determines whether the PID counterpart in the incoming PID
    file is the corresponding program for the incoming filename.
    '''
    if not os.path.exists(pid_file):
        with open(pid_file, "w") as wf:
            wf.write("-1")
        return False

    p = __read_pid(pid_file)
    p = int(p)

    if p > 0:
        try:
            pid = psutil.Process(p)
            if pid.status() == "running":
                print "app is running!"
                cmd = pid.cmdline()[-1].replace("\\", os.sep).replace("/", os.sep)  # cmd command, get app name
                app_name = filename.replace("\\", os.sep).replace("/", os.sep)
                if app_name == cmd:
                    print "app is running cmd"
                    return True

        except psutil.NoSuchProcess:
            print "No Such Process"
            pass

    if p != 0:
        write_pid(pid_file, 0)

    return False


if __name__ == '__main__':
    # pid_file = "./pid.txt"

    # if not is_run(pid_file, "test.py"):
    #     print "nothing running..."
    #     prc = subprocess.Popen("python test.py")
    #     write_pid(pid_file, prc.pid)

    # print "finish!"

    help(__file__)
