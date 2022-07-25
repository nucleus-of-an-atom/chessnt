#### Initialize ####
from shutil import move
import intp,gi, chess,time
from stockfish import Stockfish
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk,GLib
from intp import *
d = vars(intp)
win = Intp.init()

#### Your code ####
count = 1
stockfish = Stockfish(path="../stockfish")
Intp.create(Intp.read("gui.json"))

items = {
    "r":"♖",
    "n":"♘",
    "b":"♗",
    "q":"♔",
    "k":"♕",
    "p":"♙",
    "K":"♚",
    "Q":"♛",
    "R":"♜",
    "B":"♝",
    "N":"♞",
    "P":"♟"
}

def make_matrix(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

brd = chess.Board()

for i in range(1,9):
    lbl = Gtk.Label(label=9-i)
    lbl.get_style_context().add_class("posY")
    d["lpos"].pack_start(lbl,False,True,0)

    lbl2 = Gtk.Label(label=["","a","b","c","d","e","f","g","h"][i])
    lbl2.get_style_context().add_class("posA")
    d["bpos"].pack_start(lbl2,False,True,0)

def clearBoard():
    for each in d["board"].get_children():
        d["board"].remove(each)

def updateBoard(brd):
    board = make_matrix(brd)

    for i in range(0,len(board)):
        for n in range(len(board[i])):
            if board[i][n]==".":
                lbl=Gtk.Label(label="")
                lbl.get_style_context().add_class("posX")
                d["board"].attach(lbl,n,i,1,1)
            else:
                lbl=Gtk.Label(label=items[str(board[i][n])])
                lbl.get_style_context().add_class("posX")
                d["board"].attach(lbl,n,i,1,1)

updateBoard(brd)

def turn():
    if brd.turn:
        return "Black"
    else:
        return "White"

def stockfishM():
    global brd,count
    stockfish.set_fen_position(str(brd.fen).split("'")[1])
    bmove=stockfish.get_best_move()
    brd.push(chess.Move.from_uci(bmove))
    d["mvL"].add(Gtk.Label(label=f"{count}. {turn()} => {bmove}"))
    clearBoard()
    updateBoard(brd)
    win.show_all()
    count += 1

def on_activate_move(w):
    global brd, count
    move = chess.Move.from_uci(w.get_text())
    if move in list(brd.legal_moves):
        brd.push(move)
        d["mvL"].add(Gtk.Label(label=f"{count}. {turn()} => {w.get_text()}"))
        clearBoard()
        updateBoard(brd)
        win.show_all()
        GLib.timeout_add_seconds(2,stockfishM)
    else:
        d["mvL"].add(Gtk.Label(label="Illegal Move"))   
        win.show_all()
    w.set_text("")

d["move"].connect("activate",on_activate_move)

#### Run ####
win.connect("destroy",exit)
win.resize(1000,600)
win.set_decorated(False)
Func.css("gui.css")
Intp.show()