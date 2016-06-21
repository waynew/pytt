'''
Python Teaches Typing,

Levels:
    1 - Home Row
    1.1 - fj
    1.2 - fghj
    1.3 - dk
    1.4 - dfghjk
    1.5 - sl
    1.6 - sdfghjkl
    1.7 - a;
    1.8 - asdfghjkl;
    1.9 - Words with asdfhghjkl;

    2 - Top Row
    2.1 - ru
    2.2 - rtyu
    2.3 - ei
    2.4 - ertyui
    2.5 - wo
    2.6 - wertyuio
    2.7 - qp
    2.8 - qwertyuiop
    2.9 - 1+2, combination of word

    3 - Bottom Row
    3.1 - vm
    3.2 - vbnm
    3.3 - c,
    3.4 - cvbnm,
    3.5 - x.
    3.6 - xcvbbnm,.
    3.7 - z/
    3.8 - zxcvbnm,./
    3.9 - 1+2+3, combination of word

    4 - Numbers
    4.1 - 47
    4.2 - 4567
    4.3 - 38
    4.4 - 345678
    4.5 - 29
    4.6 - 23456789
    4.7 - 10
    4.8 - `1234567890
    4.9 - 1+2+3+4, combination of word

    5 - Shift
    5.1 - fFgGHhJj
    5.2 - Words with capitalization (1+2+3+4)

    6 - Punctuation
    6.1 - $%^&
    6.2 - #*
    6.3 - #$%^&
    6.4 - @(
    6.5 - @#$%^&*(
    6.6 - !)
    6.7 - !@#$%^&*()
    6.8 - -_=+
    6.9 - {[]}\|
    6.10 - :;'"
    6.11 - ,<>./?

Copyright (c) 2015, Wayne Werner
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its
       contributors may be used to endorse or promote products derived from
       this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import re
import time
import string
import random

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

hand_positions = {' ': thumb,
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


def make_some(population):
    words = ''.join(random.choice(population) for x in range(100)).strip()
    words = re.sub('\s+', ' ', words)
    return words

level_one_one = make_some(' jf')
level_one_two = make_some(' fghj')
level_one_three = make_some(' dk')
level_one_four = make_some(' dfghjk')
level_one_five = make_some(' sl')
level_one_six = make_some(' sdfghjkl')
level_one_seven = make_some(' a;')
level_one_eight = make_some(' asdfghjkl;;')

'''
    1.9 - Words with asdfhghjkl;
'''



def move_to_top():
    print('\033[14A', end='')


def clear(cursor_at_top=True):
    '''
    Clear some screen space. If ``cursor_at_top`` is True, return the cursor
    to the top of the drawing area. Otherwise, leave it at the end.
    '''
    move_to_top()
    print('\n\033[K'*14, end='')
    if cursor_at_top:
        move_to_top()


def draw(cur_pos, text):
    '''
    Draw the text and hand positions based on the letter at the ``cur_pos``
    in ``text``. Return letter in text at ``cur_pos``.
    '''

    letter = text[cur_pos]
    print(text[cur_pos:] + '\033[K')
    print('^', end='')
    print(hand_positions[letter].format(letter))
    return letter


def test(text):
    ch = ''
    cur_pos = 0
    print('\n'*14)
    start = None
    errors = 0
    while cur_pos < len(text):
        clear()
        letter = draw(cur_pos, text)
        ch = getch()
        if start is None:
            start = time.time()
        while letter != ch:
            errors += 1
            print('\a', end='')
            clear()
            time.sleep(0.1)
            letter = draw(cur_pos, text)
            clear()
            letter = draw(cur_pos, text)
            ch = getch()
        cur_pos += 1

    wordcount = text.count(' ')
    letters = len(text)
    seconds = (time.time()-start)
    minutes = seconds/60
    print('{:.2f} Words Per Minute - {:.2f} letters per second'
          .format(wordcount/minutes, letters/seconds))
    print('{:d} errors'.format(errors), '- Great Job!' if not errors else '')


if __name__ == '__main__':
    test(level_one_two)
