from math import *
from ion import * 
from kandinsky import * 
from time import * 
from random import *

snake = [[0,0],[1,0],[2,0]]

head_direction = [1,0]
direction = [1,0]

colors = [
  color(99,155,255),
  color(63,63,133),
  color(255,255,255),
  color(255,50,50),
  color(106,190,48),
  color(102,57,49),
  color(143,86,59),
  color(217,160,102)
  ]

graphics = [
  [[1,5,7,3,0],[2,4,5,1,0],[3,3,3,1,0],[0,5,1,3,1],[1,4,1,1,1],[2,3,1,1,1],[2,4,1,2,2],[5,4,1,2,2],[3,1,2,2,3],[2,0,1,2,3],[5,0,1,2,3]],
  [[1,0,7,3,0],[2,3,5,1,0],[3,4,3,1,0],[0,0,1,3,1],[1,3,1,1,1],[2,4,1,1,1],[2,2,1,2,2],[5,2,1,2,2],[3,5,2,2,3],[2,6,1,2,3],[5,6,1,2,3]],
  [[0,0,3,7,0],[3,1,1,5,0],[4,2,1,3,0],[0,7,3,1,1],[3,6,1,1,1],[4,5,1,1,1],[2,2,2,1,2],[2,5,2,1,2],[5,3,2,2,3],[6,2,2,1,3],[6,5,2,1,3]],
  [[5,0,3,7,0],[4,1,1,5,0],[3,2,1,3,0],[5,7,3,1,1],[4,6,1,1,1],[3,5,1,1,1],[4,2,2,1,2],[4,5,2,1,2],[1,3,2,2,3],[0,2,2,1,3],[0,5,2,1,3]],
  [[1,0,7,8,0],[0,0,1,8,1]],
  [[0,0,8,7,0],[0,7,8,1,1]],
  [[1,0,7,7,0],[0,0,1,6,1],[1,6,1,1,1],[2,7,6,1,1]],
  [[0,0,7,7,0],[7,0,1,5,0],[0,0,1,1,1],[0,7,6,1,1],[6,6,1,1,1],[7,5,1,1,1]],
  [[1,1,7,7,0],[3,0,5,1,0],[0,2,1,6,1],[1,1,1,1,1],[2,0,1,1,1]],
  [[0,1,7,7,0],[0,0,6,1,0],[7,2,1,6,0],[0,7,1,1,1]],
  [[1,0,7,4,0],[2,4,5,2,0],[3,6,2,1,0],[0,0,1,4,1],[1,4,1,2,1],[2,6,1,1,1],[3,7,2,1,1],[5,6,1,1,1],[6,5,1,1,1],[7,3,1,1,1]],
  [[1,4,7,4,0],[2,2,5,2,0],[3,1,3,1,0],[4,0,1,1,0],[0,4,1,4,1],[1,2,1,2,1],[2,1,1,1,1],[3,0,1,1,1]],
  [[4,0,4,7,0],[2,1,2,5,0],[1,2,1,3,0],[0,3,1,1,0],[0,4,1,1,1],[1,5,1,1,1],[2,6,2,1,1],[4,7,4,1,1]],
  [[0,0,4,7,0],[4,1,2,5,0],[6,2,1,3,0],[7,3,1,1,0],[0,7,4,1,1],[4,6,2,1,1],[6,5,1,1,1],[7,4,1,1,1]],
  [[1,2,5,5,3],[0,3,1,3,3],[2,7,3,1,3],[6,3,1,3,3],[2,1,1,1,3],[3,0,1,3,4],[4,0,2,2,4],[2,3,1,1,2]],
  [[0,0,8,8,5],[1,1,2,2,6],[4,0,2,2,6],[3,3,2,2,6],[2,4,2,2,6],[6,5,2,2,6],[1,6,2,1,7],[6,2,2,1,7],[5,5,2,1,7]]
  ]

render_queue = []

screenx = 40
scale = 8
screeny = 28

for n in range(screenx):
  for j in range(screeny):
    for k in graphics[15]:
      fill_rect((n * scale) + k[0],(j * scale) + k[1],k[2],k[3],colors[k[4]])

delta = monotonic()
move_speed = 1/2
move_time = 0

apple = [0,0]
ate_apple = 0
while apple == snake[0]: 
  apple = [randrange(0,screenx-1),randrange(0,screeny-1)]
for k in graphics[14]:
  fill_rect((apple[0] * scale) + k[0],(apple[1] * scale) + k[1],k[2],k[3],colors[k[4]])

dead = 0

