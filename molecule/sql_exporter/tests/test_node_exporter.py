import testinfra

host = testinfra.get_host("podman://rhel9")


def test_node_exporter_service(host):
    service = host.service("node_exporter")
    assert service.is_running
    assert service.is_enabled


def test_get_node_exporter_metrics_success(host):
    cmd = host.run(
        "curl -o /dev/null -s -w '%{http_code}' http://localhost:9100/metrics"
    )
    assert cmd.stdout == "200"
