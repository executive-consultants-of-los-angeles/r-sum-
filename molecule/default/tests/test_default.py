#!/usr/bin/env python

testinfra_hosts = ["docker://rsum"]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_tcp_connection(host):
    s = host.socket('tcp://0.0.0.0:8193')

    assert s.is_listening
