from selectolax.parser import Node
from datetime import datetime
import re
import pandas as pd

def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError('Selectolax node was not provided')
    return node.attributes.get(attr)

def get_first_n(input_list: list, n: int = 5):
    return input_list[:n]

def reformat_date(date_raw: str , input_format: str='%b %d, %Y', output_format: str='%d-%m-%Y'):
    dt = datetime.strptime(date_raw, input_format) #converting string to datetime format
    return datetime.strftime(dt,output_format)

def regex(input_str : str, pattern: str, action : str= 'findall'):
    if action == 'findall':
        return re.findall(pattern,input_str)
    elif action == 'split':
        return re.split(pattern,input_str)
    else:
        raise ValueError('No action provided')
    


def format_and_transform(attrs: dict):
    transforms = {
        'thumbnail' : lambda n : get_attrs_from_node(n,'src'),
        'tags' : lambda input_list : get_first_n(input_list,5),
        'release_date' : lambda date: reformat_date(date,'%b %d, %Y', '%d-%m-%Y'),
        'no_of_reviews' : lambda raw : int(''.join(regex(raw,r'\d+', 'findall'))),
        'price_currency' : lambda raw : regex(raw, r'^.', 'findall'),
        'sale_price' : lambda raw : regex(raw,r'^.', 'split')[1],
        'original_price' : lambda raw : regex(raw,r'^.', 'split')[1]       
    }
    
    for k, v in transforms.items(): #to apply transform to the keys of transforms object (attrs)
        if k in attrs:
            attrs[k] = v(attrs[k])
    return attrs

def save_to_file(filename='extract.csv', data: list[dict] = None):
    if data is None:
        raise ValueError('Function expects data to be provided as a list of dictionaries')
    df = pd.DataFrame(data)
    filename=f'{datetime.now().strftime('%d-%m-%Y')}_{filename}.csv'
    df.to_csv(filename,index=False)