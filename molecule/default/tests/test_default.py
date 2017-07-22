#!/usr/bin/env python

testinfra_hosts = ["rsum"]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
