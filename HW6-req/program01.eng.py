#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
You have just been hired at a video game software house and you have
to render the snake game on an image  by saving the final image of the
snake's path and returning the length of the snake.
Implement the generate_snake function that takes as input a path to an
image file, which is the starting image "start_img". The image can
contain black background pixels, obstacle for the snake as red pixels
and finally food as orange pixels. The snake must be drawn in green.
In addition you must draw in gray the trail that the snake leaves onto
its path. The function also takes as input the initial snake position,
"position" as a list of two integers X and Y. The commands of the
player on how to move the snake in the video game are available in a
string "commands."  The function must save the final image of the
snake's path to the path "out_img," which is passed as the last input
argument to the function. In addition, the function must return the
length of the snake at the end of the game.

Each command in "commands" corresponds to a cardinal sign, followed by
a space. The possible cardinal signs are:

| NW | N | NE |
| W  |   |  E |
| SW | S | SE |

corresponding to one-pixel snake movements such as:

| up-left     | up     | up-right     |
| left        |        | right        |
| bottom-left | bottom | bottom-right |

The snake moves according to the commands; in the case the snake
eats food, it increases its size by one pixel.

The snake can move from side to side of the image, horizontally and
vertically, this means that if the snake crosses a side of the image,
it will appear again from the opposite side.
The game ends when the commands are over or the snake dies. The snake
dies when:
- it hits an obstacle
- it hits itself so it cannot pass over itself
- crosses itself diagonally. As an examples, a 1->2->3-4 path like the
  one below on the left is not allowed; while the one on the right is
  OK.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

For example, considering the test case data/input_00.json
the snake starts from "position": [12, 13] and receives the commands
 "commands": "S W S W W S W N N W N N N N N W N" 
generates the image in visible in data/expected_end_00.png
and returns 5 since the snake is 5 pixels long at the
end of the game.

NOTE: "commands": "S W S W W S W N N W N N N N N W N

NOTE: Analyze the images to get the exact color values to use.

NOTE: do not import or use any other library except images.
'''


import images


# def generate_snake(start_img: str, position: list[int, int],
#                    commands: str, out_img: str) -> int:

def generate_snake(start_img, position, commands, out_img):
    org = (255, 128, 0) # food
    red = (255, 0, 0) # obstacle
    gry = (128, 128, 128) # snake trail
    grn = (0, 255, 0) # snake
    blk = (0, 0, 0)#background
    l = 1
    
    image = images.load(start_img)
    
    #read next command
    #get next coordinates
    #check if next coordinates are a legal input from current head position
    #if S N E W chec
    #if input ok:
    #   add to head of snake, and paint the position orange
    #if not food, remove from tail of snake and replace
    comMap = {"S" : (1,0,0),
              "E" : (0,1,0),
              "N" : (-1,0,0),
              "W" : (0,-1,0),
              "NW" : (-1,-1,1),
              "SW" : (1,-1,1),
              "SE" : (1,1,1),
              "NE" : (-1,1,1)}
    position[0], position[1] = position[1], position[0]
    commands = commands.split()
    snake = [position]
    head = position
    image[head[0]][head[1]] = grn
    nextHead = head
    print(commands)
    for coms in commands:
        print(coms)
        com = comMap[coms]
        
        nextHead = [head[0] + com[0], head[1] + com[1]]
        print(image[nextHead[0]][nextHead[1]])
        
        if image[nextHead[0]][nextHead[1]] == grn or image[nextHead[0]][nextHead[1]] ==  red:
            
            break # gameover
        if com[2] and (image[head[0]][head[1]+com[1]] and 
                       image[head[0]+com[1]][head[1]] ==
                       grn or red):
            break #gameover
        
        if image[nextHead[0]][nextHead[1]] == org:
            l+=1
        else:
            tailX, tailY = snake.pop(0)
            image[tailY][tailX] = gry
        image[nextHead[0]][nextHead[1]] = grn
        snake.append(nextHead)
    images.save(image, out_img)
        
    
    
    pass


if __name__ == '__main__':
    generate_snake("./data/input_00.png", [12, 13], "S W S W W W S W W N N W N N N N N W N", "./output_end_00.png")
