import gi, json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class Var():
    pass

class Func():
    def css(file:str):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        provider.load_from_path(file)
    def create(obj:str,name:str,prt:str,addby:str):
        exec(f'globals()["{name}"]=Gtk.{obj}()')
        if addby == "add":
            exec(f'globals()["{prt}"].add(globals()["{name}"])')
        elif addby == "pkgstartF":
            exec(f'globals()["{prt}"].pack_start(globals()["{name}"],True,True,0)')
        elif addby == "pkgendF":
            exec(f'globals()["{prt}"].pack_end(globals()["{name}"],True,True,0)')
        elif addby == "pkgstartNF":
            exec(f'globals()["{prt}"].pack_start(globals()["{name}"],False,True,0)')
        elif addby == "pkgendNF":
            exec(f'globals()["{prt}"].pack_end(globals()["{name}"],False,True,0)')
        return globals()[name]
    def argParse(name:str,argsList):
        for arg in argsList:
            argX,argY = arg[0],arg[1]
            exec(f'globals()["{name}"].{argX}({argY})')
    def cssParse(name:str,cssList):
        for _class in cssList:
            exec(f'globals()["{name}"].get_style_context().add_class("{_class}")')

class Intp():
    def read(file:str):
        with open(file,"r") as ctn:
            return json.load(ctn)
    def create(ctn:list):
        for obj in ctn:
            Func.create(obj["type"], obj["name"], obj["parent"],obj["addby"])
            Func.argParse(obj["name"],obj["args"])
            Func.cssParse(obj["name"], obj["class"])
    def init():
        globals()["win"] = Gtk.Window()
        return globals()["win"]
    def show():
        globals()["win"].show_all()
        Gtk.main()
    pass