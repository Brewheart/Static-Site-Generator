

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
        
        left_html_tag = ""
        right_html_tag = ""
        if self.tag == "p":
            left_html_tag = "<p>"
            right_html_tag = "</p>"

        return f"{left_html_tag}{self.value}{right_html_tag}
