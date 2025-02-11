import testinfra

host = testinfra.get_host("podman://")


def test_sql_exporter_service(host):
    service = host.service("sql_exporter")
    assert service.is_running
    assert service.is_enabled


def test_get_sql_exporter_metrics_success(host):
    cmd = host.run(
        "curl -o /dev/null -s -w '%{http_code}' http://localhost:9399/metrics"
    )
    assert cmd.stdout == "200"
