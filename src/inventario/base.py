
from abc import ABC, abstractmethod

class ItemBase(ABC):

    def __init__(self, _id, metadados):

        self._id = _id
        self._metadados = metadados

    def __repr__(self):
        return f'ItemBase(id={self._id})'

    @abstractmethod
    def copiar(self):
        pass

    @property
    def id(self):
        return self._id

class ItemTeste(ItemBase):

    def copiar(self):
        return ItemTeste(self._id, self._metadados)

    def __eq__(self, outro):
        return isinstance(outro, ItemTeste) and self._id == outro._id and self._metadados == outro._metadados

class PaginaInventario:

    def __init__(self, n_itens):
        self._itens = [None for _ in range(n_itens)]

    def __len__(self):
        return len(self._itens)

    def __iter__(self):
        return iter(self._itens)

    def __repr__(self):
        return f'PaginaInventario(n_itens={len(self._itens)})'

    def __getitem__(self, indice):
        
        if not isinstance(indice, int):
            raise TypeError(f'PaginaInventario.__getitem__: indice deve ser do tipo int, {type(indice)} recebido')       
        
        if indice < -len(self._itens) or indice >= len(self._itens):
            raise IndexError(f'PaginaInventario.__getitem__: indice invalido {indice}')
        
        return self._itens[indice]

    def __setitem__(self, indice, item):

        if not isinstance(indice, int):
            raise TypeError(f'PaginaInventario.__setitem__: indice deve ser do tipo int, {type(indice)} recebido')

        if indice < -len(self._itens) or indice >= len(self._itens):
            raise IndexError(f'PaginaInventario.__setitem__: indice invalido {indice}')
        
        if item is not None and not isinstance(item, ItemBase):
            raise TypeError(f'PaginaInventario.__setitem__: item deve ser do tipo Item ou None, {type(item)} recebido')

        self._itens[indice] = item

    def __delitem__(self, indice):

        if not isinstance(indice, int):
            raise TypeError(f'PaginaInventario.__delitem__: indice deve ser do tipo int, {type(indice)} recebido')

        if indice < -len(self._itens) or indice >= len(self._itens):
            raise IndexError(f'PaginaInventario.__delitem__: indice invalido {indice}')

        self._itens[indice] = None

    def __hasitem__(self, item):
        return item in self._itens

    @property
    def itens(self):
        return list(self._itens)

class ProxyPaginaInventario:
    
    def __init__(self, mestre, pagina):

        if not isinstance(mestre, Inventario):
            raise TypeError(f'ProxyPaginaInventario.__init__: mestre deve ser do tipo Inventario, {type(mestre)} recebido')

        if not isinstance(pagina, int):
            raise TypeError(f'ProxyPaginaInventario.__init__: pagina deve ser do tipo int, {type(pagina)} recebido')

        if pagina < -mestre.paginas or pagina >= mestre.paginas:
            raise ValueError(f'ProxyPaginaInventario.__init__: pagina {pagina} fora dos valores permitidos para o inventario {mestre}')

        self._mestre = mestre
        self._pagina = pagina

    def __len__(self):
        return len(self._mestre._paginas[self._pagina])

    def __repr__(self):
        return f'ProxyPaginaInventario(mestre={self._mestre}, pagina={self._pagina})'

    def __getitem__(self, indice):
        
        if not isinstance(indice, int):
            raise TypeError(f'ProxyPaginaInventario.__getitem__: indice deve ser do tipo int, {type(indice)} recebido')
        
        if indice < -self._mestre.itens_por_pagina or indice >= self._mestre.itens_por_pagina:
            raise IndexError(f'ProxyPaginaInventario.__getitem__: indice invalido {indice}')

        return self._mestre[self._pagina, indice]

    def __setitem__(self, indice, item):
        
        if not isinstance(indice, int):
            raise TypeError(f'ProxyPaginaInventario.__setitem__: indice deve ser do tipo int, {type(indice)} recebido')
        
        if indice < -self._mestre.itens_por_pagina or indice >= self._mestre.itens_por_pagina:
            raise IndexError(f'ProxyPaginaInventario.__setitem__: indice invalido {indice}')
        
        if item is not None and not isinstance(item, ItemBase):
            raise TypeError(f'ProxyPaginaInventario.__setitem__: item deve ser do tipo Item ou None, {type(item)} recebido')
        
        self._mestre[self._pagina, indice] = item

    def __delitem__(self, indice):
        
        if not isinstance(indice, int):
            raise TypeError(f'ProxyPaginaInventario.__delitem__: indice deve ser do tipo int, {type(indice)} recebido')
        
        if indice < -self._mestre.itens_por_pagina or indice >= self._mestre.itens_por_pagina:
            raise IndexError(f'ProxyPaginaInventario.__delitem__: indice invalido {indice}')

        del self._mestre[self._pagina, indice]
   
    def copiar(self):
        """
        cria um novo proxy ProxyPaginaInventario referenciando a mesma pagina-alvo
        """

        return ProxyPaginaInventario(self._mestre, self._pagina)

    def extrair(self):
        """
        cria uma nova PaginaInventario contendo copias dos itens da pagina ProxyPaginaInventario
        """

        container = []
        for item in self._mestre[self._pagina]:
            container.append(item.copiar() if item is not None else None)

        return PaginaInventario(container)

    def referencia(self):
        """
        retorna a pagina contendo os itens referenciada pelo proxy
        """

        return self._master[self._pagina]

    @property
    def mestre(self):
        return self._mestre

    @property
    def pagina(self):
        return self._pagina

