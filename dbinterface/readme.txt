sudo docker build -p mysql-dock -f mysql-dockerfie
sudo docker run -p 3306:3306 mysql-dock
sudo docker build -t db-dock -f db-dockerfile .
sudo docker run -p 5000:5000 --network host db-dock
sudo docker build -t api-dock -f api-dockerfile .
sudo docker run --network host-p 5001:5001 api-dock
sudo docker build -t html-dock -f htmldocker .
sudo docker run -p 5002:5002 html-dock
