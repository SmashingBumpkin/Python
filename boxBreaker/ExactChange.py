import time



def exactChange(a, b, c, w):
    cfactor = w//c
    cRemainder = w % c
    for ic in range (cfactor+1):
        bremainder = ic*c + cRemainder
        while bremainder > 0:
            if bremainder % a == 0:
                return True
            bremainder -= b
            
            
    return False

def exactChange2(a, b, c, w):
    cfactor = w//c
    cRemainder = w % c
    bremPri = cRemainder - c
    for ic in range (cfactor+1):
        bremPri += c
        bremainder = bremPri
        while bremainder > 0:
            if bremainder % a == 0:
                return True
            bremainder -= b
            
            
    return False


start_time = time.time()
print(exactChange(2,4,102,200001))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")

start_time = time.time()
print(exactChange2(2,4,102,200001))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")