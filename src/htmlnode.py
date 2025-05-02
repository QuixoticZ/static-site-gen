class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        text_representation = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return text_representation
    
class LeafNode(HTMLNode):
    def __init__(self,tag,value,leaf_props=None):
        super().__init__(tag,value,props=leaf_props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNodes require a value")
        if not self.tag:
            return f"{self.value}"
        return f'<{self.tag}{self.props_to_html}>{self.value}</{self.tag}>'