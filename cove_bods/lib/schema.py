from urllib.parse import urljoin

from django.conf import settings

from cove.lib.common import SchemaJsonMixin


config = settings.COVE_CONFIG


class SchemaBODS(SchemaJsonMixin):
    schema_host = config['schema_host']
    release_schema_name = config['schema_item_name']
    release_pkg_schema_name = config['schema_name']
    release_schema_url = urljoin(schema_host, release_schema_name)
    release_pkg_schema_url = urljoin(schema_host, release_pkg_schema_name)

    def __init__():
        pass

    def process_codelists():
        pass

    def get_entity_schema_obj():
        pass

    def get_person_schema_obj():
        pass

    def get_ownership_schema_obj():
        pass

    def get_components_schema_obj():
        pass

    def get_package_schema_obj():
        pass
