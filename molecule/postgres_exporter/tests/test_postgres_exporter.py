import testinfra

host = testinfra.get_host("podman://")


def test_postgres_exporter_service(host):
    service = host.service("postgres_exporter")
    assert service.is_running
    assert service.is_enabled


def test_get_postgres_exporter_metrics_success(host):
    cmd = host.run(
        "curl -o /dev/null -s -w '%{http_code}' http://localhost:9187/metrics"
    )
    assert cmd.stdout == "200"
