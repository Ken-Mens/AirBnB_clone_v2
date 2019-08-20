#!/usr/bin/python3
"""
Full Deployment
"""
import os
import time
from fabric.api import local, run, hosts, env, put
env.hosts = ['34.73.28.199', '35.229.73.92']
env.user = 'ubuntu'


def do_pack():
    """
    do_pack - compresses the files
    """
    d_time = time.strftime("%Y%m%d%H%M%S")
    stored = "web_static_" + d_time + ".tgz"
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(stored))
        return ("versions/{}".format(stored))
    except:
        return None


def do_deploy(archive_path):
    """
    deploy
    """
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    put(archive_path, "/tmp/{}".format(filename))

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

    def deploy():
        try:
            ok_pack = do_pack()
            ok_deploy = do_deploy(ok_path)
            return ok_deploy
        except:
            return False
