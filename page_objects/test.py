import yaml


def load(yaml_path, **kwargs):
    with open(yaml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    filename = yaml_path.split('.')[0]
    adjacency = {}
    # {filename: {'pre': None, 'next': ['index_page']}}
    adjacency[filename] = data['adjacency']
    print(adjacency)


load('login_page.yaml')
load('index_page.yaml')
