
from base import *

class Opt:

    def __init__(self, text, callback):
        self.text = text
        self.callback = callback

    def __call__(self, *args, **kwargs):
        if callable(self.callback):
            self.callback(*arg, **kwargs)

class Choices:
    
    def __init__(self, entry, query, *opts):

        self.entry = entry
        self.query = query
        self.opts  = opts

    def prompt_callback(self):

        choice = None
        while True:
            
            print('')
            print(self.entry)

            for index, opt in enumerate(self.opts):
                print(f'{index} - {opt.text}')

            print()

            try:
                choice = input('choice: ')
                choice = int(choice)

            except ValueError:
                pass
            else:
                if choice >= 0 and choice < len(self.opts):
                    break

            print('invalid choice')

        return choice, self.opts[choice]

    def prompt(self, *args, **kwargs): 

        index, callback = prompt_callback()
        return callback(*args, **kwargs)

def create_inventory():

    global inventarios

    print('')

    itens_por_pagina = None
    paginas = None

    while True:
        try:
            text = input('itens/pagina: ')
        
            if text.isspace() or text == '':
                return

            itens_por_pagina = int(text)

        except ValueError:
            pass 
        else:
            if itens_por_pagina > 0:
                break

        print('valor invalido')

    while True:
        try:
            text = input('paginas: ')
        
            if text.isspace() or text == '':
                return

            paginas = int(text)

        except ValueError:
            pass 
        else:
            if paginas > 0:
                break

        print('valor invalido')

    inventarios.append(Inventario(paginas, itens_por_pagina))

def remove_inventory():

    global inventarios

    print('')
    for index, inv in enumerate(inventarios):
        print(f'{index} - {inv}')

    index = None

    print('')
    while True:
        try:
            text = input('indice: ')
        
            if text.isspace() or text == '':
                return

            index = int(text)

        except ValueError:
            pass 
        else:
            if index >= 0 and index < len(inventarios):
                break

        print('valor invalido')

    del inventarios[indice]

def select_inventory():

    global inventories
    global inventory_index

    print('')
    for index, inv in enumerate(inventarios):
        print(f'{index} - {inv}')

    index = None

    print('')
    while True:
        try:
            text = input('indice: ')
        
            if text.isspace() or text == '':
                return

            index = int(text)

        except ValueError:
            pass 
        else:
            if index >= 0 and index < len(inventarios):
                break

        print('valor invalido')

    inventory_index = index

def grab_item():
    pass
