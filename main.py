from httpx import get
from selectolax.parser import HTMLParser
from utils.extract import extract_full_body_html
from config.tools import get_config
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform, save_to_file
       
if __name__ == '__main__':
    config = get_config()
    html = extract_full_body_html(
        url=config.get('url'),
        waitfor=config.get('container').get('selector')
    )
    tree = HTMLParser(html)
    divs = tree.css(config.get('container').get('selector')) #selecting the bottom list
    game_data = []
    for d in divs:
        attrs = parse_raw_attributes(d, config.get('items'))
        attrs = format_and_transform(attrs)
        game_data.append(attrs)
        save_to_file('extract',game_data)