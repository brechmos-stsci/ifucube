from astropy.io import fits

from ifucube import IFUCube

filename = '/Users/crjones/Documents/DATB/cubeviz/data/manga-7495-12704-LOGCUBE.fits.gz'

c = IFUCube()

c.open(filename)
