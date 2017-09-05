#!/usr/bin/env python

testinfra_hosts = [
    "docker://mrsum",
    "docker://mpsql",
]


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_http_connection(host):
    h = host.get_host('docker://mrsum')
    s = h.socket('tcp://0.0.0.0:8193')

    assert s.is_listening


def test_pgsql_connection(host):
    h = host.get_host('docker://mpsql')
    s = h.socket('tcp://0.0.0.0:5432')

    assert s.is_listening


def test_pgsql_create(host):
    h = host.get_host('docker://mpsql')
    assert h.run_test('sudo -u psql /opt/psql/bin/createdb testinfra')


def test_pgsql_drop(host):
    h = host.get_host('docker://mpsql')
    assert h.run_test('sudo -u psql /opt/psql/bin/dropdb testinfra')


# def test_rsyslog(host):
#    rsyslog = host.supervisor('rsyslogd')
#    print(rsyslog)
#    assert rsyslog.is_running


def test_psql(host):
    h = host.get_host("docker://mpsql")
    psql = h.supervisor('psql')
    assert psql.is_running


def test_gunicorn(host):
    h = host.get_host("docker://mrsum")
    gunicorn = h.supervisor('gunicorn')
    assert gunicorn.is_running
