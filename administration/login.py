
import pdb


MENU_ITEMS = {}



class MenuItem:
    def __init__(self, command, display_name=None):
        self.command = command
        self.display_name = display_name
    
    def execute(self, *args, **kwargs):
        return self.command(*args, **kwargs)
    
    def __repr__(self):
        if self.display_name is not None:
            return self.display_name
        else:
            return self.command.__name__
    

class Menu:
    def __init__(self, menu_items_dict):
        if not isinstance(menu_items_dict, dict):
            print("Please provide menu options as a dict")
        else:
            self.menu_items_dict = menu_items_dict
    
    def display_options(self):
        for menu_item in self.menu_items_dict:
            print(menu_item)
    
    def choose_option(self, option, *args, **kwargs):
        if option in self.menu_items_dict:
            return self.menu_items_dict[option].execute(*args, **kwargs)


def register_menu_item(display_name=None):
    def decorator(function):
        MENU_ITEMS[display_name] = MenuItem(function, display_name=display_name)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@register_menu_item(display_name="Print Hello World")
def display_hello_world(*args, **kwargs):
    print("Hello World")

@register_menu_item(display_name="Multiply Two Numbers")
def multiply_two_numbers(*args, **kwargs):
    return args[0]*args[1]

if __name__ == "__main__":
    main_menu = Menu(MENU_ITEMS)
    main_menu.display_options()
    main_menu.choose_option("Print Hello World")
    result = main_menu.choose_option("Multiply Two Numbers", 5, 6)
    pdb.set_trace()