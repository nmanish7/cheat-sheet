### Environment Variable

```shell
vim .env
```

```env
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=abc@123  

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=N9TBBf5XiJmBu1UxdDR6

# Version of Elastic products
STACK_VERSION=8.7.1

# Set the cluster name
CLUSTER_NAME=elasticsearch-cluster

# Set to 'basic' or 'trial' to automatically start the 30-day trial
LICENSE=basic

# Port to expose Elasticsearch HTTP API to the host
ES_PORT=9200
#ES_PORT=127.0.0.1:9200

# Port to expose Kibana to the host
KIBANA_PORT=5601
#KIBANA_PORT=80

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824

# Project namespace (defaults to the current folder name if not set)
#COMPOSE_PROJECT_NAME=myproject
```

---

### Elasticsearch Compose File

```yaml
version: "2.2"

  

services:

  setup:

    image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}

    volumes:

      - certs:/usr/share/elasticsearch/config/certs

    user: "0"

    command: >

      bash -c '

        if [ x${ELASTIC_PASSWORD} == x ]; then

          echo "Set the ELASTIC_PASSWORD environment variable in the .env file";

          exit 1;

        elif [ x${KIBANA_PASSWORD} == x ]; then

          echo "Set the KIBANA_PASSWORD environment variable in the .env file";

          exit 1;

        fi;

        if [ ! -f config/certs/ca.zip ]; then

          echo "Creating CA";

          bin/elasticsearch-certutil ca --silent --pem -out config/certs/ca.zip;

          unzip config/certs/ca.zip -d config/certs;

        fi;

        if [ ! -f config/certs/certs.zip ]; then

          echo "Creating certs";

          echo -ne \

          "instances:\n"\

          "  - name: es01\n"\

          "    dns:\n"\

          "      - es01\n"\

          "      - localhost\n"\

          "    ip:\n"\

          "      - 127.0.0.1\n"\

          > config/certs/instances.yml;

          bin/elasticsearch-certutil cert --silent --pem -out config/certs/certs.zip --in config/certs/instances.yml --ca-cert config/certs/ca/ca.crt --ca-key config/certs/ca/ca.key;

          unzip config/certs/certs.zip -d config/certs;

        fi;

        echo "Setting file permissions"

        chown -R root:root config/certs;

        find . -type d -exec chmod 750 \{\} \;;

        find . -type f -exec chmod 640 \{\} \;;

        echo "Waiting for Elasticsearch availability";

        until curl -s --cacert config/certs/ca/ca.crt https://es01:9200 | grep -q "missing authentication credentials"; do sleep 30; done;

        echo "Setting kibana_system password";

        until curl -s -X POST --cacert config/certs/ca/ca.crt -u "elastic:${ELASTIC_PASSWORD}" -H "Content-Type: application/json" https://es01:9200/_security/user/kibana_system/_password -d "{\"password\":\"${KIBANA_PASSWORD}\"}" | grep -q "^{}"; do sleep 10; done;

        echo "All done!";

      '

    healthcheck:

      test: ["CMD-SHELL", "[ -f config/certs/es01/es01.crt ]"]

      interval: 1s

      timeout: 5s

      retries: 120

  

    networks:

      ELK_NETWORK:

        ipv4_address: 192.168.1.200

  

  es01:

    container_name: elasticsearch_01

  

    depends_on:

      setup:

        condition: service_healthy

    image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}

    volumes:

      - certs:/usr/share/elasticsearch/config/certs

      - esdata01:/usr/share/elasticsearch/data

  

    ports:

      - ${ES_PORT}:9200

  

    environment:

      - node.name=es01

      - cluster.name=${CLUSTER_NAME}

      - cluster.initial_master_nodes=es01,es02

      - discovery.seed_hosts=es02

      - network.host=0.0.0.0

      - ELASTIC_PASSWORD=${ELASTIC_PASSWORD}

      - bootstrap.memory_lock=true

      - xpack.security.enabled=true

      - xpack.security.http.ssl.enabled=true

      - xpack.security.http.ssl.key=certs/es01/es01.key

      - xpack.security.http.ssl.certificate=certs/es01/es01.crt

      - xpack.security.http.ssl.certificate_authorities=certs/ca/ca.crt

      - xpack.security.transport.ssl.enabled=true

      - xpack.security.transport.ssl.key=certs/es01/es01.key

      - xpack.security.transport.ssl.certificate=certs/es01/es01.crt

      - xpack.security.transport.ssl.certificate_authorities=certs/ca/ca.crt

      - xpack.security.transport.ssl.verification_mode=certificate

      - xpack.license.self_generated.type=${LICENSE}

  

    mem_limit: ${MEM_LIMIT}

    ulimits:

      memlock:

        soft: -1

        hard: -1

    healthcheck:

      test:

        [

          "CMD-SHELL",

          "curl -s --cacert config/certs/ca/ca.crt https://localhost:9200 | grep -q 'missing authentication credentials'",

        ]

  

      interval: 10s

      timeout: 10s

      retries: 120

  

    networks:

      ELK_NETWORK:

        ipv4_address: 192.168.1.201

  

  es02:

    container_name: elasticsearch_02

  

    depends_on:

      - es01

    image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}

    volumes:

      - certs:/usr/share/elasticsearch/config/certs

      - esdata02:/usr/share/elasticsearch/data

    environment:

      - node.name=es02

      - cluster.name=${CLUSTER_NAME}

      - cluster.initial_master_nodes=es01,es02

      - discovery.seed_hosts=es01

      - bootstrap.memory_lock=true

      - xpack.security.enabled=true

      - xpack.security.http.ssl.enabled=true

      - xpack.security.http.ssl.key=certs/es02/es02.key

      - xpack.security.http.ssl.certificate=certs/es02/es02.crt

      - xpack.security.http.ssl.certificate_authorities=certs/ca/ca.crt

      - xpack.security.transport.ssl.enabled=true

      - xpack.security.transport.ssl.key=certs/es02/es02.key

      - xpack.security.transport.ssl.certificate=certs/es02/es02.crt

      - xpack.security.transport.ssl.certificate_authorities=certs/ca/ca.crt

      - xpack.security.transport.ssl.verification_mode=certificate

      - xpack.license.self_generated.type=${LICENSE}

    mem_limit: ${MEM_LIMIT}

    ulimits:

      memlock:

        soft: -1

        hard: -1

    healthcheck:

      test:

        [

          "CMD-SHELL",

          "curl -s --cacert config/certs/ca/ca.crt https://localhost:9200 | grep -q 'missing authentication credentials'",

        ]

      interval: 10s

      timeout: 10s

      retries: 120

  

    networks:

      ELK_NETWORK:

        ipv4_address: 192.168.1.202

  

volumes:

  certs:

    driver: local

  

  esdata01:

    driver: local

  

  esdata02:

    driver: local

  

networks:

  ELK_NETWORK:

    external:

      name: ELK_LOG_NETWORK
```


