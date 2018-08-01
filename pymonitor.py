import os
import subprocess
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def log(s):
    print('[Monitor] %s' % s)


class MyFileSystemEventHander(FileSystemEventHandler):

    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

    # 完成修改后启动
    def on_modified(self, event):
        if event.src_path.endswith('.py') or event.src_path.endswith('.html') or event.src_path.endswith('.css'):
            log('Python source file changed: %s' % event.src_path)
            self.restart()


process = None


def kill_process():
    global process
    if process:
        log('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process
    command = []
    # 加入Python 命令符
    command.append("python")
    appPath = os.path.abspath("./runserver.py")
    print(appPath)
    command.append(appPath)

    log('Start process command -> %s...' % ' '.join(command))
    process = subprocess.Popen(
        command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):

    # 监视目录文件
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(
        restart_process), path, recursive=True)
    log('Watching directory %s...' % path)
    observer.start()

    # 开始执行入口文件
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    # 检测到键盘 ctrl C 终止命令后结束
    observer.join()


if __name__ == '__main__':
    print(os.path.abspath("."))
    # 在当前目录的子目录中进行监视
    path = os.path.abspath('./WebProject/')
    print(os.path.exists(path))
    start_watch(path, None)
