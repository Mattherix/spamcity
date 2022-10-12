"""
spamcity.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Spamcity
"""
from requests import Request


def pretty_print_POST(req: Request):
    print(
        "{}\n{}\r\n{}\r\n\r\n{}".format(
            "-----------REQUEST-----------",
            req.method + " " + req.url,
            "\r\n".join("{}: {}".format(k, v) for k, v in req.headers.items()),
            req.body,
        )
    )
