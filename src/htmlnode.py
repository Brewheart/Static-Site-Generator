

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:  # Add this guard clause
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __repr__(self):
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props={self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value!")
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.children = []

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            props_string = self.props_to_html()
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None:
            raise ValueError("ParentNode must have a child")
        super().__init__(tag=tag, value=None, children=children, props=props)
        self.value = ""

    def to_html(self):
        child_string = ""
        if self.tag is None:
            raise ValueError("ParentNode must have a tag!")
        if self.children is None:
            raise ValueError("ParentNode must have children!")
        for child in self.children:
            html_child = child.to_html()
            child_string += html_child
        return f"<{self.tag}>{child_string}</{self.tag}>"

