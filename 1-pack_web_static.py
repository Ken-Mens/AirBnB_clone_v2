#!/usr/bin/python3
"""
Compress before sending
"""
from fabric.api import *
from datetime import datetime, date


def do_pack():
    """creates a .tgz file
    """
    time_var = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(time_var)
    try:
        local("mkdir -p ./versions")
        local("tar -czvf {} ./web_static".format(path))
        return path
    except:
        return None
