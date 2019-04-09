import logging

from astropy.io import fits

from .ifucube import IFUCube

FORMAT = "%(levelname)-8s %(filename)-10s %(lineno)-3d %(funcName)-12s%(message)s"
logging.basicConfig()
log = logging.getLogger('ifcube')
log.setLevel(logging.DEBUG)


class IFUList(list):
    """Container for IFUCube objects, but is just a list."""

    @classmethod
    def read(cls, filename):

        f = fits.open(filename)

        ifulist = []

        for hdui, hdu in enumerate(f):
            if hasattr(hdu, 'data') and hdu.data is not None and len(hdu.data.shape) == 3:
                cube = IFUCube.constructFromHDU(hdu)

                ifulist.append(cube)

        return cls(ifulist)

    def __str__(self):
        return '[' + ', '.join(['{}. {}'.format(ii, x.__str__()) for ii, x in enumerate(self)]) + ']'

    def __repr__(self):
        return self.__str__()