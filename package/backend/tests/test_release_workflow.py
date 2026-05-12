from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def test_release_workflow_builds_and_uploads_windows_oneclick_package():
    workflow = (PROJECT_ROOT / ".github" / "workflows" / "build-exe.yml").read_text(encoding="utf-8")

    assert "tags:" in workflow
    assert "- 'v*'" in workflow
    assert "build-oneclick.ps1" in workflow
    assert "-PostgresZipUrl" in workflow
    assert "GankAIGC-Windows-OneClick.zip" in workflow
    assert "name: GankAIGC-Windows-OneClick" in workflow
    assert "gh release upload" in workflow


def test_oneclick_builder_validates_portable_postgres_tool_versions():
    script = (PROJECT_ROOT / "package" / "build-oneclick.ps1").read_text(encoding="utf-8")

    assert "Test-PortablePostgresVersions" in script
    assert "bin\\initdb.exe" in script
    assert "bin\\postgres.exe" in script
    assert "--version" in script
    assert "PostgreSQL 可执行文件版本不一致" in script
