import httplib2
from keys import *
from math import floor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_board(url, empty_cell):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chromedriver_path, options=options)
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
        if cell == "empty" and empty_cell == 0: #unfilled cell, used for solving so must indicate value as 0
            cell = empty_cell
            row = floor(i / 9) #find row of cell by dividing by 9 and rounding down
            board[row].append(int(cell))
        elif cell == 'empty' and empty_cell =='': #unfilled cell, used for displaying so must indicate value as ''
            cell = empty_cell
            row = floor(i/9)
            board[row].append(cell)
        else: #filled cell, add to list
            row = floor(i/9)
            board[row].append(int(cell))
    driver.close()
    print(board)
    return(board)

def test_url(url):
    h = httplib2.Http()
    resp = h.request(url, 'HEAD')
    if int(resp[0]['status']) < 400:
        return True
    else:
        print('URL not working - please check again')
        return False

#TODO: Function to store list in database / text file