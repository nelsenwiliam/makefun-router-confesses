"""The Router Confesses -- make.fun bounty entry.

Writes one line, at most 200 characters, to /output/entry.txt: the excuse
a home Wi-Fi router gives for dropping the connection at the exact climax
of a movie. Pure Python standard library only.
"""

import os

# The router's confession: it already knows how the movie ends, and it
# dropped the connection rather than spoil it. Smug secret, fresh angle,
# no buffering / bandwidth / firmware cliche.
LINE = (
    "I already know who dies in the end, and unlike you, "
    "I have the self-control to keep it to myself."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def _resolve_output_path() -> str:
    """Return a writable output path.

    The grader runs the program in a sandbox where /output exists. When
    run by hand on a machine without a writable /output, fall back to a
    local output/entry.txt next to the working directory so the line can
    still be inspected.
    """
    try:
        probe = os.path.join(os.path.dirname(OUTPUT_PATH) or ".", ".write-test")
        with open(probe, "w", encoding="utf-8") as handle:
            handle.write("")
        os.remove(probe)
        return OUTPUT_PATH
    except OSError:
        return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    path = _resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
