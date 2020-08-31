import click
import logging
from ckan.lib.search.common import make_connection

log = logging.getLogger(__name__)


@click.group(name=u"multilang", short_help=u"Multilang module commands")
def multilang():
    pass


@multilang.command()
def initdb():
    from ckanext.multilang.model import setup as db_setup
    db_setup()


@multilang.command()
def initsearch():
    conn = make_connection()
    path = "schema"
    dynamic_field = b'{"add-dynamic-field": {"name": ' \
                    b'"package_multilang_localized_*",' \
                    b'"type": "text", "indexed": "true", ' \
                    b'"stored": "true", "multiValued": "false"}}'
    res = conn._send_request("post", path, dynamic_field)
    log.debug("Result of dynamic field addition {result}".format(
        result=res))

    copy_field = b'{"add-copy-field":{' \
                 b'"source": "package_multilang_localized_*",  ' \
                 b'"dest": "text"}}'

    res = conn._send_request("post", path, copy_field)
    log.debug("Result of copy field addition {result}".format(result=res))
    pass
