from textnode import TextNode, TextType

def main():
    print('hello world')
    object = TextNode("This is a test text", TextType.BOLD, "https://test.com")
    print (object)


if __name__ == '__main__':
    main()

