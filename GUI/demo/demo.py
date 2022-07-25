#### Initialize ####
import intp
from intp import *
d = vars(intp)
win = Intp.init()

#### Your code ####
Intp.create(Intp.read("demo.fs"))

#### Run ####
win.connect("destroy",exit)
win.resize(300,400)
Func.css("demo.css")
Intp.show()