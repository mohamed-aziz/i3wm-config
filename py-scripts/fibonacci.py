#!/USR/BIn/python

import i3
import time

prog = "feh -. -B black ~/Bilder/Hintergrund/arch-logo.png"


def fibonacci(num):
    i3.__call__cmd(prog)
    i3.border('none')
    i3.gaps('inner', 'all', 'set', '15')
    time.sleep(0.5)
    if num % 2 == 0:
        i3.border('none')
        if num % 4 == 0:
            i3.focus('up')
            i3.border('none')
        i3.split('h')
        i3.border('none')
    else:
        i3.border('none')
        if num % 4 == 1:
            i3.focus('left')
        i3.split('v')
    if num > 1:
        fibonacci(num - 1)


def run(num):
    # current workspace
    current = [ws for ws in i3.get_workspaces() if ws['focused']][0]
    # switch to workspace named 'fibonacci'
    i3.workspace('fibonacci')
    i3.layout('default')
    fibonacci(num)
    time.sleep(1.5)
    # close all opened terminals
    for n in range(num):
        i3.kill()
        time.sleep(0.5)
    i3.workspace(current['name'])
    i3.gaps('inner', 'all', 'set', '0')

if __name__ == '__main__':
    run(12)
