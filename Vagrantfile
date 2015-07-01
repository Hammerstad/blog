# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64server"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 5555, host:9500		# When running from manage.py

  config.vm.provision :shell, :inline => "mkdir /home/vagrant/.vimtmp -p"
  config.vm.provision :shell, :inline => "cp /vagrant/conf/.bashrc /home/vagrant"
  config.vm.provision :shell, :inline => "cp /vagrant/conf/.vimrc /home/vagrant"
  config.vm.provision :shell, :path => "tools/bootstrap.sh" 
end