import argparse
import pathlib

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", action="version", version="PYfetch 1.0")
    parser.add_argument("--only", help="Show only specific sections (comma-separated, e.g. 'pc,user')", choices=['pc', 'user', 'desktop', 'other'], default="")
    parser.add_argument("--no-art", action="store_true", help="Don't show ASCII art")
    parser.add_argument("--custom-art", help="Path to custom ASCII art file", type=pathlib.Path)
    parser.add_argument("--logo", help="Show only specific logo", choices=['windows', 'macos', 'linux'], default="")
    return parser.parse_args()