class Inventario:

    def __init__(self, paginas, itens_por_pagina):
        
        if not isinstance(paginas, int):
            raise TypeError(f'Inventario.__init__: paginas deve ser do tipo int, {type(pagina)} recebido')

        if not isinstance(itens_por_pagina, int):
            raise TypeError(f'Inventario.__init__: itens_por_pagina deve ser do tipo int, {type(pagina)} recebido')

        if paginas <= 0:
            raise ValueError('Inventario.__init__: paginas deve ser um numero maior que zero')

        if itens_por_pagina <= 0:
            raise ValueError('Inventario.__init__: itens_por_pagina deve ser um numero maior que zero')
 
        self._paginas = [PaginaInventario(itens_por_pagina) for _ in range(paginas)]

    def __repr__(self):
        return f'Inventario(id={id(self)}, paginas={self.paginas}, itens/pagina={self.itens_por_pagina})'

    def __getitem__(self, indice):

        if isinstance(indice, int):

            if indice < -len(self._paginas) or indice >= len(self._paginas):
                raise IndexError(f'Inventario.__getitem__[int]: indice invalido {indice}')

            return ProxyPaginaInventario(self, indice)

        if isinstance(indice, tuple):
            
            if len(indice) != 2:
                raise IndexError(f'Inventario.__getitem__[tuple]: indice invalido {indice}')

            num_pagina, item = indice

            if num_pagina < -len(self._paginas) or num_pagina >= len(self._paginas):
                raise IndexError(f'Inventario.__getitem__[int, int]: indice invalido {indice}')

            pagina = self._paginas[num_pagina]
            if item < -len(pagina) or item >= len(pagina):
                raise IndexError(f'Inventario.__getitem__[int, int]: indice invalido {indice}')

            return pagina[item]

        raise IndexError(f'Inventario.__getitem__[]: indice invalido {indice}')

    def __setitem__(self, indice, valor):

        if isinstance(indice, int):

            raise IndexError(f'Inventario.__setitem__[int]: indice invalido {indice}')

            if not isinstance(valor, PaginaInventarioBase):
                raise ValueError(f'Inventario.__setitem__[int]: valor deve ser do tipo PaginaInventarioBase, {type(valor)} recebido')

            if indice < -len(self._paginas) or indice >= len(self._paginas):
                raise IndexError(f'Inventario.__setitem__[int]: indice invalido {indice}')

        elif isinstance(indice, tuple):
            
            if valor is not None and not isinstance(valor, ItemBase):
                raise ValueError(f'Inventario.__setitem__[int,int]: valor deve ser do tipo Item ou None, {type(valor)} recebido')
            
            if len(indice) != 2:
                raise IndexError(f'Inventario.__setitem__[tuple]: indice invalido {indice}')

            num_pagina, item = indice
            if num_pagina < -len(self._paginas) or num_pagina >= len(self._paginas):
                raise IndexError(f'Inventario.__setitem__[int, int]: indice invalido {indice}')

            pagina = self._paginas[num_pagina]
            if item < -len(pagina) or item >= len(pagina):
                raise IndexError(f'Inventario.__setitem__[int, int]: indice invalido {indice}')

            pagina[item] = valor

        else:
            raise IndexError(f'Inventario.__setitem__[]: indice invalido {indice}')

    def __delitem__(self, indice):

        if isinstance(indice, int):
            
            raise IndexError(f'Inventario.__delitem__[int]: impossivel remover pagina')

            if indice < -len(self._paginas) or indice >= len(self._paginas):
                raise IndexError(f'Inventario.__delitem__[int]: indice invalido {indice}')

        elif isinstance(indice, tuple):
            
            if len(indice) != 2:
                raise IndexError(f'Inventario.__delitem__[tuple]: indice invalido {indice}')

            num_pagina, item = indice
            if num_pagina < -len(self._paginas) or num_pagina >= len(self._paginas):
                raise IndexError(f'Inventario.__delitem__[int, int]: indice invalido {indice}')

            pagina = self._paginas[num_pagina]
            if item < -len(pagina) or item >= len(pagina):
                raise IndexError(f'Inventario.__delitem__[int, int]: indice invalido {indice}')

            pagina[item] = None

        else:
            raise IndexError(f'Inventario.__delitem__[]: indice invalido {indice}')

    def validar(self):

        itens = self.itens_por_pagina
        for indice, pagina in enumerate(self._paginas):
            if len(pagina) != itens:
                raise Exception(f'Inventario.validar: numero invalido de itens na pagina {indice}')

    @property
    def paginas(self):
        return len(self._paginas)

    @property
    def itens_por_pagina(self):
        return len(self._paginas[0]) if self._paginas else 0

    @property
    def itens(self):
        return self.paginas * self.itens_por_pagina
