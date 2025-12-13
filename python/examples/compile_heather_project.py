#!/usr/bin/env python3
"""Compile a minimal Heather project using the H-hat Python APIs.

This script mirrors the quick-start bash snippet from the Heather documentation
by:
- creating a project directory with ``src/main.hat`` containing ``main {}``,
- compiling that source into an IR graph via ``compile_project_ir``.

After installing the package (``pip install .`` from the repo's ``python``
folder), run:
```
python examples/compile_heather_project.py --project-root /path/to/demo
```
The "project root" can be anywhere on your machine; it does not need to live
inside the repository.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from hhat_lang.dialects.heather.compiler.core import compile_project_ir


def _write_minimal_source(project_root: Path) -> Path:
    """Ensure ``src/main.hat`` exists with the minimal Heather entry point."""

    source_path = project_root / "src" / "main.hat"
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_text("main {}\n", encoding="utf-8")
    return source_path


def compile_minimal_project(project_root: Path) -> None:
    """Create and compile a minimal Heather project to an IR graph.

    Args:
        project_root: Directory that will contain ``src/main.hat``.
    """

    source_path = _write_minimal_source(project_root)
    raw_code = source_path.read_text(encoding="utf-8")

    # ``compile_project_ir`` only relies on the ``project_root`` attribute of
    # ``HhatProjectSettings``. Avoid importing the full settings class here to
    # keep the example self-contained and to bypass any heavy dependencies that
    # might be missing in a minimal environment.
    settings = type("ProjectSettings", (), {"project_root": project_root})()

    ir_graph = compile_project_ir(project_settings=settings, raw_code=raw_code)

    print(f"Project root: {project_root}")
    print(f"Source file: {source_path}")
    print("Compiled IR modules:", ", ".join(ir_graph.modules.keys()))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a minimal Heather project and compile it to IR."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd() / "heather_demo",
        help=(
            "Directory to contain the Heather project (defaults to ./heather_demo). "
            "The folder will be created if it does not exist."
        ),
    )

    args = parser.parse_args()
    compile_minimal_project(args.project_root)


if __name__ == "__main__":
    main()
