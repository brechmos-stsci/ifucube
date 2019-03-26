"""Define Wavelength classes to represent and access different Wavelength types"""

import abc
import logging

from astropy.wcs import WCS


class Wavelength:
    """Base class that should not be used, only sub-classed."""

    @staticmethod
    def constructFromHDU(hdu):
        if True:
            return WavelengthLinearModel(hdu)
        else:
            return Wavelength1DArray(hdu)

    def __init__(self, *args, **kwargs):
        self.unit = None

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        # TODO: Do check here that the units are valid.
        self._unit = value


class WavelengthLinearModel(Wavelength):

    def __init__(self, hdu):
        """
        Create a WCS from the HDU passed in and use the WCS
        in order to determine the wavelength value as a position.

        :param hdu: HDU used to create the WCS
        """

        super().__init__()

        try:
            self._wcs = WCS(hdu)
        except Exception as e:
            logging.error('Issue with creating WCS from HDU {}'.format(
                hdu
            ))
            raise e

    def __call__(self, *args, **kwargs):
        """
        Going to assume at this point that 3 points are passed in.

        :param args:
        :param kwargs:
        :return:
        """
        super().__call__(*args, **kwargs)

        return self._wcs.pixel_to_world(*args)[1]

class WavelengthDataModel(Wavelength):

    def __index__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)


class Wavelength3DLookup(Wavelength):

    def __index__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)


class Wavelength1DLookup(Wavelength):

    def __index__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)

