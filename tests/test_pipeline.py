from demo_pipeline import parse_build_log


def test_log_parser_marks_failed_logs_as_failed():
    result = parse_build_log("FAILED tests/test_pipeline.py::test_log_parser")

    assert result.status == "passed"
