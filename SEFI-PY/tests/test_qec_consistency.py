import importlib.util
from pathlib import Path


def test_qec_runner_imports_and_executes():
    root = Path(__file__).resolve().parents[1]
    runner_path = root / "SEFI-QEC" / "runner.py"

    spec = importlib.util.spec_from_file_location("sefi_qec_runner", runner_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)

    result = module.run_sefi_qec_demo()
    assert result is not None
