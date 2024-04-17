import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

pygame.init()
def calculator():
    a=float(input("1_num"))
    b=float(input("2_num"))
    s=input("+,-,*,/:")
    if s=='+':
        print(a+b)
    elif s=='-':
        print(a-b)
    elif s=='*':
        print(a*b)
    elif s=='/':
        if b!=0:
            print(a/b)
        else:
            print ("error,try again")

pygame.display.flip()