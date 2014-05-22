# ifs

Install from source. When the version in the package manager has gone stale, get a fresh, production-ready version from a source tarball or precompiled archive.

Supports Ubuntu 14.04 as a target platform.

## Example

Install nginx

    install-base.sh   # apt-get update, install some deps
    install-nginx.sh  # Compile nginx from source
    cp nginx.conf /etc/nginx/nginx.conf
    cp upstart-nginx.conf /etc/init/nginx.conf
    start nginx

The API for this could be cleaner, but it works for now.