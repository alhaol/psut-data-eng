curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository deb [arch=amd64] https://download.docker.com/linux/ubuntu stable
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo apt-get install docker-compose -y
sudo systemctl status docker
#sudo usermod -aG docker 
#su - 
#id -nG
#sudo usermod -aG docker root

