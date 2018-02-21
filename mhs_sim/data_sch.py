#
"""
data sch module
"""
from collections import namedtuple


Packages = namedtuple(
    'Packages', ['parcel_id', 'small_id', 'timestamp']
)
