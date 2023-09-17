from dataclasses import dataclass


@dataclass
class SortType:
    EXCHANGE: str = "exchange"
    FAST: str = "fast"
    HEAP: str = "heap"
    INSERTION: str = "insertion"
    MERGE: str = "merge"
    SELECT: str = "select"
    SHELL: str = "shell"
    TREE: str = "tree"
