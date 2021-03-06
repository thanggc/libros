
from functools import wraps

def unarygen (fn):
    @wraps (fn)
    def envoltorio (inic):
        while True:
            yield inic
            inic = fn (inic)
    return envoltorio

@unarygen
def dedosendos (n):
    return n + 2

if __name__ == '__main__':
    from itertools import islice
    print list (islice (dedosendos (0), 10))
