from selectolax.parser import Node

def parse_raw_attributes(node : Node , selectors : list):
    parsed = {}
    
    for s in selectors:
        name = s.get("name")
        type_ = s.get("type")
        match = s.get("match")
        selector = s.get("selector")
        
        if match == "all":
            matched = node.css(selector)
            
            if type_ == "text":
                parsed[name] = [node.text() for node in matched]
            elif type_ == "node":
                parsed[name]=matched
                
        elif match == "first":
            matched = node.css_first(selector)
            
            if type_ == "text":
                parsed[name] = matched.text()
            elif type_ == "node":
                parsed[name] = matched
                
    return parsed