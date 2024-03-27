from httpx import get
from selectolax.parser import HTMLParser
from utils.extract import extract_full_body_html
from config.tools import get_config
from utils.parse import parse_raw_attributes
from utils.process import format_and_transform
       
if __name__ == '__main__':
    config = get_config()
    html = extract_full_body_html(
        url=config.get('url'),
        waitfor=config.get('container').get('selector')
    )
    tree = HTMLParser(html)
    divs = tree.css(config.get('container').get('selector')) #selecting the bottom list
    # print(len(divs))
    for d in divs:
        attrs = parse_raw_attributes(d, config.get('items'))
        attrs = format_and_transform(attrs)
        print(attrs)
        # title = d.css_first('div[class*=StoreSaleWidgetTitle]').text()
        # thumbnail = d.css_first('c').attrs.get('src')
        # tags = [a.text() for a in d.css('div[class*=_3OSJsO_BdhSFujrHvCGLqV] > a')[:5]] #tag wrapper class name (not dynamic)
        # release_date = d.css_first('div[class*=_3eOdkTDYdWyo_U5-JPeer1]').text() #release date class
        # review_score = d.css_first('div[class*=_2SbZztpb7hkhurwbFMdyhL] > div').text()
        # no_of_reviews = d.css_first('div[class*=_1Deyvnxud-VpRoj0-ak-WK]').text() #review counter class
        # sale_price = d.css_first('div[class*=Wh0L8EnwsPV_8VAu8TOYr]').text() #sale price container class
        # original_price = d.css_first('div[class*=_1EKGZBnKFWOr3RqVdnLMRN]').text()
        # attributes = {
        #     'title' : title,
        #     'tags' : tags,
        #     'review_score' : review_score,
        #     'release_date' : release_date,
        #     'no_of_reviews' : no_of_reviews,
        #     'thumbnail' : thumbnail,
        #     'original_price' : original_price,
        #     'sale_price' : sale_price
        # }
        # print(attributes)
        