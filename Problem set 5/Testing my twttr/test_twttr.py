from twttr import shorten

def test():
    assert shorten("Sinan")=="Snn"
    assert shorten("AAAaa")==""
    assert shorten("sdfg")=="sdfg"
    assert shorten("oooaaa")==""
