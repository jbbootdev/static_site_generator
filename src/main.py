# python


from textnode import TextType, TextNode


def main():
    textNode = TextNode("My text", TextType.BOLD, "http://google.com")
    print("HERE I AM")
    print(textNode)


if __name__ == "__main__":
    main()
