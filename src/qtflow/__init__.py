from importlib import metadata


def main() -> None:
    version = metadata.version("qtflow")
    print(f"qtflow v{version}")