---

### Kibana Compose File

```yaml
version: "2.2"

  

services:

  kibana:

    container_name: kibana

    # depends_on:

    #   es01:

    #     condition: service_healthy

    image: docker.elastic.co/kibana/kibana:${STACK_VERSION}

    volumes:

      - certs:/usr/share/kibana/config/certs

      - kibanadata:/usr/share/kibana/data

    ports:

      - ${KIBANA_PORT}:5601

    environment:

      - SERVERNAME=kibana

      - ELASTICSEARCH_HOSTS=https://es01:9200

      - ELASTICSEARCH_USERNAME=kibana_system

      - ELASTICSEARCH_PASSWORD=${KIBANA_PASSWORD}

      - ELASTICSEARCH_SSL_CERTIFICATEAUTHORITIES=config/certs/ca/ca.crt

    mem_limit: ${MEM_LIMIT}

    healthcheck:

      test:

        [

          "CMD-SHELL",

          "curl -s -I http://localhost:5601 | grep -q 'HTTP/1.1 302 Found'",

        ]

      interval: 10s

      timeout: 10s

      retries: 120

    networks:

      ELK_NETWORK:

        ipv4_address: 192.168.1.203

  

volumes:

  certs:

    driver: local

  kibanadata:

    driver: local

  

networks:

  ELK_NETWORK:

    external:

      name: ELK_LOG_NETWORK
```

---

### Docker Command to Run above Compose in Windows

```shell
# Creating Docker Network
docker network create --subnet=192.168.1.0/24 --gateway=192.168.1.1 ELK_LOG_NETWORK

# Setting Maximum number of memory map areas a process may have to 262144
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144

# Testing Docker Compose File
docker-compose -f .\elasticsearch-docker.yaml config

# Turning on Docker Compose YAML File elasticsearch
docker-compose -f .\elasticsearch-docker.yml up

# Testing Elasticsearch
curl -u elastic:abc@123 https://localhost:9200 -k

# Turning on Docker Compose YAML File kibana
docker-compose -f .\kibana-docker.yml up

# Getting Elasticsearch TTY
docker exec -it -u 0 elasticsearch_01 bash
su elasticsearch
```