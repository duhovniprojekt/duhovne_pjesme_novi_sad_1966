#!/usr/bin/env python3

from ms2ly_dom import *

xml_paths = {
    "chord" : "/museScore/Score/Staff/Measure/voice/Chord",
    "staff" : "/museScore/Score/Staff"
}

def getStaffId(node):
    staff = getParentNodeByPath(node, xml_paths['staff'])
    for attr in getAttributes(staff):
        if (attr[0] == 'id'):
            return attr[1]
    return None