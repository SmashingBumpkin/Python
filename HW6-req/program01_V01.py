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
#pytest test_01.py -v -rA


import images


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:

# def generate_snake(start_img, position, commands, out_img):

    image = images.load(start_img)
    commands = commands.split()
    
    org = (255, 128, 0) # food
    red = (255, 0, 0) # obstacle
    gry = (128, 128, 128) # snake trail
    grn = (0, 255, 0) # snake
    blk = (0, 0, 0) #background
    
    sizeY = len(image)
    sizeX = len(image[0])
    l = 1
    
    comMap = {"S" : (1,0,0),
              "E" : (0,1,0),
              "N" : (-1,0,0),
              "W" : (0,-1,0),
              "NW" : (-1,-1,1),
              "SW" : (1,-1,1),
              "SE" : (1,1,1),
              "NE" : (-1,1,1)}
    
    #read next command
    #get next coordinates
    #check if next coordinates are a legal input from current head position
    #if S N E W chec
    #if input ok:
    #   add to head of snake, and paint the position orange
    #if not food, remove from tail of snake and replace
    
    headY, headX = position[1], position[0]
    snake = [[headY,headX]]
    
    
    #print(commands)
    for coms in commands:
        com = comMap[coms]
        
        diffY, diffX = comMap[coms][0],comMap[coms][1]
        nextY, nextX = headY + diffY, headX + diffX
        if abs(nextY) == sizeY:
            nextY = 0
        if abs(nextX) == sizeX:
            nextX = 0
        
        if image[nextY][nextX] == grn or image[nextY][nextX] == red:
            if [nextY, nextX] != snake[0]:
                tailY, tailX = snake[0]
                image[tailY][tailX] = gry
                break # gameover
        diagCheck = [image[headY][nextX],image[nextY][headX]]
        if com[2] and diagCheck == [grn,grn]:
        #if com[2] and image[nextY][headX] == grn and image[headY][nextX] == grn:
            tailY, tailX = snake.pop(0)
            image[tailY][tailX] = gry
            break #gameover
        
        if image[nextY][nextX] == org:
            l+=1
        else:
            tailY, tailX = snake.pop(0)
            image[tailY][tailX] = gry
        
        headY, headX, image[nextY][nextX] = nextY, nextX, grn
        snake.append([nextY,nextX])
        
    images.save(image, out_img)
        
    return l


