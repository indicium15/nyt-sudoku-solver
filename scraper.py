from keys import *
from math import floor
from selenium import webdriver
def get_board(url):    
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(url) #Initiate ChromeDriver and open webpage
    board = [ #Nested array board to pass to solving function
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for i in range(0, 81):      
        cell = driver.find_element_by_xpath('//div[@data-cell={}]'.format(i)).get_attribute('aria-label') #find int value of cell
        if cell == "empty": #unfilled cell
            cell = 0
        #print(cell)
        row = floor(i / 9) #find row of cell by dividing by 9 and rounding down
        board[row].append(int(cell)) #add cell to nested list
    driver.close()
    print(board)
    return(board)