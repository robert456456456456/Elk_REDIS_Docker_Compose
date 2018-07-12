FROM elasticsearch:2

MAINTAINER Ingresse

RUN plugin install elasticsearch/license/latest && \
    plugin install elasticsearch/shield/latest

ENV ES_SHIELD /usr/share/elasticsearch/bin/shield/
ENV PATH $ES_SHIELD:$PATH
ENV NODE_NAME ingresse-log
ENV CLUSTER_NAME ingresse-log

# For ELK works properly you need to:
# Add user for logstash and kibana
# CMD esusers useradd <username> -p <password> -r logstash,kibana4_server
