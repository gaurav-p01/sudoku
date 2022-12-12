import pygame

WIDTH = 500
HEIGHT = 500

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hello")

run = True
color = "#000000"

sudoku = []
txt = [""]

pygame.font.init()

unsolved = ""
text = "046109200002064000001352800008000042003800579069000000607098000000013000910400006"

def make_sudoku():
    k=0
    try:
        for i in range(9):
            sudoku.append([])
            for j in range(9):
                sudoku[i].append(int(unsolved[k]))
                k+=1
        return True
    except:
        return False
        

def make_text():
    t = ""
    for i in range(9):
        for j in range (9):
            t+=str(sudoku[i][j])
    txt[0] = t


def is_correct(n,r,c):
    if (n in sudoku[r]):
        return False
    for x in range(9):
        if sudoku[x][c] == n:
            return False

    r = (r//3)*3
    c = (c//3)*3

    for x in range(r, r+3):
        for y in range(c,c+3):
            if sudoku[x][y] == n:
                return False

    return True



def solve():
    for i in range(9):
        for j in range (9):
            if(sudoku[i][j] == 0):
                for a in range (1,10):
                    if(is_correct(a,i,j)):
                        sudoku[i][j] = a
                        solve()
                    sudoku[i][j] = 0
                return
    make_text()
    return



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_BACKSPACE):
                text = text[:-1]
            elif(event.key == pygame.K_RETURN):
                sudoku = []
                txt[0] = text
                unsolved = text
                success = make_sudoku()
                if success:
                    solve()
                    text = txt[0]
            else:
                text+=event.unicode

        rect = pygame.Rect(25,25,450,450)
        pygame.draw.rect(SCREEN, "#ffff99", rect)
        font = pygame.font.SysFont(None, 30)

        # for i in range (9):
        #     pygame.draw.line(SCREEN, "#000000", (0, i*BLOCK_WIDTH), (WIDTH, i*BLOCK_WIDTH))



        k=0
        if(len(text)>0):
            n = text[0]
            for i in range (9):
                for j in range(9):
                    img = font.render(n, True, color)
                    SCREEN.blit(img, (25 + j*(50),25 + (i)*50))
                    if(k+1 < len(text)):
                        k+=1
                        n = text[k]
                    else:
                        n = " "
                    
            


    

    if pygame.mouse.get_pressed()[0]:
        color = "#ff9999"
    
    if pygame.mouse.get_pressed()[2]:
        color = "#d8bfff"
    
    
    pygame.display.update()




pygame.quit()
