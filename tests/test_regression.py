# Copyright (C) 2011-2012 James Rowe <jnrowe@gmail.com>
#
# This file is part of python-github2, and is made available under the 3-clause
# BSD license.  See LICENSE for the full details.

import httplib2

from nose.tools import eq_

from github2.client import Github

import utils


def test_issue_50():
    """Erroneous init of ``Http`` with proxy setup.

    See https://github.com/ask/python-github2/pull/50
    """
    utils.set_http_mock()

    client = Github(proxy_host="my.proxy.com", proxy_port=9000)
    setup_args = client.request._http.called_with
    eq_(type(setup_args['proxy_info']), httplib2.ProxyInfo)
    eq_(setup_args['proxy_info'].proxy_host, 'my.proxy.com')
    eq_(setup_args['proxy_info'].proxy_port, 9000)

    utils.unset_http_mock()
