from flask import Flask, redirect, url_for, render_template
from scraper import get_board, test_url
from solver import main, nyt_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sudoku_easy')
def soduku_easy():
    url = nyt_url['easy']
    if test_url(url):
        board = get_board(url,empty_cell='')
        solved = main(get_board(url,empty_cell=0))
        return render_template('sudoku.html',board=board, solved=solved, header="Easy")

@app.route('/sudoku_medium')
def soduku_medium():
    url = nyt_url['medium']
    if test_url(url):
        board = get_board(url,empty_cell='')
        solved = main(get_board(url,empty_cell=0))
        return render_template('sudoku.html',board=board, solved=solved, header="Medium")

@app.route('/sudoku_hard')
def soduku_hard():
    url = nyt_url['hard']
    if test_url(url):
        board = get_board(url,empty_cell='')
        solved = main(get_board(url,empty_cell=0))
        return render_template('sudoku.html',board=board, solved=solved, header="Hard")

if __name__ == '__main__':
    app.run(debug=True)