from astropy.io import fits

from ifucube import IFUCube

#filename = '/Users/crjones/Documents/DATB/cubeviz/data/manga-7495-12704-LOGCUBE.fits.gz'
#filename = '../manga-7495-12704-LOGCUBE.fits.gz'
filename = '../helper_cubeviz/test_wcs_file.fits'
c = IFUCube()

c.check(filename)
