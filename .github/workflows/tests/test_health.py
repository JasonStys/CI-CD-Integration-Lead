from codeflow import project_status


def test_project_status_has_expected_keys() -> None:
    result = project_status()

    assert "status" in result
    assert "project" in result
    assert "component" in result


def test_project_status_values() -> None:
    result = project_status()

    assert result["status"] == "ok"
    assert result["project"] == "codeflow"
    assert result["component"] == "ci"
