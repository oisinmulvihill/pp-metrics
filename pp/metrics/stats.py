# -*- coding: utf-8 -*-
"""
This initialises the GraphitePeriodicPusher to send stats to the graphite
service.

"""
import logging

from greplin.scales.graphite import GraphitePeriodicPusher


_metrics = list()


def init(config={}):
    """Set up the GraphitePusher instance from a config dict.

    :param config: A dict in the form::

        config = {
            "metrics.enabled": "yes" | "no",
            "metrics.host": 'localhost',
            "metrics.port": 2003,
            "metrics.prefix": 'pp',
            # seconds:
            "metrics.period": 60,
            # no restrictions on the prefix all will be logged:
            "metrics.allow": '*',
        }

        If metrics.enabled = "no" then the GraphitePeriodicPusher
        won't be created and started.

    """
    log = logging.getLogger("{}.init".format(__name__))

    enabled = (config.get("metrics.enabled", "no")).lower().strip()

    if enabled != "yes":
        log.warn("Metrics are disabled (metrics.enabled = 'no').")
        return

    host = config.get("metrics.host", 'localhost')
    port = int(config.get("metrics.port", 2003))
    prefix = config.get("metrics.prefix", 'api.audience')
    period = float(config.get("metrics.period", 60))
    allow = config.get("metrics.allow", '*')

    d = dict(
        host=host,
        port=port,
        prefix=prefix,
        period=period,
        allow=allow
    )
    log.info((
        "GraphitePeriodicPusher configuration = "
        "host:{host} port:{port} prefix:'{prefix}' period:{period}"
    ).format(**d))

    g = GraphitePeriodicPusher(host, port, prefix, period)
    g.allow(allow)
    g.start()
    _metrics.append(g)