while not dead:
  #randomize
  seed(int(randrange(0,100)))
  
  #update time
  move_time = move_time + (monotonic()- delta)
  
  #reset variables
  delta = monotonic()
  
  #input
  if keydown(2) and [snake[len(snake)-1][0],snake[len(snake)-1][1] + 1] != snake[len(snake)-2]:
    direction = [0,1]
  if keydown(1) and [snake[len(snake)-1][0],snake[len(snake)-1][1] - 1] != snake[len(snake)-2]:
    direction = [0,-1]
  if keydown(3) and [snake[len(snake)-1][0] + 1,snake[len(snake)-1][1]] != snake[len(snake)-2]:
    direction = [1,0]
  if keydown(0) and [snake[len(snake)-1][0] - 1,snake[len(snake)-1][1]] != snake[len(snake)-2]:
    direction = [-1,0]
  
  if move_time > move_speed:
    #move
    snake.append([snake[len(snake)-1][0] + direction[0],snake[len(snake)-1][1]+direction[1]])
    head_direction = list(direction)
    
    #death logic
    snake_not_head = list(snake)
    del snake_not_head[len(snake_not_head)-1]
    if [snake[len(snake)-1][0],snake[len(snake)-1][1]] in snake_not_head:
      dead = 1
    elif snake[len(snake)-1][0] < 0 or snake[len(snake)-1][0] > screenx - 1 or snake[len(snake)-1][1] < 0 or snake[len(snake)-1][1] > screeny - 1:
      dead = 1
    if not dead:
      
      #apple logic
      if [snake[len(snake)-1][0],snake[len(snake)-1][1]] == [apple[0],apple[1]]:
        a = 1
        while a: 
          apple = [randrange(0,screenx-1),randrange(0,screeny-1)]
          if [apple[0],apple[1]] not in snake:
            a = 0
        ate_apple = 1
        render_queue.append([apple[0],apple[1],14])
      
      #remove tail
      if ate_apple == 0:
        render_queue.append([snake[0][0],snake[0][1],15])
        del snake[0]
      else:
        #only update when apple is eaten
        move_speed = 1/2*(1/(len(snake)**(1/2)))
        ate_apple = 0
      
      #draw head
      if head_direction == [1,0]:
        render_queue.append([snake[len(snake)-1][0],snake[len(snake)-1][1],2])
      if head_direction == [-1,0]:
        render_queue.append([snake[len(snake)-1][0],snake[len(snake)-1][1],3])
      if head_direction == [0,1]:
        render_queue.append([snake[len(snake)-1][0],snake[len(snake)-1][1],1])
      if head_direction == [0,-1]:
        render_queue.append([snake[len(snake)-1][0],snake[len(snake)-1][1],0])
      
      #turn ex_head into body
      head = [snake[len(snake)-1][0] - snake[len(snake)-2][0], snake[len(snake)-1][1] - snake[len(snake)-2][1]]
      ex_ex_head = [snake[len(snake)-3][0]-snake[len(snake)-2][0],snake[len(snake)-3][1] - snake[len(snake)-2][1]]
      if head == [1,0] and ex_ex_head == [-1,0] or head == [-1,0] and ex_ex_head == [1,0]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],5])
      if head == [0,1] and ex_ex_head == [0,-1] or head == [0,-1] and ex_ex_head == [0,1]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],4])
      if head == [0,-1] and ex_ex_head == [-1,0] or head == [-1,0] and ex_ex_head == [0,-1]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],7])
      if head == [0,-1] and ex_ex_head == [1,0] or head == [1,0] and ex_ex_head == [0,-1]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],6])
      if head == [0,1] and ex_ex_head == [-1,0] or head == [-1,0] and ex_ex_head == [0,1]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],9])
      if head == [0,1] and ex_ex_head == [1,0] or head == [1,0] and ex_ex_head == [0,1]:
        render_queue.append([snake[len(snake)-2][0],snake[len(snake)-2][1],8])
      
      #tail
      tail_direction = [snake[1][0] - snake[0][0], snake[1][1] - snake[0][1]]
      render_queue.append([snake[0][0],snake[0][1],15])
      if tail_direction == [0,-1]:
        render_queue.append([snake[0][0],snake[0][1],10])
      if tail_direction == [0,1]:
        render_queue.append([snake[0][0],snake[0][1],11])
      if tail_direction == [1,0]:
        render_queue.append([snake[0][0],snake[0][1],12])
      if tail_direction == [-1,0]:
        render_queue.append([snake[0][0],snake[0][1],13])
      
      #render
      for n in render_queue:
        for k in graphics[n[2]]:
          fill_rect((n[0] * scale) + k[0],(n[1] * scale) + k[1],k[2],k[3],colors[k[4]])
      render_queue = []
      #reset move clock
      move_time = 0
      print(1/(monotonic()-delta))
      print(len(snake))
      print("")

print("you died")
