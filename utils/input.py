from pathlib import Path

INPUT_PATH = Path("input")

def read_input(filename: Path):
    with open(INPUT_PATH / filename, "r") as f:
        return f.read()

def read_lines(filename: Path):
    with open(INPUT_PATH / filename, "r") as f:
        return [l.strip() for l in f.readlines()]
