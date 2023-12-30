import pyautogui as pag
import time
from solver import solve
from scrape_sides import scrape

def autogui(sols):
    #switch to letterboxed window (set up beforehand silly)
    pag.hotkey('command', 'tab', interval = 0.25)
    
    for sol in sols[:1]:
        enter_sol(sol)
    

def enter_sol(sol):
    #type a solution into the letterboxed window
    pag.write(sol[0])
    time.sleep(0.25)
    pag.press('enter')
    time.sleep(3)
    pag.write(sol[1][1:])
    pag.press('enter')



if __name__ == '__main__':
    test1 = [('calmed', 'driveways')]

    URL = 'https://www.nytimes.com/puzzles/letter-boxed'
    sides = scrape(URL)
    sols = solve([list(tri.lower()) for tri in sides])
    autogui(sols)