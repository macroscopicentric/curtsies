import sys

from fmtstr.fmtfuncs import blue, red, bold, on_red

from fmtstr.canvas import Canvas
from fmtstr.terminal import Terminal

if __name__ == '__main__':

    print(blue('hey') + ' ' + red('there') + ' ' + red(bold('you')))

    with Terminal(sys.stdin, sys.stdout) as tc:
        with Canvas(tc) as t:
            rows, columns = t.tc.get_screen_size()
            while True:
                c = t.tc.get_event()
                if c == "":
                    sys.exit() # same as raise SystemExit()
                elif c == "a":
                    a = [blue(on_red(c*columns)) for _ in range(rows)]
                elif c == "b":
                    a = t.array_from_text("a small array")
                else:
                    a = t.array_from_text("try a, b, or ctrl-D")
                t.render_to_terminal(a)


