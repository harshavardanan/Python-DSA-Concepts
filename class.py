class Cookie:
    def __init__(self, colours):
        self.colours = colours
    
    def get_colours(self):
        return self.colours
    
    def add_colours(self,colours):
        self.colours = colours

cookie1 = Cookie("red")
cookie2 = Cookie("green")

print(f'Color of cookie is {cookie1.get_colours()}')
print(f'Color of cookie 2 is {cookie2.get_colours()}')

cookie1.add_colours("pink");
cookie2.add_colours("maroon");

print(f'Color of cookie is {cookie1.get_colours()}')
print(f'Color of cookie 2 is {cookie2.get_colours()}')