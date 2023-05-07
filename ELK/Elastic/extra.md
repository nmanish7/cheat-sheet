curl -XPUT "https://localhost:9200/_nodes/6Z3F5DNsRf-zqQW0hppihA/shutdown?pretty" -H 'Content-Type: application/json' -d'                                                                                                                                                   {
  "type": "restart",
  "reason": "Demonstrating how the node shutdown API works",
  "allocation_delay": "1m"
}
' -u elastic -k


curl -XGET "https://localhost:9200/_nodes/6Z3F5DNsRf-zqQW0hppihA/shutdown" -u elastic --cacert ./http_ca.crt


curl -XPUT "https://localhost:9200/_nodes/6Z3F5DNsRf-zqQW0hppihA/shutdown?pretty" -H 'Content-Type: application/json' -d'                                                                                                                                                   {
  "type": "restart",
  "reason": "Demonstrating how the node shutdown API works"
}
' -u elastic -k
