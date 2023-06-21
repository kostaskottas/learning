
def triangle(size):
    if size > 0:
        #triangle(size-1) 
        print((" " *(13-(size))), "*"*(2*(size-1)-1))
        triangle(size-1)  #reverce triangle
        

triangle(12)