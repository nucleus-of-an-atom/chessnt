[
    {
        "name": "root",
        "type": "Box",
        "class": [
            "root"
        ],
        "args":[
            ["orientation","Gtk.Orientation.VERTICAL"],
            ["spacing",10]
        ],
        "parent":"win",
        "addby":"add"
    },
    {
        "name": "obj1",
        "type": "Button",
        "class": [
            "test"
        ],
        "args": [
            ["label","'Test'"]
        ],
        "parent":"root",
        "addby":"pkgstart"
    },
    {
        "name": "obj2",
        "type": "Button",
        "class": [
            "test"
        ],
        "args": [
            ["label","'Test 2.0'"]
        ],
        "parent":"root",
        "addby":"pkgend"
    }
]