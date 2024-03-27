import json
_config = {
    "url" : "https://store.steampowered.com/specials",
    "container":
        {
            "name" : "store_sale_divs",
            "selector" : "div[class*=y9MSdld4zZCuoQpRVDgMm]",
            "match" : "all",
            "type" : "node"
        },
    "items" : [
        {
            "name" : "title",
            "selector": "div[class*=StoreSaleWidgetTitle]",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "thumbnail",
            "selector": "img",
            "match": "first",
            "type": "node"
        },
        {
            "name" : "tags",
            "selector": "div[class*=_3OSJsO_BdhSFujrHvCGLqV] > a",
            "match": "all",
            "type": "text"
        },
        {
            "name" : "release_date",
            "selector": "div[class*=_3eOdkTDYdWyo_U5-JPeer1]",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "review_score",
            "selector": "div[class*=_2SbZztpb7hkhurwbFMdyhL] > div",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "no_of_reviews",
            "selector": "div[class*=_1Deyvnxud-VpRoj0-ak-WK]",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "price_currency",
            "selector": "div[class*=Wh0L8EnwsPV_8VAu8TOYr]",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "sale_price",
            "selector": "div[class*=Wh0L8EnwsPV_8VAu8TOYr]",
            "match": "first",
            "type": "text"
        },
        {
            "name" : "original_price",
            "selector": "div[class*=_1EKGZBnKFWOr3RqVdnLMRN]",
            "match": "first",
            "type": "text"
        }       
    ]
}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json","r") as f:
            return json.load(f)
    return _config

def generate_config():
    with open("config.json","w") as f:
        json.dump(_config,f,indent=4)
        
if __name__ == "__main__":
    generate_config()