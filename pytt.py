import time
import string

hands = '''
           ||                   ||      
        || || ||             || || ||   
     || || || ||     {:^5}   || || || ||
     || || || ||             || || || ||
     || || || ||             || || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

left_pinky = '''
           ||                   ||      
        || || ||             || || ||   
        || || ||     {:^5}   || || || ||
       /|| || ||             || || || ||
      //|| || ||             || || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

left_ring = '''
           ||                   ||      
           || ||             || || ||   
     ||   /|| ||     {:^5}   || || || ||
     ||  / || ||             || || || ||
     || / /|| ||             || || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

left_middle = '''
                                ||      
        ||    ||             || || ||   
     || ||   /||     {:^5}   || || || ||
     || ||  / ||             || || || ||
     || || / /||             || || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

left_pointer = '''
           ||                   ||      
        || ||                || || ||   
     || || ||    _,  {:^5}   || || || ||
     || || ||  / /           || || || ||
     || || || / /            || || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

left_thumb = '''
           ||                   ||      
        || || ||             || || ||   
     || || || ||     {:^5}   || || || ||
     || || || ||             || || || ||
     || || || ||             || || || ||
     | U  U  U |_        ||  | U  U  U |
     (         | \       ||  |         )
      \         L \      | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

right_thumb = '''
           ||                   ||      
        || || ||             || || ||   
     || || || ||     {:^5}   || || || ||
     || || || ||             || || || ||
     || || || ||             || || || ||
     | U  U  U |  ||        _| U  U  U |
     (         |  ||       / |         )
      \         L/ |      / √         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

right_pointer = '''
           ||                   ||      
        || || ||                || ||   
     || || || ||     {:^5} _,   || || ||
     || || || ||           \ \  || || ||
     || || || ||            \ \ || || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

right_middle = '''
           ||                           
        || || ||             ||    ||   
     || || || ||     {:^5}   ||\   || ||
     || || || ||             || \  || ||
     || || || ||             ||\ \ || ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

right_ring = '''
           ||                   ||      
        || || ||             || ||      
     || || || ||     {:^5}   || ||\   ||
     || || || ||             || || \  ||
     || || || ||             || ||\ \ ||
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''

right_pinky = r'''
           ||                   ||      
        || || ||             || || ||   
     || || || ||     {:^5}   || || ||   
     || || || ||             || || ||\  
     || || || ||             || || ||\\ 
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''


# _find_getch came from this answer on stackoverflow.com
# http://stackoverflow.com/a/21659588/344286
def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ord(ch) == 3:
            raise KeyboardInterrupt('^C entered')
        if ord(ch) == 4:
            raise EOFError('EOF entered')
        return ch

    return _getch

getch = _find_getch()

handedness = 'right'
if handedness == 'right':
    thumb = right_thumb

chars = {' ': thumb,
         '0': right_ring,
         '1': left_pinky,
         '2': left_ring,
         '3': left_middle,
         '4': left_pointer,
         '5': left_pointer,
         '6': right_pointer,
         '7': right_pointer,
         '8': right_middle,
         '9': right_ring,
         'a': left_pinky,
         'b': left_pointer,
         'c': left_middle,
         'd': left_middle,
         'e': left_middle,
         'f': left_pointer,
         'g': left_pointer,
         'h': right_pointer,
         'i': right_middle,
         'j': right_pointer,
         'k': right_middle,
         'l': right_ring,
         'm': right_pointer,
         'n': right_pointer,
         'o': right_ring,
         'p': right_pinky,
         'q': left_pinky,
         'r': left_pointer,
         's': left_ring,
         't': left_pointer,
         'u': right_pointer,
         'v': left_pointer,
         'w': left_ring,
         'x': left_ring,
         'y': right_pointer,
         'z': left_pinky,
         'A': left_pinky,
         'B': left_pointer,
         'C': left_middle,
         'D': left_middle,
         'E': left_middle,
         'F': left_pointer,
         'G': left_pointer,
         'H': right_pointer,
         'I': right_middle,
         'J': right_pointer,
         'K': right_middle,
         'L': right_ring,
         'M': right_pointer,
         'N': right_pointer,
         'O': right_ring,
         'P': right_pinky,
         'Q': left_pinky,
         'R': left_pointer,
         'S': left_ring,
         'T': left_pointer,
         'U': right_pointer,
         'V': left_pointer,
         'W': left_ring,
         'X': left_ring,
         'Y': right_pointer,
         'Z': left_pinky,
         '!': left_pinky,
         '"': right_pinky,
         '#': left_middle,
         '$': left_pointer,
         '%': left_pointer,
         '&': right_pointer,
         "'": right_pinky,
         '(': right_ring,
         ')': right_pinky,
         '*': right_middle,
         '+': right_pinky,
         ',': right_middle,
         '-': right_pinky,
         '.': right_ring,
         '/': right_pinky,
         ':': right_pinky,
         ';': right_pinky,
         '<': right_middle,
         '=': right_pinky,
         '>': right_ring,
         '?': right_pinky,
         '@': left_ring,
         '[': right_pinky,
         '\\': right_pinky,
         ']': right_pinky,
         '^': right_pointer,
         '_': right_pinky,
         '`': left_pinky,
         '{': right_pinky,
         '|': right_pinky,
         '}': right_pinky,
         '~': left_pinky,
         '\t': left_pinky,
         '\n': right_pinky,
         '\r': right_pinky,
        } 


print('\n'*13)
print('\033[13A', hands)
#time.sleep(1)
#print('\033[13A', left_pinky)
ch = ''#getch()
print('\033[13A', hands)
#print(ch.lower(), ord(ch))

text = 'The quick brown fox jumps over the lazy dog'
cur_pos = 0

#while ch.lower() in chars.keys():
while cur_pos < len(text):
    letter = text[cur_pos]
    #print('\033[13A', chars[ch.lower()])
    print('\033[15A')
    print(text[cur_pos:] + '\033[K')
    print(chars[letter].format(letter))
    ch = getch()
    while letter != ch:
        print('\033[1A\a')
        print('\033[15A'+'\n\033[K'*14)
        print('\033[15A')
        time.sleep(0.1)
        print(text[cur_pos:] + '\033[K')
        print(chars[letter].format(letter))
        ch = getch()
    cur_pos += 1
