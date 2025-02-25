import copy

"""
# WebPageCreation
A website has number of pages that share the common layout and design,
such as header, footer, and navigation Menu> Instead of creating each
page from scratch, a prototype page can be created within the common
elements, and then copies of that page can be made as needed, each with
their own unique contents.

"""


class WebPage:
    def __init__(self):
        self.header = None
        # self.contents= ....
        # self.paragraph
        # self.people
        # header and footer are same content changes
        self.footer = None

    def set_page(self, ctype, content):
        setattr(self, ctype, content)

    def contents(self):
        # flexible web pages
        return "".join(
            [
                web
                for name, web in self.__dict__.items()
                if name not in ("header", "footer")
            ]
        )

    def page(self):
        return f"{self.header} {self.contents()} {self.footer}"


# prototype
class PageMaker:
    def __init__(self):
        self._page = {}

    def register_page(self, name, obj):
        self._page[name] = obj

    def unregister_page(self, name):
        del self._page[name]

    def create_page(self, name, **contents):
        webpage = copy.deepcopy(self._page.get(name))
        webpage.__dict__.update(contents)
        return webpage


if __name__ == "__main__":
    home = WebPage()
    home.set_page("header", "<div>home HEADER</div>")
    home.set_page("footer", "<div>home FOOTER</div>")
    home.set_page("Introduction", "<div>home Intro</div>")
    home.set_page("management", "<div>home Mgt</div>")
    home.set_page("product_list", "<div>product list</div>")
    print(home.__dict__)
    print("*" * 40)
    print(home.page())

    pm = PageMaker()

    pm.register_page("home", home)

    # clone the object to create another page

    about = pm.create_page(
        "home", header="<div>ABOUT Header </div>", footer="<div>ABOUT Footer </div>"
    )
    about.set_page("management", "<div> ABOUT US Management</div>")

    print("========ABOUT US =================")
    print(about.page())
