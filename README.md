# ifs

Install from source. When the version in the package manager has gone stale, get a fresh, production-ready version from a source tarball or precompiled archive.

These scripts currently target Ubuntu 14.04.

## Example

Install nginx

    pip install --upgrade ifs
    ifs install nginx
    ifs install redis
    ifs install riak
    ifs install mongodb
    etc.

Run `ifs` to see all commands and `--help` on any command to see additional information.

## Install from source

(It's so meta)

    git clone https://github.com/cbednarski/ifs.git
    pip install -e ifs

## Install for development

    pip install --upgrade virtualenv
    git clone https://github.com/cbednarski/ifs.git
    make test
