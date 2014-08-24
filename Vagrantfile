Vagrant.configure('2') do |config|
  config.vm.box = 'cbednarski/ubuntu-1404'
  config.vm.provision 'shell', inline: 'apt-get update'
  config.vm.provision 'shell', inline: 'apt-get install -y python-pip'
  config.vm.provision 'shell', inline: 'pip install -e /vagrant'
end
