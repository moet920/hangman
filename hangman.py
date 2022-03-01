#　ハングマンゲーム！

def hangman (word):
  wrong = 0     #間違えた回数
  stages = ['',
            '_________       ',
            '|       ｜      ',
            '|       ｜      ',
            '|       😅      ',
            '|      /｜\     ',
            '|      /  \     ',
            '|               ',
            ]
  rletters = list(word)       #残りの文字
  board = ['_'] * len(word)   #みせるやつ
  win = False
  print('ハングマンへようこそ！')
  while wrong < len(stages) - 1:
    print('\n')
    msg = '1文字を予想してね'
    char = input(msg)
    if char in rletters:
      cind = rletters.index(char)
      board[cind] = char
      rletters[cind] = '$'
    else:
      wrong += 1
    print(' '.join(board))
    e = wrong + 1
    print('\n'.join(stages[0:e]))
    if '_' not in board:
      print('あなたの勝ち！')
      print(' '.join(board))
      win = True
      break
  if not win:
    print('\n'.join(stages[0:wrong+1]))
    print('あなたの負け！正解は{}'.format(word))

wordlist = ['cat', 'dog', 'rabbit', 'turtle', 'bear', 'fox']

import random
w = wordlist[random.randint(0, len(wordlist))-1]
hangman (w)
