# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attribute in attrs:
            print("->",attribute[0],">",attribute[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attribute in attrs:
            print("->",attribute[0],">",attribute[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()


parser.feed(''.join([input().strip() for _ in range(int(input()))]))
