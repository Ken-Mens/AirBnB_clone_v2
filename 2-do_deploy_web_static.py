#!/usr/bin/python3
""" Deploy archive"""
import os
from fabric.api import *
env.hosts = ['34.73.28.199', '35.229.73.92']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    put(archive_path, "/tmp/{}".format(filename))

    try:
        run("mkdir -p /data/web_static/releases/{}".format(filename))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(filename, filename))

        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}"
            .format(filename, filename))

        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename))

        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except:
        return False
