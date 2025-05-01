class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = []
        if not self.props:
            return ""
        for key, value in self.props.items():
            props_string.append(f' {key}="{value}"')
        return "".join(props_string)

    def __repr__(self):
        text_representation = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return text_representation