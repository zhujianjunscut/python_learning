def test_print():
    print("test_print")



def test_dir():
    d = {}
    d["name"] = "zjj"
    d["age"] = 42
    print(d)
    y = d
    yy = d.copy()
    print (y)
    y.clear()
    print( d,"\n", y,"\n",d, yy)

def test_dir_fun():
    d = {}.fromkeys(["name","age"],"40")
    print (d)
    d2 = {}
    print (d2.get("name"))
    print (d.items())
    it = d.items()
    print (it)
    list(it)
    d.pop("name")
    print (d)
    d.setdefault("name","zjj")
    print (d)
    key,value = d.popitem()
    print (key, value)
    pass

def test_os():
    import os
    print(os.name)
    pass






test_os()
test_print()
test_dir_fun()

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
#test_dir()