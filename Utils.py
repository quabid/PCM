import sys
import os
import fcntl
import termios
import struct


def get_args():
    args = sys.argv[1:]
    size = len(args)
    has_args = size > 0
    return has_args, args, size


def get_terminal_size():
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            cr = struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get("LINES", 25), env.get("COLUMNS", 80))

        # Use get(key[, default]) instead of a try/catch
        # try:
        #    cr = (env['LINES'], env['COLUMNS'])
        # except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])


c_width, c_height = get_terminal_size()


def make_line():
    line = "_"
    for i in range(1, c_width, 1):
        line += "_"
    return line


def make_dashed_line():
    line = "-"
    for i in range(1, c_width, 1):
        line += "-"
    return line


# Function for nth Fibonacci number


def fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


LINE = make_line()
DASH = make_dashed_line()
BRK = "\n"
TAB = "\t"


def header(title):
    half_width = int(c_width / 2)
    line = BRK + BRK

    for i in range(1, half_width, 1):
        line += " "

    line += title.title() + BRK + LINE + BRK + BRK
    return line


def center_text(text):
    half_width = int(c_width / 2)
    line = BRK + BRK

    for i in range(1, half_width, 1):
        line += " "

    line += text.title() + BRK + BRK
    return line


def body(body):
    half_width = int(c_width / 4)
    line = BRK

    for i in range(1, half_width, 1):
        line += " "

    line += body + BRK + LINE + BRK
    return line


cls = lambda: os.system("clear")
