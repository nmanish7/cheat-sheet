## Elasticsearch

*Elasticsearch is a distributed, open-source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It is built on top of the Apache Lucene library and provides a scalable and efficient way to search and analyze large volumes of data quickly.*

### Components of Elasticsearch
-   Search engine
-   Indexing engine
-   Distributed computing and storage infrastructure
-   RESTful API
-   Plugins and integrations


### Index


### Document
A document is the basic unit of data that can be indexed and searched. It is a JSON object that contains key-value pairs of field names and their values.

**Example :** Here's an example of what a single employee document might look like in Elasticsearch:
```json
{
  "name": "John Doe",
  "age": 32,
  "job_title": "Software Engineer",
  "department": "Engineering",
  "salary": 100000
}

```

### Document Type
A document type is a logical category or grouping of documents with similar characteristics. In Elasticsearch version 6.x and earlier, a document type is a way to partition data within an index. However, in Elasticsearch version 7.x and later, multiple types are no longer supported within a single index.

### Node
A node is a single server that is part of a cluster. It stores data and participates in the cluster's indexing and search capabilities.

### Cluster
A cluster is a collection of one or more nodes that work together to store data and provide indexing and search capabilities across all the nodes.

### Shard
A shard is a single unit of data in Elasticsearch. It is a subset of the total data set that is stored on a single node. Elasticsearch can split an index into multiple shards, allowing for distributed processing and improved performance.

> *Think of Elasticsearch as a big library where all the books represent your data. The books are grouped by topic and stored on bookshelves called nodes. Now, imagine that you have a lot of books and not enough shelves to store them all on one node. That's where shards come in.*
> 
> *A shard is like a smaller bookshelf that holds a subset of the books on a node. Elasticsearch can split your index into multiple shards, allowing for distributed processing and improved performance. Each shard can be stored on a different node, so your data is spread out across the cluster.* 
> 
> *In summary, shards help Elasticsearch handle large amounts of data by breaking it up into smaller, more manageable pieces that can be distributed across multiple nodes.*

### Replica
A replica is a copy of a shard. Replicas provide redundancy and high availability, enabling Elasticsearch to continue to function even if some nodes fail.

## Index

- An index is the place where ElasticSearch stores data.
- In Elasticsearch, an index is a collection of documents that have somewhat similar characteristics. It can be thought of as a logical namespace that points to one or more physical shards, which actually store the data.
- **For example**, if you have a database of products, you might create an index called "products" in Elasticsearch. Within that index, you can store documents that represent each product. Each document might have fields such as the product name, price, description, and so on.

---
## Directory Structure of Elasticsearch

| Directory | Description                                                                      |
| --------- | -------------------------------------------------------------------------------- |
| bin       | The scripts needed for running ElasticSearch instances and for plugin management |
| config    | The directory where the configuration files are located                          |
| lib       | The libraries used by ElasticSearch                                              |

**After ElasticSearch starts, it will create the following directories (if they don't exist):**

| Directory | Description                                                                                |
| --------- | ------------------------------------------------------------------------------------------ |
| data      | Where all the data used by ElasticSearch is stored                                         |
| logs      | Files with information about event and errors that occur during the running of an instance |
| plugins   | The location for storing the installed plugins                                             |
| work      | Temporary files                                                                                           |

---

## Installing Elasticsearch from archive on Linux

```shell
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.7.1-linux-x86_64.tar.gz
tar -xzvf elasticsearch-8.7.1-linux-x86_64.tar.gz
cd elasticsearch-8.7.1
```


## Running Elasticsearch and Configuring first time

```shell
./bin/elasticsearch
```

> After running the above command first time it's configure elasticsearch to default and generate password (Enable the authentication and encrypt the cluster connections). You will get:
> - elastic user password
> - HTTP CA certificate SHA-256 fingerprint
> - Enrollment token for Kibana (valid for next 30 minutes)

### Reset Elastic Password

```Shell
# autogenerated
./bin/elasticsearch-reset-password -u elastic --url https://localhost:9200

# user interactive
./bin/elasticsearch-reset-password -u elastic --url https://localhost:9200 -i
```


### Regenerating Kibana Enrollment Token
```shell
./bin/elasticsearch-create-enrollment-token -s kibana
```


### Adding Elasticsearch Node to Cluster using Enrollment Token

To add another Nodes in cluster, first we have to change configuration in Master Node.
> **Uncomment** : \#transport.host: 0.0.0.0 *in **config/elasticsearch.yml** file.*
> 
```shell
sed -i 's/#transport.host: 0.0.0.0/transport.host: 0.0.0.0/' ./config/elasticsearch.yml  
```

> Restart Elasticsearch Service

```shell
# Generate token in Node1
./bin/elasticsearch-create-enrollment-token -s node

# Run below command in Node2
./bin/elasticsearch --enrollment-token <enrollment_token>
```

#### Increasing virtual memory areas configuration of the operating system where Elasticsearch is running

```shell
sysctl -w vm.max_map_count=262144
```

#### Elastic Node Help
```shell
# https://192.168.206.139:9200/_cat/nodes?help
curl -XGET "https://192.168.206.139:9200/_cat/nodes?help" -u elastic  -k
```

#### Elastic Getting Nodes Information with Header

```shell
# https://192.168.206.139:9200/_cat/nodes?v=true&h=ip,heap.percent,ram.percent,cpu,load_*,node.role,master,name,nodeId
curl -XGET "https://192.168.206.139:9200/_cat/nodes?v=true&h=ip,heap.percent,ram.percent,cpu,load_*,node.role,master,name,nodeId" -u elastic -k
```

#### Elastic Getting Nodes Information with Header with Full Id

```shell
# https://192.168.206.139:9200/_cat/nodes?v=true&h=ip,heap.percent,ram.percent,cpu,load_*,node.role,master,name,nodeId&full_id=true
curl -XGET "https://192.168.206.139:9200/_cat/nodes?v=true&h=ip,heap.percent,ram.percent,cpu,load_*,node.role,master,name,nodeId&full_id=true" -u elastic -k
```

#### Elastic Getting Detail Nodes Information
```shell
# https://192.168.206.139:9200/_nodes?nodeId&pretty
curl -XGET "https://192.168.206.139:9200/_nodes?nodeId&pretty" -u elastic -k
```


