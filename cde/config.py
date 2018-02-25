import os
import yaml


def get_config():
    if os.path.exists('.cde.yml'):
        with open('.cde.yml') as f:
            return yaml.load(f)

    return {}
