import time
import string

hands = '''
           ||                   ||      
        || || ||             || || ||   
     || || || ||             || || || ||
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
        || || ||             || || || ||
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
     ||   /|| ||             || || || ||
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
     || ||   /||             || || || ||
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
     || || ||    _,          || || || ||
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
     || || || ||             || || || ||
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
     || || || ||             || || || ||
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
     || || || ||           _,   || || ||
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
     || || || ||             ||\   || ||
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
     || || || ||             || ||\   ||
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
     || || || ||             || || ||   
     || || || ||             || || ||\  
     || || || ||             || || ||\\ 
     | U  U  U |  ||     ||  | U  U  U |
     (         |  ||     ||  |         )
      \         L/ |     | \√         / 
       \          /       \          /  
        |       _/         \_       |   
        |      /             \      |   
'''
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
        return ch

    return _getch

getch = _find_getch()

chars = {' ': right_thumb,
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
         }


print('\n'*13)
print('\033[13A', hands)
time.sleep(1)
print('\033[13A', left_pinky)
ch = getch()
print('\033[13A', hands)
#print(ch.lower(), ord(ch))

while ch.lower() in chars.keys():
    print('\033[13A', chars[ch.lower()])
    ch = getch()
