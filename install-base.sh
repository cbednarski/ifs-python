# Only apt-get update every 24 hours
echo 'APT::Update::Post-Invoke-Success {"touch /var/lib/apt/periodic/update-success-stamp 2>/dev/null || true";};' > /etc/apt/apt.conf.d/15update-stamp
now=`date +%s`
updated=`stat --printf %Y /var/lib/apt/periodic/update-success-stamp || 0`
expiry=$(($updated+86400))
if ((expiry < now)); then
  apt-get update && apt-get upgrade -y
fi

# Install base dependencies
apt-get install -y build-essential git vim curl tree