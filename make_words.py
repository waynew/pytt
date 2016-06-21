def make_dict(letters):
    with open('/usr/share/dict/words') as f, \
         open(letters+'.txt', 'w') as outfile:
        letters = set(letters)
        for line in f:
            line = line.strip().lower()
            if not set(line) - letters:
                print(line, file=outfile)

def asdfhghjkl():
    make_dict('asdfhghjkl')


def qwertyuiop():
    make_dict('qwertyuiop')

def zxcvbnm():
    make_dict('zxcvbnm')

if __name__ == '__main__':
    zxcvbnm()
