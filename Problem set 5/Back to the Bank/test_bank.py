from bank import value
def test_hello():
    assert value("hello")=="$0"
    assert value("Hello sinan")=="$0"
    assert value("Hello brother")=="$0"

def test_h():
    assert value("hi")=="$20"
    assert value("hey")=="$20"
    assert value("hola")=="$20"

def test_no():
    assert value("Whatsup")=="$100"
    assert value("sinan")=="$100"
    assert value("What do you need")=="$100"
    
