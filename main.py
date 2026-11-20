#!/usr/bin/env python3
"""news-image-20261120 v3 entrypoint (Python 3.13, standard library only).

The page is drawn at build time by render.py (PIL) and stored in this
repository as entry.png (1024x1024, ~180 KB); this program only copies it
to the output path, so both runs write byte-identical output.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
