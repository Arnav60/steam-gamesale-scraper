from selectolax.parser import Node

def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError('Selectolax node was not provided')
    return node.attributes.get(attr)


def format_and_transform(attrs: dict):
    transforms = {
        'thumbnail' : lambda n : get_attrs_from_node(n,'src')
    }
    
    for k, v in transforms.items(): #to apply transform to the keys of transforms object (attrs)
        if k in attrs:
            attrs[k] = v(attrs[k])
    return attrs