# Node.js
if brew -v && ! node -v; then
  brew install nodejs
  exit
fi

if ! node -v ; then
  cd /tmp
  wget -q http://nodejs.org/dist/v0.10.28/node-v0.10.28-linux-x64.tar.gz
  tar --strip-components 1 -C /usr/local -xzf /tmp/node-v0.10.28-linux-x64.tar.gz
fi