import nfc
import errno
import logging

Logger = logging.getLogger('main')
Logger.setLevel(logging.CRITICAL)

path = 'usb'
while True:
    try:
        clf = nfc.ContactlessFrontend(path)
    except IOError as error:
        if error.errno == errno.ENODEV:
            Logger.info(f"no contactless reader found on {path}")
        elif error.errno == errno.EACCES:
            Logger.info(f"access denied for device with path {path}")
        elif error.errno == errno.EBUSY:
            Logger.info(f"the reader on {path} is busy")
        else:
            Logger.debug(f"{repr(error)} when trying {path}")