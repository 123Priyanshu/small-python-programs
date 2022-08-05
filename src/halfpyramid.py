def halfPyramid(height):
    for x in range(1, height+1):
        print(x*"*")
    #if height < 4 or height > 9:
        #print(f'The input is supposed to be from 4 to 10. Your input was {height}.')
        #return

    # If height value is 6
    # Output should be
    #
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *


halfPyramid(9)
