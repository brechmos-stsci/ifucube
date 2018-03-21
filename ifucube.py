import os
import logging

from astropy.io import fits

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('ifcube')
log.setLevel(logging.DEBUG)


class IFUCube(object):
    """
    Check the IFUCube
    """

    def __init__(self):
        pass

    def check(self, filename, fix=False):
        """
        Check all checkers
        """
        log.debug('In check with filename {} and fix {}'.format(filename, fix))

        # Check existence of the file
        if not os.path.isfile(filename):
            log.warning('File {} does not exist'.format(filename))
            return
        else:
            log.info('File {} exists'.format(filename))

        # Open the file
        try:
            fits_file = fits.open(filename)
        except:
            log.warning('Could not open {} '.format(filename))
            return

        # Do all the checks
        methods = [getattr(self, method_name) 
                   for method_name in dir(self) 
                   if callable(getattr(self, method_name)) and 
                      method_name.startswith('check_')]

        for method in methods:
            method(fits_file, fix)

    def check_data(self, fits_file, fix=False):
        """
        Check CTYPE and make sure it is the correct value

        :param: fits_file: The open fits file
        :param: fix: boolean whether to fix it or not
        :return: boolean whether it is good or not
        """
        log.debug('In check_data')
        good = True

        if not hasattr(fits_file[0], 'data'):
            good = False
            log.warning('  data does not exist')

            if fix:
                log.error('  Can\'t fix lack of data')
                return False
        else:
            log.info('  data exists and is of shape {}'.format(
                fits_file[0].data.shape))

        return good

    def check_ctype(self, fits_file, fix=False):
        """
        Check CTYPE and make sure it is the correct value

        :param: fits_file: The open fits file
        :param: fix: boolean whether to fix it or not
        :return: boolean whether it is good or not
        """
        log.debug('In check_ctype')
        good = True

        if 'CTYPE1' not in fits_file[0].header:
            good = False
            log.warning('  CTYPE1 does not exist')

            if fix:
                log.info('  Fixing')
                fits_file[0].header['CTYPE1'] = 0
        else:
            log.info('  CTYPE1 exists and is {}'.format(
                fits_file[0].header['CTYPE1']))

        return good
