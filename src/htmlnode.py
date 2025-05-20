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
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes require a value")
        if self.tag is None:
            return f"{self.value}"
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be present for Parent Nodes")
        if not self.children:
            raise ValueError("Parent nodes must have one or more Child Nodes")
        child_strings = []
        for child in self.children:
            child_strings.append(child.to_html())
        return f'<{self.tag}{super().props_to_html()}>{"".join(child_strings)}</{self.tag}>'
    

