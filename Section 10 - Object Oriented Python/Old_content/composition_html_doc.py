# So can see difference between composition between inheritance use case and composition use case
# Tag as base class, Head, DocType and Body all inherit from this.
# Can be said that a Head, a body, a doctype IS a tag
# Whereas the htmlDoc relies on composition
# A htmlDoc HAS a doctype, a head, a body
class Tag:

    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file = None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        # this is the header /footer that needs to go on every html file. It varies by file but theres a limited number
        # to choose from. It's just a requirement to specifcy file type or something.
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' #doctype doesnt have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        # self.contents was originally nothing, ie ''
        # by doing the below, we've created a tag <title> and inserted this into the content
        # if we ever wanted to add further tags, you'd need an add tag method that would do self.content + tag
        if title:
            self._title = Tag("title", title)
            self.contents = str(self._title)
        # If wanted a title of a title, it would again need to go in the init
        # self._second_level_title = Tag('title2', self.contents)
        #self.contents = str(self._second_level_title)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '') # Body content built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)



class htmlDoc:

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == '__main__':
    my_page = htmlDoc("Demo HTML DOC")
    my_page.add_tag("h1","Main Heading")
    my_page.add_tag("h2", "sub-heading")
    my_page.add_tag("p", "This is a paragraph that will appear on the page")
    # the display function calls the print of each title, head & body
    with open('test.html', 'w', encoding='utf-8') as write_file:
        my_page.display(file=write_file)