from ifucube import IFUCube

filename = '/Users/crjones/Documents/DATB/cubeviz/data/manga-7495-12704-LOGCUBE.fits.gz'

def test_load():
    c = IFUCube()
    c.open(filename)
    assert True
