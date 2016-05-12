Vagrant.configure('2') do |config|
  config.vm.box = 'cbednarski/ubuntu-1604'
  config.vm.provision 'shell', inline: 'apt-get update -qq'
  config.vm.provision 'shell', inline: 'apt-get install -qy python3-pip'
  config.vm.provision 'shell', inline: 'pip3 install -e /vagrant'
end
