# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
command information
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/29 18:31"
__all__ = ["__version__", "is_run", "PIDFile"]
__version__ = "1.0.0"


import os
import psutil
import time


PID_FILE = ""




def write_pid(pid_file, pid=-1):
    if pid == -1:
        pid = os.getpid()
    with open(pid_file, 'w') as fp:
        fp.write(str(pid))


def read_pid(pid_file):
    if os.path.exists(pid_file):
        with open(pid_file, 'r') as fp:
            pid = fp.read()
        return pid
    else:
        return False


def write_log(log_content):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_content = time_now + "---->" + log_content + os.linesep
    fp = open('recognition.log', 'a+')
    fp.write(log_content)
    fp.close()


def is_run(pid_file=PID_FILE, pid=-1):
    '''
    默认传入当前程序PID文件，如果判断其他程序，传入其他程序的PID文件即可
    '''
    if not os.path.exists(pid_file):
        with open(pid_file, "w") as wf:
            wf.write("-1")
        return False

    p = read_pid(pid_file)
    p = int(p)
    if p:
        running_pid = psutil.pids()
        if p in running_pid:
            # log_content = "process is running..."
            # write_log(log_content)
            return True
    write_pid(pid_file, pid)
    return False




'''
PID 管理，在 with 语句中使用，控制进程只有一个在运行，否则抛出 AlreadyRun 异常
'''

import os
import sys
import time
import signal

class PIDFile:
  def __init__(self, pidfile):
    self.pidfile = pidfile
    try:
      pid = int(open(pidfile).read())
    except (IOError, ValueError):
      self._write_pid()
      return
    else:
      try:
        os.kill(pid, 0)
      except OSError:
        self._write_pid()
      else:
        raise AlreadyRun(pid)

  def _write_pid(self):
    with open(self.pidfile, 'w') as f:
      f.write(str(os.getpid()))

  def __enter__(self):
    pass

  def __exit__(self, exc_type, exc_value, traceback):
    os.unlink(self.pidfile)


def wait_and_exit(pid):
  res = os.waitpid(pid, 0)[1]
  status = res & 0x7f
  if status == 0:
    status = (res & 0xff00) >> 8
  sys.stdout.flush()
  os._exit(status)


def _got_sgiusr2(signum, sigframe):
  os._exit(0)


class Daemonized(PIDFile):
  '''daemonize the process and then write its pid to file
  * fork
    * chdir("/")
    * setsid
    * fork
      * close fds
      * do_work
    * killed by SIGUSR2
    * _exit
  * waitpid
  * _exit
  This procedure is borrowed from MongoDB.
  '''
  def __init__(self, pidfile):
    pid = os.fork()
    if pid:
      wait_and_exit(pid)

    os.chdir('/')
    os.setsid()
    leader = os.getpid()
    pid_2 = os.fork()
    if pid_2:
      signal.signal(signal.SIGUSR2, _got_sgiusr2)
      wait_and_exit(pid_2)

    super().__init__(pidfile)
    fd = os.open('/dev/null', os.O_RDWR)
    os.dup2(fd, 0)
    os.dup2(fd, 1)
    os.dup2(fd, 2)
    os.close(fd)
    os.kill(leader, signal.SIGUSR2)


class AlreadyRun(Exception):
  def __init__(self, pid):
    self.pid = pid

  def __repr__(self):
    return "Process with pid %d is already running" % self.pid