if __name__ == '__main__':
    #generate_snake("./data/input_00.png", [12, 13], "S W S W W W S W W N N W N N N N N W N", "./output_end_00.png")
    #command = "S S E E E E E N N N N N E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E N N N N N N N N N N N N N N N N N N E N N N N N N N N E E E E E S S E S S E S E S S S SE SE SE SE SE SE SE SE SE NE NE NE SE NE SE NE NE NE NE NE N NE NE NE N N N N E E E E S S S S S S S S S S S S S S S W N E SW NW E S SE W E E SE SE NE W E S S E SE N SW W SE N SE S NE NE W S NE S E NW S NE N E E E NE S SE W W E S W SE E N NE S SW E SW W NW E SE N NE S S SW S SW N NW NE E N N NE SW S SE E NW NE NE NW S SE W SW SE W SE E S W N N S SW SW SW S NE E E N N S SE N NW W E NE NE S W SW N E W S W NW S S NE S E S NW SE N W SE S SE NE S N SW W SW S NE W N SW NE SE NW W S W SW SW E SE SE S NE W S W W SE NE S NW NE E S E SW S NW SE SE S N W NE NE N W W NW E W NW SE S S S S NW W SW N W S N NE N NW S S NW E SW E E N W NW W S W E W W SE SE NE SW W SW SW SE N NE N W W S N SE SE S S S SE W SE SE SW N SW NE W SW E NW SE SW SW SW SE NW SE S W NE W SW S E W W N S E S SW E N NW SW S E S W E S SE N SE E SW E SE S SW SW SE E SW NW S W SW N SE SW S E E E N SE SE N S S NE N SW SW E S W E E S NW NW E W SW SE W NE SE E NE S E N W NW W SE S NE W SW N S NW NW NW SE NE W SW NW S SW NW SW SW SW S E S NE SW W S W E E S N S N E S W SE NW W S NW S NW SE W S NE SE E NE SE SE SE S SE SE N E NE NE S SW N NW N S N SW SE S S SE W E E NE E S NW N E W W S N N E SE W S E S S E S SE S S E N E NW N W N N SE S SW S NE S W SE W NW SW E NW SW SE NW SW W NE NW NE NW N NW S NE NE S S NE E N NW N W S W SW W W E S S E SW S W NE SW N S S S S SW SE S W E SE W NE S E S W W S W S NE N W N S S E W W SE SW S SE E SW S S SW NW E NE S S NW E SW S N NW NE W W E E S NE S NE S SE N N S S NW N NW SW E S SE S NE E NE SE NW S W SW SE NE NW S SE N NW SW E SE N SE S SE W N E W S S W SW N NW SW SE SE E N SW S NW NE N SW S SW NW S E E S N W E E NW E W S N S SE SE E NW W S NE S NW SE N W S E NW SW N S W E S SW SE E E NE NW S SW S SW S W SE SW NW E SW NW E NE NE NE N E NE N W S S SE S S NE N E SE W N E S S NW S NE NE SE N W S NW NE W SW N S NE W E S S S W SW N S W N W W SW NE NW S N SE N E NW N SE S E N SE N S N SW E N SE N NE E N E E NE SW NW N NE S NE NE NE SE SE E W W N SW N N S S E E S N S E E W N S NW W S S SE S N SW S W SW NE S SW SE SW S SE N SW S NW S W W E S E S S NE S S N S NE S SE NW SE S SW S S NW NW S E NW S SE SE SE SE NW N SW NE E S N NE S NW W S W W S N S S NW NW S S NW SW S E SE SW S SW NW N NW SW S"
    #generate_snake("./data/input_03.png", [1, 20], command, "./output/output_end_03.png")
    command = "S S S S E S S S E E E E E E E E E E E E E E E E E E N E N N N N E S E E E N W W N W W W S S E N E S E E N W N W W W W W W W W W W N N N N W N E E S S S S E E N E E S S S S W N N W W W W N W W W W N W S S S S W S W S W N W N E N N N W W W W S S S S S W W N N N W W N W W W S S S S S E E E E E E E S S S S S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S NW S SE SE SE SE SE SE SE SE NE NE S E E E E E E E E E E E E E E E E E E E NE NE NE NE NE S"
    generate_snake("./data/input_06.png", [28, 1], command, "./output/output_end_06.png")
    command = "NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE NE W W W W W W W S S S S S S S E S S N N N SW SW S W S N E S E W S N NW S SE W N S E SW SW S W E NW S S E E E SW S SE E NW N S NW S E NW SW E SE N SW NW NE S NE NE NE E N S S W E NE S S W SE NE SE E N SE SE SW S E S S NW E NW S S NE N NE NE W W SW NW N SW S NE S W S NE NW NW NW SW SE S SW NE S S N E E E NE S NE W E SW NW SW S NE SE W SW E NE NE NE S NW S NW S W SW SW N SE E SE NE S SE W SW S W SW N W NE S W W SE NE S E S N SW SW S E N SE SE S SW S NW SW E NW E E W S N S NW S W E S SE S N E E N SW SE E W S E S SW SE E NW W NW W N SW SW S E N SW NW SW W E NW E N E S N S SW E E S E NW NE NE SE S N S NE N NW W S S S SW E W NE W E S SE E N NE NE W SE SW NW SW E S E N SE E S NE S E NW S SW NW E S NW S SE NW NW S S S S SE N SE SE NE SE NE N SE NW NW NW NE SE NE S S N N S SW S W W E NE SW W N NE NW NW S S E SE E N E SW SE S NE N NW E E NE NE S S S NW W SW W S S N S E E S N S SE S W W SW SW W SW NW S SE E SE W NE W W S E NW SW N NW SW S NE SW SW SE S SW N W SW NE W NE NE NE NW S S S SW NW S N W S W NE S S S S W S"
    # generate_snake("./data/input_05.png",[32, 94], command , "./output/output_end_05.png")


    pass