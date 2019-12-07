# -*- coding:utf-8 -*-

from game_center import app
import multiprocessing
import signal
import sys
import subprocess


def start_web_server():
    cmd = ["gunicorn", "-w", "1", "-b", "0.0.0.0:9051", "--access-logfile", "-",
           "--error-logfile", "-", "--log-file", "-", "game_center:app"]
    return subprocess.Popen(cmd)


def main():
    web_process = start_web_server()
    
    def exit_kill(sig, frame):
        if sys.version_info >= (3, 7):
            web_process.kill()
        else:
            web_process.terminate()
    for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:
        signal.signal(sig, exit_kill)
    signal.pause()


if __name__ == "__main__":
    main()
