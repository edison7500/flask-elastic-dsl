from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

from flask import current_app
from flask import _app_ctx_stack as stack


class ElasticDSL(object):
    def __init__(self, app=None):
        assert app is not None
        self.init_app(app)

    def init_app(self, app):
        self.elastic_urls = list()

        _elastic_host = app.config.get("ELASTIC_HOST", "localhost:9200")
        _elastic_user = app.config.get("ELASTIC_USER", None)
        _elastic_passwd = app.config.get("ELASTIC_PASSWORD", None)

        if _elastic_user is not None:
            _elastic_url = "http://{user}:{passwd}@{host}".format(
                user=_elastic_user,
                passwd=_elastic_passwd,
                host=_elastic_host
            )
        else:
            _elastic_url = "http://{host}".format(
                host=_elastic_host
            )

        self.elastic_urls.append(_elastic_url)

    # @property
    # def es_client(self):
    #     return Elasticsearch(hosts=self.elastic_urls)

    def es_connection(self):
        return connections.create_connection(hosts=self.elastic_urls, timeout=15)
