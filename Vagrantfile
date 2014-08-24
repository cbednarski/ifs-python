Vagrant.configure('2') do |config|
  config.vm.box = 'cbednarski/ubuntu-1404'
  config.vm.provision 'shell', inline: 'apt-get update -qq'
  config.vm.provision 'shell', inline: 'apt-get install -qy python-pip'
  config.vm.provision 'shell', inline: 'pip install -e /vagrant'
end
