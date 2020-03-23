import time

width = 45

def setBar(var, max):
    inx = width*(var/max)
    sA = int(inx+0.5)
    sB = int((width-inx)+0.5)
    bar = "|%s%s| %d%% " % ('#' * sA, ' ' * sB, var*100/max)
    print('\r{}'.format(bar), end='', flush=True)

def clearBar():
    bar = "%s" % " " * width + "      "
    print('\r{}'.format(bar), end='', flush=True)

if __name__ == "__main__":
    for i in range(0, 100):
        setBar(i, 100)
        time.sleep(0.2)
