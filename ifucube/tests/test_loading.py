import pytest
from astropy import units as u

from ifucube.ifucubelist import IFUList

filename = 'ifucube/tests/data/data_cube.fits.gz'


def test_load():
    ifulist = IFUList.read(filename)

    # Correct length
    assert len(ifulist) == 2

    # Right amount of data
    assert ifulist[0].data.shape == (2048, 17, 17)

    # Right amount of data
    assert ifulist[1].data.shape == (2048, 17, 17)

    assert ifulist[0].wavelength(12, 34, 34).value == pytest.approx(1.9345*10**-6, rel=0.0001)
    assert ifulist[0].wavelength(12, 34, 34).unit == u.m