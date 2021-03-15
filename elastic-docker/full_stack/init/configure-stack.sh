#!/bin/bash


# Wait for Elasticsearch to start up before doing anything.
until curl -s http://elasticsearch:9200/_cat/health -o /dev/null; do
    echo Waiting for Elasticsearch...
    sleep 1
done


# Wait for Kibana to start up before doing anything.
until curl -s http://kibana:5601/ -o /dev/null; do
    echo Waiting for Kibana...
    sleep 1
done

# Load any declared ingest pipelines.
PIPELINES=/usr/local/bin/pipelines/*.json
for f in $PIPELINES
do
     filename=$(basename $f)
     pipeline_id="${filename%.*}"
     echo "Loading $pipeline_id ingest chain..."
     curl -s  -H 'Content-Type: application/json' -XPUT http://elasticsearch:9200/_ingest/pipeline/$pipeline_id -d@$f
done

# Load any declared extra index templates
TEMPLATES=/usr/local/bin/templates/*.json
for f in $TEMPLATES
do
     filename=$(basename $f)
     template_id="${filename%.*}"
     echo "Loading $template_id template..."
     curl -s  -H 'Content-Type: application/json' -XPUT http://elasticsearch:9200/_template/$template_id -d@$f
     #We assume we want an index pattern in Kibana.
     curl -s -XPUT http://elasticsearch:9200/.kibana/index-pattern/$template_id-* \
     -d "{\"title\" : \"$template_id-*\",  \"timeFieldName\": \"@timestamp\"}"
done
