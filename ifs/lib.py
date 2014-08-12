import urllib
import subprocess

def download(url, filename):
    # Add progress bar via:
    # http://stackoverflow.com/a/22776/317916
    urllib.urlretrieve(url, filename)

def bash(command):
    try:
        return subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        return False