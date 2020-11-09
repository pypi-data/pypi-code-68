'''
Whole pupilanalysis wide settings here.

Attributes
-----------

DEFAULT_FILENAME
'''

import os
import json

from pupilanalysis.directories import PUPILDIR


DEFAULT_SAVENAME = "pupilanalysis-settings.json"


def _load(fn):
    fullfn = os.path.join(PUPILDIR, fn)
    if os.path.isfile(fullfn):
        with open(fullfn, 'r') as fp:
            return json.load(fp)
    else:
        return {}

def _save(data, fn):
    with open(os.path.join(PUPILDIR, fn), 'w') as fp:
        json.dump(data, fp)


def set(key, value, fn=DEFAULT_SAVENAME):
    '''
    Set and save a setting.
    '''
    settings = _load(fn)

    settings[key] = value

    _save(settings, fn)


def get(key, default=None, fn=DEFAULT_SAVENAME):
    '''
    Get a setting.
    Specidy default for default value like in Python's standard get.
    '''
    settings = _load(fn)

    return settings.get(key, default)

