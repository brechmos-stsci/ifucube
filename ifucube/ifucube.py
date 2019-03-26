"""IFUCube is one instance of a 3D IFU dataset"""

from astropy import units as u
from traitlets import HasTraits, Unicode, Instance, Dict, validate

from .wavelength import Wavelength, WavelengthLinearModel


class IFUCube(HasTraits):

    # Create a mapping from what we don't want to what we want.
    # The search is case sensitive...
    unit_mapping = [
        ('Ang', 'A'),
        ('Spaxel', 'pixel'),
        ('spaxel', 'pixel'),
    ]

    _name = Unicode()
    unit = Instance(u.UnitBase)
    _wavelength = Instance(Wavelength)
    _other_header = Dict()

    @classmethod
    def constructFromHDU(cls, hdu, wavelength=None):
        """
        Create an IFUCube from the HDU read in. It should have a
        reasonably normal header and 3D data otherwise will error.

        :param hdu:
        :param wavelength:
        :return:
        """

        if wavelength is None:
            wavelength = Wavelength.constructFromHDU(hdu)

        # TODO MORE HERE
        name = hdu.header.get('EXTNAME', '')
        data = hdu.data  # should check that it exists
        unit = hdu.header.get('BUNIT', '') # auto convert to u.dimensionless
        other_header = dict(hdu.header)

        return cls(name, data, unit, other_header, wavelength)

    @classmethod
    def constructFromASDF(cls, tree, wavelength_tree=None):
        # TODO: Look at ASDF tag mechanism
        name = 'asdf'
        data = 3
        unit = u.AA
        other_header = {}
        wavelength = WavelengthLinearModel()

        return cls(name, data, unit, other_header, wavelength)

    def __init__(self, name=None, data=None, unit=None, other_header=None, wavelength=None):

        self._name = name
        self.unit = unit
        self._data = data
        self._other_header = other_header
        self._wavelength = wavelength

        self.unit.on_trait_change(self._unit_changed, 'unit')

    # @property
    # def unit(self):
    #     return self._unit
    #
    # @unit.setter
    # def unit(self, value):
    #     print('Entering unit setter with {}'.format(value))
    #
    #     # If this is a string coming in, then let's first
    #     # fix any issues based on the mapping.
    #     for m in IFUCube.unit_mapping:
    #         if not m[0]:
    #             continue
    #
    #         print('    converting {} to {}'.format(*m))
    #         value = value.replace(m[0], m[1])
    #
    #     # TODO: Do checks here that the units are valid
    #     print('unit: going to set to {}'.format(value))
    #     self._unit = u.Unit(value)

    def _unit_changed(self, old, value):

        # If this is a string coming in, then let's first
        # fix any issues based on the mapping.
        for m in IFUCube.unit_mapping:
            if not m[0]:
                continue

            print('    converting {} to {}'.format(*m))
            value = value.replace(m[0], m[1])

        # TODO: Do checks here that the units are valid
        print('unit: going to set to {}'.format(value))
        self._unit = u.Unit(value)
        return self._unit

    @property
    def name(self):
        return self._name

    @property
    def other_header(self):
        return self._other_header

    @property
    def data(self):
        return self._data

    @property
    def wavelength(self):
        return self._wavelength

    def __str__(self):
        return 'IFUCube {} {}'.format(
            self._name,
            self._data.shape
        )
