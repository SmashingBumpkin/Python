# task 1: write a function that rotates an image provided by parameter by 90 degrees
# clockwise; the function modifies the image in-place, so it does not
# return anything

# task 2: write a function that rotates an image provided by parameter by 90 degrees
# clockwise; the function modifies the image in-place, so it does not
# return anything; you cannot allocate any auxiliary image inside the function!

import pngmatrix

def RotateImage_task1(image : list) -> None:
    print(len(image))
    newImg = []
    for y in range(len(image)):
        newImg.append([])
        for x in range(len(image[0])):
            newImg[y].append(image[x][y])
    for y in range(len(image)):
        for x in range(len(image[0])):
            image[y][x] = newImg[y][x]

    pass

def RotateImage_task2(image : list) -> None:
    
    pass

if __name__ == "__main__":
    RotateImage_task1([[0,1,2],[3,4,5],[6,7,8]])
    img = pngmatrix.load_png8("Shape+Square+Clipart-881591175.png")
    RotateImage_task1(img)
    pngmatrix.save_png8(img, "result1.png")
    RotateImage_task2(img)
    pngmatrix.save_png8(img, "result2.png")