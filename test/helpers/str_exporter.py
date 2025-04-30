from pathlib import Path


PYCACHE_DIR = 'test/__pycache__/'

path_default = Path(PYCACHE_DIR)


def tmp_export_str(filename: str, data: str):
    path = path_default / filename
    path.write_text(data, encoding='utf8')
