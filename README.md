IFUCube

Small class to read in an IFU cube dataset with some cleanup.

For example:
```buildoutcfg
>>> from ifucube import IFUList

>>> ifu_data = IFUList.read('ifucube/tests/data/data_cube.fits.gz')

>>> ifu_data
[<ifucube.ifucube.IFUCube object at 0x7f1dbbd2cba8>, <ifucube.ifucube.IFUCube object at 0x7f1dbc09bd68>]

```

This will not fix all issues, but hopefully will make it easier to read "not completely standard" data cubes.