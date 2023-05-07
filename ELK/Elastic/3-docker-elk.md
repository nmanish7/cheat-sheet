### Use ELK-DOCKER-COMPOSE File

[environment](env.env)  - *Remove the Name of the file and keep as .env*
[elasticsearch-docker-yaml](elasticsearch-docker.yml)
[kibana-docker](kibana-docker.yml)

---

### Docker Command to Run above Compose in Windows

#### Creating Docker Network
```shell
docker network create --subnet=192.168.1.0/24 --gateway=192.168.1.1 ELK_LOG_NETWORK
```

#### Setting Maximum number of memory map areas a process may have to 262144

```shell
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```


```shell
# Testing Docker Compose File
docker-compose -f .\elasticsearch-docker.yaml config
docker-compose -f .\kibana-docker.yaml config
```


```shell
# Generating Certificate for node es01 and es02
docker-compose -f .\elasticsearch-docker.yaml up setup
```

```shell
# Turning on the First Node of elasticsearch "es01"
docker-compose -f .\elasticsearch-docker.yml up es01
```

```shell
# Turning on the Second Node of elasticsearch "es02"
docker-compose -f .\elasticsearch-docker.yml up es01
```

```shell
# Setting up the Kibana_system password for Elasticsearch and Kibana Integration
# As the Password "kibana_password" present in the environment file so we set that password
# We use RESTful API to Set the password
curl -k -u elastic:abc@123 -XPUT 'https://localhost:9200/_security/user/kibana_system/_password' -H 'Content-Type: application/json' -d '{ "password": "kibana_password" }'
```

```shell
# Turning on the Kibana Container "kibana"
docker-compose -f .\kibana-docker.yml up
```

```shell
# Getting Elasticsearch TTY
docker exec -it -u 0 elasticsearch_01 bash
su elasticsearch
```