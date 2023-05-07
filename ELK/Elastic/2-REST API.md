## Data Manipulation with REST API
*A RESTful API is an interface that allows two software applications to communicate with each other over the internet. It is designed to be simple and lightweight, and it uses HTTP methods such as GET, POST, PUT, and DELETE to manipulate resources on the server.*



### Storing Data in Elasticsearch

#### Creating Index

```shell
curl -XPUT "https://localhost:9200/blog?pretty" -u elastic --cacert ./config/certs/ht
tp_ca.crt
```

#### Getting Index Information

```shell
curl -XGET "https://localhost:9200/_cat/indices" -u elastic --cacert ./config/cacerts/http_ca.crt

# With Header
curl -XGET "https://localhost:9200/_cat/indices/blog?v" -u elastic --cacert ./config/cacerts/http_ca.crt
```

#### Creating Index with Mapping

Creating an index named `blog` with one shard and the specified mappings for the `id`, `title`, `content`, `priority`, and `tags` fields.

```shell
curl -XPUT "https://localhost:9200/blog5?pretty" -H 'Content-Type: application/json' -d '{
  "settings": { "index": { "number_of_shards": 1 } },
  "mappings": {
    "properties": {
      "id": { "type": "integer" },
      "title": { "type": "text" },
      "content": { "type": "text" },
      "priority": { "type": "integer" },
      "tags": { "type": "keyword" }
    }
  }
}' -u elastic --cacert ./config/certs/http_ca.crt
```

#### Getting Index Mapping

```shell
# https://192.168.206.139:9200/blog5/_mapping?pretty
curl -XGET "https://192.168.206.139:9200/blog5/_mapping?pretty" -u elastic --cacert ./config/certs/http_ca.crt
```

#### Creating a new Document with  given \_id

- For our example, let's imagine that we are building some kind of CMS (Content Management System) for our blog.
- Example:

```json
{ 
"id": "1", 
 "title": "New version of Elastic Search released!", 
 "content": "…", 
 "priority": 10, 
 "tags": ["announce", "elasticsearch", "release"] 
 }
```

```shell
curl -XPOST "https://localhost:9200/blog/_doc/1?pretty" -H 'Content-Type: application/json' -d '{
	"title": "New version of Elastic Search released!",
	"content": "...",
	"tags": ["announce", "elasticsearch", "release"]
}' -u elastic --cacert ./config/certs/http_ca.crt
```
#### Creating a new document with autogenerated \_id
```shell
curl -XPOST "https://localhost:9200/blog/_doc?pretty" -H 'Content-Type: application/json' -d '{
	"title": "New version of Elastic Search released!",
	"content": "...",
	"tags": ["announce", "elasticsearch", "release"]
}' -u elastic --cacert ./config/certs/http_ca.crt
```
---
### Retrieving documents

```shell
curl -XGET "https://localhost:9200/blog/_doc/1?pretty" -u elastic --cacert ./config/certs/http_ca.crt
```

```json
# output
{
  "_index" : "blog",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 0,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "title" : "New version of Elastic Search released!",
    "content" : "...",
    "tags" : [
      "announce",
      "elasticsearch",
      "release"
    ]
  }
}
```


#### What is _doc?
*  *In Elasticsearch, `_doc` is a type name for documents that are stored in an index. Prior to Elasticsearch version 7.0, it was possible to define custom types in an index, such as `blog`, `user`, `post`, etc. However, starting from Elasticsearch 7.0, types have been deprecated and only a single type `_doc` is supported. Therefore, when creating a new document in an index, you should use the `_doc` type.*
---
### Updating documents

Updating documents in an index is a more complicated task. Internally, ElasticSearch must fetch the document, take its data from the _source field, remove the old document, apply changes, and index it as a new document. ElasticSearch implements this through a script given as a parameter. This allows us to do more sophisticated document transformation than simple field changes. Let's see how it works in a simple case.

#### Updating without Script

```shell
curl -XPOST "https://localhost:9200/blog/_update/1?pretty" -H 'Content-Type: application/json' -d '{
  "doc": {
    "content": "Updated content"
  }
}' -u elastic -k
```

#### Updating With Script

```shell
curl -XPOST "https://localhost:9200/blog/_update/1?pretty" -H 'Content-Type: application/json' -u elastic -k -d '{
  "script": {
    "source": "ctx._source.content = params.new_content",
    "lang": "painless",
    "params": {
      "new_content": "This is the updated content"
    }
  }
}'

```
> In this example, the script updates the `content` field of the document with ID 1 in the `blog` index. The `source` field of the script contains the Painless script, which assigns the new value for the `content` field to the `ctx._source.content` variable. The `params` field of the script contains a parameter named `new_content`, which is used in the script to set the new value for the `content` field.
>>**Pianless**: *Painless is a simple, secure, and fast scripting language used by Elasticsearch, Kibana, and other related products in the Elastic Stack. It was specifically designed to be used in the context of Elasticsearch, allowing users to write custom scripts for tasks like updating documents, filtering search results, and more.*


#### upsert operation

- In Elasticsearch, an "upsert" operation is a combination of an update and a create operation.

- It is used to update a document if it exists or create a new document with the specified ID if it doesn't exist. The upsert operation eliminates the need to first check if a document exists before attempting to update it.

- For example, if you want to update a document with a specific ID, you can perform an upsert operation that specifies the ID and the new data. If the document with that ID already exists, it will be updated with the new data. If it doesn't exist, a new document will be created with the specified ID and the new data.

```shell
curl -XPOST "https://localhost:9200/blog/_update/5?pretty" -H "Content-Type: application/json" -u elastic -k -d '{
    "script": {
      "source": "ctx._source.counter += params.count",
      "lang": "painless",
      "params":{
        "count" : 4
      }
    },
    "upsert": {
      "counter": 1
    }
  }'
```

---
### Delete Documents

```shell
curl -XDELETE "https://localhost:9200/blog/_doc/1?pretty" -u elastic -k
```