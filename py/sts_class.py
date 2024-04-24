# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 13:55:06 2015

@author: ssheng
"""

try:
    from thread import get_ident as _get_ident    #thread 管理多个执行进程
except ImportError:
    from dummy_thread import get_ident as _get_ident

try:
    from _abcoll import KeysView, ValuesView, ItemsView
except ImportError:
    pass


class OrderedDict(dict):       #字典是没有顺序的，OrderdDict会记住dict增加的顺序
    """Dictionary that remembers insertion order"""
    # An inherited dict maps keys to values.
    # The inherited dict provides __getitem__, __len__, __contains__, and get.
    # The remaining methods are order-aware.
    # Big-O running times for all methods are the same as for regular dictionaries.

    # The internal self.__map dictionary maps keys to links in a doubly linked list.
    # The circular doubly linked list starts and ends with a sentinel element.
    # The sentinel element never gets deleted (this simplifies the algorithm).
    # Each link is stored as a list of length three:  [PREV, NEXT, KEY].

    def __init__(self, *args, **kwds):
        '''Initialize an ordered dictionary.  Signature is the same as for
        regular dictionaries, but keyword arguments are not recommended
        because their insertion order is arbitrary.

        '''
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = []                     # sentinel node
            root[:] = [root, root, None]
            self.__map = {}
        self.__update(*args, **kwds)

    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        'od.__setitem__(i, y) <==> od[i]=y'
        # Setting a new item creates a new link which goes at the end of the linked
        # list, and the inherited dictionary is updated with the new key/value pair.
        if key not in self:
            root = self.__root
            last = root[0]
            last[1] = root[0] = self.__map[key] = [last, root, key]
        dict_setitem(self, key, value)

    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        'od.__delitem__(y) <==> del od[y]'
        # Deleting an existing item uses self.__map to find the link which is
        # then removed by updating the links in the predecessor and successor nodes.
        dict_delitem(self, key)
        link_prev, link_next, key = self.__map.pop(key)
        link_prev[1] = link_next
        link_next[0] = link_prev

    def __iter__(self):
        'od.__iter__() <==> iter(od)'
        root = self.__root
        curr = root[1]
        while curr is not root:
            yield curr[2]
            curr = curr[1]

    def __reversed__(self):
        'od.__reversed__() <==> reversed(od)'
        root = self.__root
        curr = root[0]
        while curr is not root:
            yield curr[2]
            curr = curr[0]

    def clear(self):
        'od.clear() -> None.  Remove all items from od.'
        try:
            for node in self.__map.itervalues():
                del node[:]
            root = self.__root
            root[:] = [root, root, None]
            self.__map.clear()
        except AttributeError:
            pass
        dict.clear(self)

    def popitem(self, last=True):
        '''od.popitem() -> (k, v), return and remove a (key, value) pair.
        Pairs are returned in LIFO order if last is true or FIFO order if false.

        '''
        if not self:
            raise KeyError('dictionary is empty')
        root = self.__root
        if last:
            link = root[0]
            link_prev = link[0]
            link_prev[1] = root
            root[0] = link_prev
        else:
            link = root[1]
            link_next = link[1]
            root[1] = link_next
            link_next[0] = root
        key = link[2]
        del self.__map[key]
        value = dict.pop(self, key)
        return key, value

    # -- the following methods do not depend on the internal structure --

    def keys(self):
        'od.keys() -> list of keys in od'
        return list(self)

    def values(self):
        'od.values() -> list of values in od'
        return [self[key] for key in self]

    def items(self):
        'od.items() -> list of (key, value) pairs in od'
        return [(key, self[key]) for key in self]

    def iterkeys(self):
        'od.iterkeys() -> an iterator over the keys in od'
        return iter(self)

    def itervalues(self):
        'od.itervalues -> an iterator over the values in od'
        for k in self:
            yield self[k]

    def iteritems(self):
        'od.iteritems -> an iterator over the (key, value) items in od'
        for k in self:
            yield (k, self[k])

    def update(*args, **kwds):
        '''od.update(E, **F) -> None.  Update od from dict/iterable E and F.

        If E is a dict instance, does:           for k in E: od[k] = E[k]
        If E has a .keys() method, does:         for k in E.keys(): od[k] = E[k]
        Or if E is an iterable of items, does:   for k, v in E: od[k] = v
        In either case, this is followed by:     for k, v in F.items(): od[k] = v

        '''
        if len(args) > 2:
            raise TypeError('update() takes at most 2 positional '
                            'arguments (%d given)' % (len(args),))
        elif not args:
            raise TypeError('update() takes at least 1 argument (0 given)')
        self = args[0]
        # Make progressively weaker assumptions about "other"
        other = ()
        if len(args) == 2:
            other = args[1]
        if isinstance(other, dict):
            for key in other:
                self[key] = other[key]
        elif hasattr(other, 'keys'):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value
        for key, value in kwds.items():
            self[key] = value

    __update = update  # let subclasses override update without breaking __init__

    __marker = object()

    def pop(self, key, default=__marker):
        '''od.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.

        '''
        if key in self:
            result = self[key]
            del self[key]
            return result
        if default is self.__marker:
            raise KeyError(key)
        return default

    def setdefault(self, key, default=None):
        'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'
        if key in self:
            return self[key]
        self[key] = default
        return default

    def __repr__(self, _repr_running={}):
        'od.__repr__() <==> repr(od)'
        call_key = id(self), _get_ident()
        if call_key in _repr_running:
            return '...'
        _repr_running[call_key] = 1
        try:
            if not self:
                return '%s()' % (self.__class__.__name__,)
            return '%s(%r)' % (self.__class__.__name__, self.items())
        finally:
            del _repr_running[call_key]

    def __reduce__(self):
        'Return state information for pickling'
        items = [[k, self[k]] for k in self]
        inst_dict = vars(self).copy()
        for k in vars(OrderedDict()):
            inst_dict.pop(k, None)
        if inst_dict:
            return (self.__class__, (items,), inst_dict)
        return self.__class__, (items,)

    def copy(self):
        'od.copy() -> a shallow copy of od'
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S
        and values equal to v (which defaults to None).

        '''
        d = cls()
        for key in iterable:
            d[key] = value
        return d

    def __eq__(self, other):
        '''od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
        while comparison to a regular mapping is order-insensitive.

        '''
        if isinstance(other, OrderedDict):
            return len(self)==len(other) and self.items() == other.items()
        return dict.__eq__(self, other)

    def __ne__(self, other):
        return not self == other

    # -- the following methods are only used in Python 2.7 --

    def viewkeys(self):
        "od.viewkeys() -> a set-like object providing a view on od's keys"
        return KeysView(self)

    def viewvalues(self):
        "od.viewvalues() -> an object providing a view on od's values"
        return ValuesView(self)

    def viewitems(self):
        "od.viewitems() -> a set-like object providing a view on od's items"
        return ItemsView(self)
## end of http://code.activestate.com/recipes/576693/ }}}

#类定义，先把config类做好     
""" OrderedBunch is a subclass of OrderedDict with attribute-style access.
    
    >>> b = OrderedBunch()
    >>> b.hello = 'world'
    >>> b.hello
    'world'
    >>> b['hello'] += "!"
    >>> b.hello
    'world!'
    >>> b.foo = OrderedBunch(lol=True)
    >>> b.foo.lol
    True
    >>> b.foo is b['foo']
    True
    
    It is safe to import * from this module:
    
        __all__ = ('OrderedBunch', 'ordered_bunchify','ordered_unbunchify')
    
    ordered_un/bunchify provide dictionary conversion; Bunches can also be
    converted via OrderedBunch.to/fromOrderedDict().
    
    original source:
    https://pypi.python.org/pypi/bunch
"""


## Compatability Issues...
#try:
#    from collections import OrderedDict
#except ImportError:
#    from ordered_dict import OrderedDict


class OrderedBunch(OrderedDict):
    """ A dictionary that provides attribute-style access.
        
        >>> b = OrderedBunch()
        >>> b.hello = 'world'
        >>> b.hello
        'world'
        >>> b['hello'] += "!"
        >>> b.hello
        'world!'
        >>> b.foo = OrderedBunch(lol=True)
        >>> b.foo.lol
        True
        >>> b.foo is b['foo']
        True
        
        A OrderedBunch is a subclass of dict; it supports all the methods a dict does...
        
        >>> b.keys()
        ['foo', 'hello']
        
        Including update()...
        
        >>> b.update({ 'ponies': 'are pretty!' }, hello=42)
        >>> print repr(b)
        OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
        
        As well as iteration...
        
        >>> [ (k,b[k]) for k in b ]
        [('ponies', 'are pretty!'), ('foo', OrderedBunch(lol=True)), ('hello', 42)]
        
        And "splats".
        
        >>> "The {knights} who say {ni}!".format(**OrderedBunch(knights='lolcats', ni='can haz'))
        'The lolcats who say can haz!'
        
        See ordered_unbunchify/OrderedBunch.toOrderedDict, ordered_bunchify/OrderedBunch.fromOrderedDict for notes about conversion.
    """
    
    _initialized = False
    
    def __init__(self,*args,**kwarg):
        """ initializes the ordered dict
        """
        super(OrderedBunch,self).__init__(*args,**kwarg)
        self._initialized = True
    
    def __contains__(self, k):
        """ >>> b = OrderedBunch(ponies='are pretty!')
            >>> 'ponies' in b
            True
            >>> 'foo' in b
            False
            >>> b['foo'] = 42
            >>> 'foo' in b
            True
            >>> b.hello = 'hai'
            >>> 'hello' in b
            True
        """
        try:
            return hasattr(self, k) or dict.__contains__(self, k)
        except:
            return False
    
    # only called if k not found in normal places 
    def __getattr__(self, k):
        """ Gets key if it exists, otherwise throws AttributeError.
            
            nb. __getattr__ is only called if key is not found in normal places.
            
            >>> b = OrderedBunch(bar='baz', lol={})
            >>> b.foo
            Traceback (most recent call last):
                ...
            AttributeError: foo
            
            >>> b.bar
            'baz'
            >>> getattr(b, 'bar')
            'baz'
            >>> b['bar']
            'baz'
            
            >>> b.lol is b['lol']
            True
            >>> b.lol is getattr(b, 'lol')
            True
        """
        try:
            # Throws exception if not in prototype chain
            return object.__getattribute__(self, k)
        except AttributeError:
            try:
                return self[k]
            except KeyError:
                raise AttributeError(k)
    
    def __setattr__(self, k, v):
        """ Sets attribute k if it exists, otherwise sets key k. A KeyError
            raised by set-item (only likely if you subclass OrderedBunch) will 
            propagate as an AttributeError instead.
            
            >>> b = OrderedBunch(foo='bar', this_is='useful when subclassing')
            >>> b.values                            #doctest: +ELLIPSIS
            <built-in method values of OrderedBunch object at 0x...>
            >>> b.values = 'uh oh'
            >>> b.values
            'uh oh'
            >>> b['values']
            Traceback (most recent call last):
                ...
            KeyError: 'values'
        """
        
        if not self._initialized:
            # for OrderedDict initialization
            return object.__setattr__(self, k, v)
        
        try:
            # Throws exception if not in prototype chain
            object.__getattribute__(self, k)
        except AttributeError:
            try:
                self[k] = v
            except:
                raise AttributeError(k)
        else:
            object.__setattr__(self, k, v)
    
    def __delattr__(self, k):
        """ Deletes attribute k if it exists, otherwise deletes key k. A KeyError
            raised by deleting the key--such as when the key is missing--will
            propagate as an AttributeError instead.
            
            >>> b = OrderedBunch(lol=42)
            >>> del b.values
            Traceback (most recent call last):
                ...
            AttributeError: 'OrderedBunch' object attribute 'values' is read-only
            >>> del b.lol
            >>> b.lol
            Traceback (most recent call last):
                ...
            AttributeError: lol
        """
        try:
            # Throws exception if not in prototype chain
            object.__getattribute__(self, k)
        except AttributeError:
            try:
                del self[k]
            except KeyError:
                raise AttributeError(k)
        else:
            object.__delattr__(self, k)
    
    def toOrderedDict(self):
        """ Recursively converts a bunch back into a dictionary.
            
            >>> b = OrderedBunch(OrderedBunchunch(lol=True), hello=42, ponies='are pretty!')
            >>> b.toOrderedDict()
            {'ponies': 'are pretty!', 'foo': {'lol': True}, 'hello': 42}
            
            See ordered_unbunchify for more info.
        """
        return ordered_unbunchify(self)
    
    def __repr__(self):
        """ Invertible* string-form of a OrderedBunch.
            
            >>> b = OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
            >>> print repr(b)
            OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
            >>> eval(repr(b))
            OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
            
            (*) Invertible so long as collection contents are each repr-invertible.
        """
        keys = self.keys()
        args = ', '.join(['%s=%r' % (key, self[key]) for key in keys])
        return '%s(%s)' % (self.__class__.__name__, args)
    
    def __str__(self):
        """ String-form of a Bunch.
        """
        keys = self.keys()
        args = ', '.join(['%s=%r' % (key, self[key]) for key in keys])
        return '{%s}' % args    
    
    @staticmethod
    def fromOrderedDict(d):
        """ Recursively transforms a dictionary into a OrderedBunch via copy.
            
            >>> b = OrderedBunch.fromOrderedDict({'urmom': {'sez': {'what': 'what'}}})
            >>> b.urmom.sez.what
            'what'
            
            See ordered_bunchify for more info.
        """
        return ordered_bunchify(d)



# While we could convert abstract types like Mapping or Iterable, I think
# ordered_bunchify is more likely to "do what you mean" if it is conservative about
# casting (ex: isinstance(str,Iterable) == True ).
#
# Should you disagree, it is not difficult to duplicate this function with
# more aggressive coercion to suit your own purposes.

def ordered_bunchify(x):
    """ Recursively transforms a dictionary into a OrderedBunch via copy.
        
        >>> b = ordered_bunchify({'urmom': {'sez': {'what': 'what'}}})
        >>> b.urmom.sez.what
        'what'
        
        ordered_bunchify can handle intermediary dicts, lists and tuples (as well as 
        their subclasses), but ymmv on custom datatypes.
        
        >>> b = ordered_bunchify({ 'lol': ('cats', {'hah':'i win again'}), 
        ...         'hello': [{'french':'salut', 'german':'hallo'}] })
        >>> b.hello[0].french
        'salut'
        >>> b.lol[1].hah
        'i win again'
        
        nb. As dicts are not hashable, they cannot be nested in sets/frozensets.
    """
    if isinstance(x, dict):
        return OrderedBunch( (k, ordered_bunchify(v)) for k,v in x.iteritems() )
    elif isinstance(x, (list, tuple)):
        return type(x)( ordered_bunchify(v) for v in x )
    else:
        return x

def ordered_unbunchify(x):
    """ Recursively converts a OrderedBunch into a dictionary.
        
        >>> b = OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
        >>> ordered_unbunchify(b)
        {'ponies': 'are pretty!', 'foo': {'lol': True}, 'hello': 42}
        
        ordered_unbunchify will handle intermediary dicts, lists and tuples (as well as
        their subclasses), but ymmv on custom datatypes.
        
        >>> b = OrderedBunch(foo=['bar', OrderedBunch(lol=True)], hello=42, 
        ...         ponies=('are pretty!', OrderedBunch(lies='are trouble!')))
        >>> ordered_unbunchify(b) #doctest: +NORMALIZE_WHITESPACE
        {'ponies': ('are pretty!', {'lies': 'are trouble!'}), 
         'foo': ['bar', {'lol': True}], 'hello': 42}
        
        nb. As dicts are not hashable, they cannot be nested in sets/frozensets.
    """
    if isinstance(x, OrderedDict):
        return OrderedDict( (k, ordered_unbunchify(v)) for k,v in x.iteritems() )    
    elif isinstance(x, dict):
        return dict( (k, ordered_unbunchify(v)) for k,v in x.iteritems() )
    elif isinstance(x, (list, tuple)):
        return type(x)( ordered_unbunchify(v) for v in x )
    else:
        return x


### Serialization

try:
    try:
        import json
    except ImportError:
        import simplejson as json
    
    def toJSON(self, **options):
        """ Serializes this OrderedBunch to JSON. Accepts the same keyword options as `json.dumps()`.
            
            >>> b = OrderedBunch(foo=OrderedBunch(lol=True), hello=42, ponies='are pretty!')
            >>> json.dumps(b)
            '{"ponies": "are pretty!", "foo": {"lol": true}, "hello": 42}'
            >>> b.toJSON()
            '{"ponies": "are pretty!", "foo": {"lol": true}, "hello": 42}'
        """
        return json.dumps(self, **options)
    
    OrderedBunch.toJSON = toJSON
    
except ImportError:
    pass




try:
    # Attempt to register ourself with PyYAML as a representer
    import yaml
    from yaml.representer import Representer, SafeRepresenter
    
    def from_yaml(loader, node):
        """ PyYAML support for Bunches using the tag `!bunch` and `!bunch.OrderedBunch`.
            
            >>> import yaml
            >>> yaml.load('''
            ... Flow style: !bunch.OrderedBunch { Clark: Evans, Brian: Ingerson, Oren: Ben-Kiki }
            ... Block style: !bunch
            ...   Clark : Evans
            ...   Brian : Ingerson
            ...   Oren  : Ben-Kiki
            ... ''') #doctest: +NORMALIZE_WHITESPACE
            {'Flow style': OrderedBunch(Brian='Ingerson', Clark='Evans', Oren='Ben-Kiki'), 
             'Block style': OrderedBunch(Brian='Ingerson', Clark='Evans', Oren='Ben-Kiki')}
            
            This module registers itself automatically to cover both OrderedBunch and any 
            subclasses. Should you want to customize the representation of a subclass,
            simply register it with PyYAML yourself.
        """
        data = OrderedBunch()
        yield data
        value = loader.construct_mapping(node)
        data.update(value)
    
    
    def to_yaml_safe(dumper, data):
        """ Converts OrderedBunch to a normal mapping node, making it appear as a
            dict in the YAML output.
            
            >>> b = OrderedBunch(foo=['bar', OrderedBunch(lol=True)], hello=42)
            >>> import yaml
            >>> yaml.safe_dump(b, default_flow_style=True)
            '{foo: [bar, {lol: true}], hello: 42}\\n'
        """
        return dumper.represent_dict(data)
    
    def to_yaml(dumper, data):
        """ Converts OrderedBunch to a representation node.
            
            >>> b = OrderedBunch(foo=['bar', OrderedBunch(lol=True)], hello=42)
            >>> import yaml
            >>> yaml.dump(b, default_flow_style=True)
            '!bunch.OrderedBunch {foo: [bar, !bunch.OrderedBunch {lol: true}], hello: 42}\\n'
        """
        return dumper.represent_mapping(u'!orderedbunch.OrderedBunch', data)
    
    
    yaml.add_constructor(u'!orderedbunch', from_yaml)
    yaml.add_constructor(u'!orderedbunch.OrderedBunch', from_yaml)
    
    SafeRepresenter.add_representer(OrderedBunch, to_yaml_safe)
    SafeRepresenter.add_multi_representer(OrderedBunch, to_yaml_safe)
    
    Representer.add_representer(OrderedBunch, to_yaml)
    Representer.add_multi_representer(OrderedBunch, to_yaml)
    
    
    # Instance methods for YAML conversion
    def toYAML(self, **options):
        """ Serializes this OrderedBunch to YAML, using `yaml.safe_dump()` if 
            no `Dumper` is provided. See the PyYAML documentation for more info.
            
            >>> b = OrderedBunch(foo=['bar', OrderedBunch(lol=True)], hello=42)
            >>> import yaml
            >>> yaml.safe_dump(b, default_flow_style=True)
            '{foo: [bar, {lol: true}], hello: 42}\\n'
            >>> b.toYAML(default_flow_style=True)
            '{foo: [bar, {lol: true}], hello: 42}\\n'
            >>> yaml.dump(b, default_flow_style=True)
            '!bunch.OrderedBunch {foo: [bar, !bunch.OrderedBunch {lol: true}], hello: 42}\\n'
            >>> b.toYAML(Dumper=yaml.Dumper, default_flow_style=True)
            '!bunch.OrderedBunch {foo: [bar, !bunch.OrderedBunch {lol: true}], hello: 42}\\n'
        """
        opts = dict(indent=4, default_flow_style=False)
        opts.update(options)
        if 'Dumper' not in opts:
            return yaml.safe_dump(self, **opts)
        else:
            return yaml.dump(self, **opts)
    
    def fromYAML(*args, **kwargs):
        return ordered_bunchify( yaml.load(*args, **kwargs) )
    
    OrderedBunch.toYAML = OrderedBunch.__repr__ = toYAML
    OrderedBunch.fromYAML = staticmethod(fromYAML)
    
except ImportError:
    pass





#---------------------------------------------------------------
#  前面是标准实现
#  下面的内容和批处理有关系
# ----------------------------------------------------------------------

#---------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

#---------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import os,copy
#import numpy as np

#try:
#    from collections import OrderedDict
#except ImportError:
#    pass
    #from ..util.ordered_dict import OrderedDict

inf = 1.0e20


# ----------------------------------------------------------------------
#  Configuration ch20 file Class
# ----------------------------------------------------------------------

class Config20(OrderedBunch):
    """ config20 = io.Config20(filename="")
        
        Starts a config class, an extension of 
        ordered_bunch()
        
        use 1: initialize by reading config file
            config20 = io.Config20('filename')
        use 2: initialize from dictionary or bunch
            config20 = io.Config20(param_dict_in)
        use 3: initialize empty
            config20 = io.Config20()
        
        Parameters can be accessed by item or attribute
        ie: config20['MESH_FILENAME'] or config20.MESH_FILENAME
        
        Methods:
            read()       - read from a config file
            write()      - write to a config file (requires existing file)
            dump()       - dump a raw config file
            unpack_dvs() - unpack a design vector 
            diff()       - returns the difference from another config
            dist()       - computes the distance from another config
    """    

    _filename = 'bhcfd20.sts.template'
    
    def __init__(self,*args,**kwarg):
        
        # look for filename in inputs
        if args and isinstance(args[0],str):
            filename = args[0]
            args = args[1:]
        elif kwarg.has_key('filename'):
            filename = kwarg['filename']
            del kwarg['filename']
        else:
            filename = ''
        
        # initialize ordered bunch
        super(Config20,self).__init__(*args,**kwarg)
        
        # read config if it exists
        if filename:
            try:
                self.read(filename)
            except:
                raise IOError , 'Could not find config file: %s' % filename
        
        self._filename = filename
    
    def read(self,filename):
        """ reads from a config file """
        konfig = read_config20(filename)
        self.update(konfig)
        
    def write(self,filename=''):
        """ updates an existing config file """
        if not filename: filename = self._filename
        #assert os.path.exists(filename) , 'must write over an existing config file'
        write_config20(filename,self)
        
    def dump(self,filename=''):
        """ dumps all items in the config bunch, without comments """
        if not filename: filename = self._filename
        dump_config20(filename,self)
    
    def __getattr__(self,k):
        try:
            return super(Config20,self).__getattr__(k)
        except AttributeError:
            raise AttributeError , 'Config parameter not found'
        
    def __getitem__(self,k):
        try:
            return super(Config20,self).__getitem__(k)
        except KeyError:
            raise KeyError , 'Config parameter not found: %s' % k


    def __eq__(self,konfig):
        return super(Config20,self).__eq__(konfig)
    def __ne__(self,konfig):
        return super(Config20,self).__ne__(konfig)
    
    
    def local_files(self):
        """ removes path prefix from all *_FILENAME params
        """
        for key,value in self.iteritems():
            if key.split('_')[-1] == 'FILENAME':
                self[key] = os.path.basename(value)    
    
    def __repr__(self):
        #return '<Config> %s' % self._filename
        return self.__str__()
    
    def __str__(self):
        output = 'Config: %s' % self._filename
        for k,v in self.iteritems():
            output +=  '\n    %s= %s' % (k,v)
        return output
#: class Config




# -------------------------------------------------------------------
#  Get ch20 STS Configuration Parameters
# Config类的方法
# -------------------------------------------------------------------

def read_config20(filename):
    """ reads a config ch20 file """
      
    # initialize output dictionary
    data_dict = OrderedDict()
    
    input_file = open(filename)
    
    # process each line
    line_number=0
    while 1:
        # read the line
        line = input_file.readline()
        line_number=line_number+1
        if line_number>53:
            break
        # remove line returns
        line = line.strip('\r\n')
        # make sure it has useful data
        if ("=" in line) or (line[0] == '#') or ("---" in line):
            continue
        if (line_number==5):
            line = line.strip()
            data_dict['TaskName'] = line
            continue  
        #if (filter(str.isalpha,line)) :
        #    continue
        # split across equals sign
        line = line.split()
        #print line
        if (line_number==7):
            data_dict['Nondimension_L'] = line[0]
            data_dict['GridType'] = line[1]
            data_dict['SolverType'] = line[2]
            data_dict['Initial_way']= line[3]
            data_dict['SG1']=line[4]
            data_dict['SG2']=line[5]
            data_dict['SG3']=line[6]
            continue
        if (line_number==12):
            #print line                
            data_dict['Height'] = line[0]
            data_dict['Mach'] = line[1]
            data_dict['Alpha'] = line[2]
            data_dict['Beta'] = line[3]
            data_dict['Twall'] = line[4]
            data_dict['Gamma'] = line[5]
            data_dict['Prandtl_Lam'] = line[6]
            data_dict['Prandtl_Turb'] = line[7]            
            continue
        if (line_number==15):  
            data_dict['ATM_Pressure'] = line[0]
            data_dict['ATM_Density'] = line[1]
            data_dict['ATM_Temperature'] = line[2]
            continue
        if (line_number==20):     
            data_dict['TimeScheme'] = line[0]
            data_dict['InvDiscretMethod'] = line[1]
            data_dict['VisDiscretMethod'] = line[2]
            data_dict['SG4']=line[3]
            continue
        if (line_number==22):         
            data_dict['FluxScheme'] = line[0]
            data_dict['Limiter'] = line[1]
            data_dict['VisDirection'] = line[2]
            data_dict['UnphysicsCorrect'] = line[3]
            data_dict['TimeSizeMethod'] = line[4]
            data_dict['RelaxFactor'] = line[5]
            continue
        if (line_number==25):            
            data_dict['EntropyFix'] = line[0]
            data_dict['EntropyFixD'] = line[1]
            data_dict['EntropyFixO'] = line[2]
            data_dict['JSTCoe2'] = line[3]
            data_dict['JSTCoe4'] = line[4]
            continue
        if (line_number==30):
            data_dict['FlowModel'] = line[0]
            continue
        if (line_number==33):    
            data_dict['CompressibilityCorrect'] = line[0]
            data_dict['DES_Method'] = line[1]
            data_dict['CDES'] = line[2]
            data_dict['CDES_SST'] = line[3]
            continue
        if (line_number==38):            
            data_dict['IsRestart'] = line[0]
            data_dict['IterationNum'] = line[1]
            data_dict['CFL'] = line[2]
            data_dict['IOUT'] = line[3]
            data_dict['ErrorTol'] = line[4]
            data_dict['InitialStepNum'] = line[5]
            continue
        if (line_number==43):        
            data_dict['Ref_Area'] = line[0]
            data_dict['Ref_Length'] = line[1]
            data_dict['Ref_X'] = line[2]
            data_dict['Ref_Y'] = line[3]
            data_dict['Ref_Z'] = line[4]
            continue
        if (line_number==48):
            data_dict['Unsteady'] = line[0]
            continue
	           
        if (line_number==51):            
            data_dict['TimeSize'] = line[0]
            data_dict['MaxTimeSteps'] = line[1]
            data_dict['EndTime'] = line[2]
            data_dict['SubCFL'] = line[3]
            data_dict['SubStepNum'] = line[4]
            data_dict['SubErrorTOL'] = line[5]
            continue
   
        if (line_number==53):            
            data_dict['IPlot'] = line[0]
            data_dict['QuasiSteadySteps'] = line[1]
            data_dict['QuasiRestartSteps'] = line[2]
            continue
        #assert not data_dict.has_key(this_param) , ('Config file has multiple specifications of %s' % this_param )       
            
            # otherwise
            # string parameters
                        
        #: for case     
    #: for line
    input_file.close()

    return data_dict
    
#: def read_config()



# -------------------------------------------------------------------
#  Set ch20 STS Configuration Parameters
# -------------------------------------------------------------------

def write_config20(filename,param_dict):
    """ updates an existing config ch20 file """
    
    #temp_filename = "temp.sts"
   # shutil.copy(filename,temp_filename)
    output_file = open(filename,"w")

    # break pointers
    param_dict_in = copy.deepcopy(param_dict)
    
    sts_file=[]
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')    
    raw_line="#                              问题描述      		                 #"
    sts_file.append(raw_line+'\n')        
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')    
    raw_line="TaskName"
    sts_file.append(raw_line+'\n')    
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="Nondimension_L  GridType   SolverType    Initial_way  "  
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                            来流参数选择     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Height(m)  Mach  Alpha  Beta   Twall  Gamma  Prandtl_Lam  Prandtl_Turb  " 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="------------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="ATM_Pressure(Pa)  ATM_Density(kg/m3)  ATM_Temperature(K)  "
    sts_file.append(raw_line+'\n')
    raw_line=" "     
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                            数值方法选择    		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="TimeScheme  InvDiscretMethod   VisDiscretMethod "
    sts_file.append(raw_line+'\n')
    raw_line=" "
    sts_file.append(raw_line+'\n')
    raw_line="FluxScheme Limiter  VisDirection  UnphysicsCorrect  TimeSizeMethod  RelaxFactor"
    sts_file.append(raw_line+'\n')
    raw_line=""    
    sts_file.append(raw_line+'\n')
    raw_line="------------------------------------------------------------------------"    
    sts_file.append(raw_line+'\n')
    raw_line="EntropyFix   EntropyFixD  EntropyFixO     JSTCoe2  JSTCoe4"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              物理模型选择     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="FlowModel "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="-----------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="CompressibilityCorrect DES_Method  CDES CDES_SST"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              计算控制参数     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="IsRestart  IterationNum   CFL   IOUT  ErrorTol  InitialStepNum"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              计算参考量     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Ref_Area  Ref_Length  Ref_X  Ref_Y  Ref_Z"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                           非定常计算控制参数		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Unsteady   "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="-----------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="TimeSize	MaxTimeSteps EndTime  SubCFL    SubStepNum   SubErrorTOL "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="IPlot QuasiSteadySteps  QuasiRestartSteps"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    
    line_number=5
    sts_file[line_number-1]="{0:s}".format(param_dict_in['TaskName'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    
    line_number=7
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s}".format(
        param_dict_in['Nondimension_L'],
        param_dict_in['GridType'],
        param_dict_in['SolverType'],
        param_dict_in['Initial_way'],
        param_dict_in['SG1'],
        param_dict_in['SG2'],
        param_dict_in['SG3'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=12
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} {7:s}".format(                
        param_dict_in['Height'] ,
        param_dict_in['Mach'] ,
        param_dict_in['Alpha'] ,
        param_dict_in['Beta'] ,
        param_dict_in['Twall'] ,
        param_dict_in['Gamma'] ,
        param_dict_in['Prandtl_Lam'],
        param_dict_in['Prandtl_Turb'] )           
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=15 
    sts_file[line_number-1]="{0:s} {1:s} {2:s}".format(        
        param_dict_in['ATM_Pressure'],
        param_dict_in['ATM_Density'],
        param_dict_in['ATM_Temperature'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=20
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}".format(
        param_dict_in['TimeScheme'],
        param_dict_in['InvDiscretMethod'],
        param_dict_in['VisDiscretMethod'],
        param_dict_in['SG4'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=22 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(        
        param_dict_in['FluxScheme'],
        param_dict_in['Limiter'],
        param_dict_in['VisDirection'],
        param_dict_in['UnphysicsCorrect'] ,
        param_dict_in['TimeSizeMethod'],
        param_dict_in['RelaxFactor'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=25
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s}".format(            
        param_dict_in['EntropyFix'],
        param_dict_in['EntropyFixD'],
        param_dict_in['EntropyFixO'],
        param_dict_in['JSTCoe2'] ,
        param_dict_in['JSTCoe4'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=30
    sts_file[line_number-1]="{0:s} ".format(
        param_dict_in['FlowModel'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=33
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} ".format(
        param_dict_in['CompressibilityCorrect'],
        param_dict_in['DES_Method'],
        param_dict_in['CDES'],
        param_dict_in['CDES_SST'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=38
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s} {5:s}".format(            
        param_dict_in['IsRestart'],
        param_dict_in['IterationNum'],
        param_dict_in['CFL'],
        param_dict_in['IOUT'],
        param_dict_in['ErrorTol'],
        param_dict_in['InitialStepNum'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=43
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s}".format(        
        param_dict_in['Ref_Area'],
        param_dict_in['Ref_Length'],
        param_dict_in['Ref_X'],
        param_dict_in['Ref_Y'],
        param_dict_in['Ref_Z'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=48
    sts_file[line_number-1]="{0:s}".format(param_dict_in['Unsteady'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'           
    line_number=51
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s}  {5:s} ".format(            
        param_dict_in['TimeSize'],
        param_dict_in['MaxTimeSteps'],
        param_dict_in['EndTime'],
        param_dict_in['SubCFL'],
        param_dict_in['SubStepNum'] ,
        param_dict_in['SubErrorTOL'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=53
    sts_file[line_number-1]="{0:s} {1:s} {2:s}  ".format(            
        param_dict_in['IPlot'],
        param_dict_in['QuasiSteadySteps'],
        param_dict_in['QuasiRestartSteps'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'     
 
    # start writing parameter
    output_file.writelines(sts_file)
    
    output_file.close()
#    os.remove( temp_filename )
    
#: def write_config()


def dump_config20(filename,config):
    ''' dumps a raw config ch20 file with all options in config 
        and no comments
    '''
    
    # HACK - twl
    #if config.has_key('DV_VALUE_NEW'):
    #    config.DV_VALUE = config.DV_VALUE_NEW
        
    #config_file = open(filename,'w')
    # write dummy file
    #for key in config.keys():
    #    config_file.write( '%s= 0 \n' % key )
    #config_file.close()
    # dump data
    #write_config(filename,config)    

# -------------------------------------------------------------------
#  Get ch20 STS Configuration Parameters
# Config20类的方法结束
# -------------------------------------------------------------------


# ----------------------------------------------------------------------
#  Configuration ch19 file Class
# ----------------------------------------------------------------------

class Config19(OrderedBunch):
    """ config19 = io.Config19(filename="")
        
        Starts a config class, an extension of 
        ordered_bunch()
        
        use 1: initialize by reading config file
            config19 = io.Config19('filename')
        use 2: initialize from dictionary or bunch
            config19 = io.Config19(param_dict_in)
        use 3: initialize empty
            config19 = io.Config19()
        
        Parameters can be accessed by item or attribute
        ie: config19['MESH_FILENAME'] or config19.MESH_FILENAME
        
        Methods:
            read()       - read from a config file
            write()      - write to a config file (requires existing file)
            dump()       - dump a raw config file
            unpack_dvs() - unpack a design vector 
            diff()       - returns the difference from another config
            dist()       - computes the distance from another config
    """    

    _filename = 'bhcfd19.sts.template'
    
    def __init__(self,*args,**kwarg):
        
        # look for filename in inputs
        if args and isinstance(args[0],str):
            filename = args[0]
            args = args[1:]
        elif kwarg.has_key('filename'):
            filename = kwarg['filename']
            del kwarg['filename']
        else:
            filename = ''
        
        # initialize ordered bunch
        super(Config19,self).__init__(*args,**kwarg)
        
        # read config if it exists
        if filename:
            try:
                self.read(filename)
            except:
                raise IOError , 'Could not find config file: %s' % filename
        
        self._filename = filename
    
    def read(self,filename):
        """ reads from a config file """
        konfig = read_config19(filename)
        self.update(konfig)
        
    def write(self,filename=''):
        """ updates an existing config file """
        if not filename: filename = self._filename
        #assert os.path.exists(filename) , 'must write over an existing config file'
        write_config19(filename,self)
        
    def dump(self,filename=''):
        """ dumps all items in the config bunch, without comments """
        if not filename: filename = self._filename
        dump_config19(filename,self)
    
    def __getattr__(self,k):
        try:
            return super(Config19,self).__getattr__(k)
        except AttributeError:
            raise AttributeError , 'Config parameter not found'
        
    def __getitem__(self,k):
        try:
            return super(Config19,self).__getitem__(k)
        except KeyError:
            raise KeyError , 'Config parameter not found: %s' % k


    def __eq__(self,konfig):
        return super(Config19,self).__eq__(konfig)
    def __ne__(self,konfig):
        return super(Config19,self).__ne__(konfig)
    
    
    def local_files(self):
        """ removes path prefix from all *_FILENAME params
        """
        for key,value in self.iteritems():
            if key.split('_')[-1] == 'FILENAME':
                self[key] = os.path.basename(value)    
    
    def __repr__(self):
        #return '<Config> %s' % self._filename
        return self.__str__()
    
    def __str__(self):
        output = 'Config: %s' % self._filename
        for k,v in self.iteritems():
            output +=  '\n    %s= %s' % (k,v)
        return output
#: class Config




# -------------------------------------------------------------------
#  Get ch19 STS Configuration Parameters
# Config类的方法
# -------------------------------------------------------------------

def read_config19(filename):
    """ reads a config ch19 file """
      
    # initialize output dictionary
    data_dict = OrderedDict()
    
    input_file = open(filename)
    
    # process each line
    line_number=0
    while 1:
        # read the line
        line = input_file.readline()
        line_number=line_number+1
        if line_number>53:
            break
        # remove line returns
        line = line.strip('\r\n')
        # make sure it has useful data
        if ("=" in line) or (line[0] == '#') or ("---" in line):
            continue
        if (line_number==5):
            line = line.strip()
            data_dict['TaskName'] = line
            continue  
        #if (filter(str.isalpha,line)) :
        #    continue
        # split across equals sign
        line = line.split()
        #print line
        if (line_number==7):
            data_dict['Nondimension_L'] = line[0]
            data_dict['GridType'] = line[1]
            data_dict['NCPUs'] = line[2]
            continue
        if (line_number==12):
            #print line                
            data_dict['Height'] = line[0]
            data_dict['Mach'] = line[1]
            data_dict['Alpha'] = line[2]
            data_dict['Beta'] = line[3]
            data_dict['Twall'] = line[4]
            data_dict['Gamma'] = line[5]
            data_dict['Prandtl_Lam'] = line[6]
            data_dict['Prandtl_Turb'] = line[7]            
            continue
        if (line_number==15):  
            data_dict['ATM_Pressure'] = line[0]
            data_dict['ATM_Density'] = line[1]
            data_dict['ATM_Temperature'] = line[2]
            continue
        if (line_number==20):     
            data_dict['TimeScheme'] = line[0]
            data_dict['InvDiscretMethod'] = line[1]
            data_dict['VisDiscretMethod'] = line[2]
            continue
        if (line_number==22):         
            data_dict['FluxScheme'] = line[0]
            data_dict['Limiter'] = line[1]
            data_dict['VisDirection'] = line[2]
            data_dict['UnphysicsCorrect'] = line[3]
            data_dict['TimeSizeMethod'] = line[4]
            data_dict['RelaxFactor'] = line[5]
            continue
        if (line_number==25):            
            data_dict['EntropyFix'] = line[0]
            data_dict['EntropyFixD'] = line[1]
            data_dict['EntropyFixO'] = line[2]
            data_dict['JSTCoe2'] = line[3]
            data_dict['JSTCoe4'] = line[4]
            continue
        if (line_number==30):
            data_dict['FlowModel'] = line[0]
            continue
        if (line_number==33):    
            data_dict['CompressibilityCorrect'] = line[0]
            data_dict['DES_Method'] = line[1]
            data_dict['CDES'] = line[2]
            data_dict['CDES_SST'] = line[3]
            continue
        if (line_number==38):            
            data_dict['IsRestart'] = line[0]
            data_dict['IterationNum'] = line[1]
            data_dict['CFL'] = line[2]
            data_dict['IOUT'] = line[3]
            data_dict['ErrorTol'] = line[4]
            data_dict['InitialStepNum'] = line[5]
            continue
        if (line_number==43):        
            data_dict['Ref_Area'] = line[0]
            data_dict['Ref_Length'] = line[1]
            data_dict['Ref_X'] = line[2]
            data_dict['Ref_Y'] = line[3]
            data_dict['Ref_Z'] = line[4]
            continue
        if (line_number==48):
            data_dict['Unsteady'] = line[0]
            continue
	           
        if (line_number==51):            
            data_dict['TimeSize'] = line[0]
            data_dict['MaxTimeSteps'] = line[1]
            data_dict['EndTime'] = line[2]
            data_dict['SubCFL'] = line[3]
            data_dict['SubStepNum'] = line[4]
            data_dict['SubErrorTOL'] = line[5]
            continue
   
        if (line_number==53):            
            data_dict['IPlot'] = line[0]
            data_dict['QuasiSteadySteps'] = line[1]
            data_dict['QuasiRestartSteps'] = line[2]
            continue
        #assert not data_dict.has_key(this_param) , ('Config file has multiple specifications of %s' % this_param )       
            
            # otherwise
            # string parameters
                        
        #: for case     
    #: for line
    input_file.close()

    return data_dict
    
#: def read_config19()



# -------------------------------------------------------------------
#  Set ch19 STS Configuration Parameters
# -------------------------------------------------------------------

def write_config19(filename,param_dict):
    """ updates an existing config ch19 file """
    
    #temp_filename = "temp.sts"
   # shutil.copy(filename,temp_filename)
    output_file = open(filename,"w")

    # break pointers
    param_dict_in = copy.deepcopy(param_dict)
    
    sts_file=[]
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')    
    raw_line="#                              问题描述      		                 #"
    sts_file.append(raw_line+'\n')        
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')    
    raw_line="TaskName"
    sts_file.append(raw_line+'\n')    
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="Nondimension_L  GridType   NCPUs"  
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                            来流参数选择     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Height(m)  Mach  Alpha  Beta   Twall  Gamma  Prandtl_Lam  Prandtl_Turb  " 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="------------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="ATM_Pressure(Pa)  ATM_Density(kg/m3)  ATM_Temperature(K)  "
    sts_file.append(raw_line+'\n')
    raw_line=" "     
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                            数值方法选择    		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="TimeScheme  InvDiscretMethod   VisDiscretMethod"
    sts_file.append(raw_line+'\n')
    raw_line=" "
    sts_file.append(raw_line+'\n')
    raw_line="FluxScheme Limiter  VisDirection  UnphysicsCorrect  TimeSizeMethod  RelaxFactor"
    sts_file.append(raw_line+'\n')
    raw_line=""    
    sts_file.append(raw_line+'\n')
    raw_line="------------------------------------------------------------------------"    
    sts_file.append(raw_line+'\n')
    raw_line="EntropyFix   EntropyFixD  EntropyFixO     JSTCoe2  JSTCoe4"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              物理模型选择     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="FlowModel "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="-----------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="CompressibilityCorrect DES_Method  CDES CDES_SST"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              计算控制参数     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="IsRestart  IterationNum   CFL   IOUT  ErrorTol  InitialStepNum"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                              计算参考量     		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Ref_Area  Ref_Length  Ref_X  Ref_Y  Ref_Z"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="#                           非定常计算控制参数		                 #"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="Unsteady   "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="-----------------------------------------------------------------------"
    sts_file.append(raw_line+'\n')
    raw_line="TimeSize	MaxTimeSteps EndTime  SubCFL    SubStepNum   SubErrorTOL "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="IPlot QuasiSteadySteps  QuasiRestartSteps"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    
    line_number=5
    sts_file[line_number-1]="{0:s}".format(param_dict_in['TaskName'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    
    line_number=7
    sts_file[line_number-1]="{0:s} {1:s} {2:s} ".format(
        param_dict_in['Nondimension_L'],
        param_dict_in['GridType'],
        param_dict_in['NCPUs'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=12
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} {7:s}".format(                
        param_dict_in['Height'] ,
        param_dict_in['Mach'] ,
        param_dict_in['Alpha'] ,
        param_dict_in['Beta'] ,
        param_dict_in['Twall'] ,
        param_dict_in['Gamma'] ,
        param_dict_in['Prandtl_Lam'],
        param_dict_in['Prandtl_Turb'] )           
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=15 
    sts_file[line_number-1]="{0:s} {1:s} {2:s}".format(        
        param_dict_in['ATM_Pressure'],
        param_dict_in['ATM_Density'],
        param_dict_in['ATM_Temperature'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=20
    sts_file[line_number-1]="{0:s} {1:s} {2:s}".format(
        param_dict_in['TimeScheme'],
        param_dict_in['InvDiscretMethod'],
        param_dict_in['VisDiscretMethod'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=22 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(        
        param_dict_in['FluxScheme'],
        param_dict_in['Limiter'],
        param_dict_in['VisDirection'],
        param_dict_in['UnphysicsCorrect'] ,
        param_dict_in['TimeSizeMethod'],
        param_dict_in['RelaxFactor'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=25
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s}".format(            
        param_dict_in['EntropyFix'],
        param_dict_in['EntropyFixD'],
        param_dict_in['EntropyFixO'],
        param_dict_in['JSTCoe2'] ,
        param_dict_in['JSTCoe4'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=30
    sts_file[line_number-1]="{0:s} ".format(
        param_dict_in['FlowModel'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=33
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} ".format(
        param_dict_in['CompressibilityCorrect'],
        param_dict_in['DES_Method'],
        param_dict_in['CDES'],
        param_dict_in['CDES_SST'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=38
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s} {5:s}".format(            
        param_dict_in['IsRestart'],
        param_dict_in['IterationNum'],
        param_dict_in['CFL'],
        param_dict_in['IOUT'],
        param_dict_in['ErrorTol'],
        param_dict_in['InitialStepNum'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=43
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s}".format(        
        param_dict_in['Ref_Area'],
        param_dict_in['Ref_Length'],
        param_dict_in['Ref_X'],
        param_dict_in['Ref_Y'],
        param_dict_in['Ref_Z'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=48
    sts_file[line_number-1]="{0:s}".format(param_dict_in['Unsteady'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'           
    line_number=51
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s}  {5:s} ".format(            
        param_dict_in['TimeSize'],
        param_dict_in['MaxTimeSteps'],
        param_dict_in['EndTime'],
        param_dict_in['SubCFL'],
        param_dict_in['SubStepNum'] ,
        param_dict_in['SubErrorTOL'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=53
    sts_file[line_number-1]="{0:s} {1:s} {2:s}  ".format(            
        param_dict_in['IPlot'],
        param_dict_in['QuasiSteadySteps'],
        param_dict_in['QuasiRestartSteps'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'     
 
    # start writing parameter
    output_file.writelines(sts_file)
    
    output_file.close()
#    os.remove( temp_filename )
    
#: def write_config()


def dump_config19(filename,config):
    ''' dumps a raw config file with all options in config 
        and no comments
    '''
    
    # HACK - twl
    #if config.has_key('DV_VALUE_NEW'):
    #    config.DV_VALUE = config.DV_VALUE_NEW
        
    #config_file = open(filename,'w')
    # write dummy file
    #for key in config.keys():
    #    config_file.write( '%s= 0 \n' % key )
    #config_file.close()
    # dump data
    #write_config(filename,config)    

# -------------------------------------------------------------------
#  Get ch19 STS Configuration Parameters
# Config类的方法结束
# -------------------------------------------------------------------






# ----------------------------------------------------------------------
#  Configuration ch18 file Class
# ----------------------------------------------------------------------

class Config18(OrderedBunch):
    """ config18 = io.Config18(filename="")
        
        Starts a config class, an extension of 
        ordered_bunch()
        
        use 1: initialize by reading config file
            config18 = io.Config18('filename')
        use 2: initialize from dictionary or bunch
            config18 = io.Config18(param_dict_in)
        use 3: initialize empty
            config18 = io.Config18()
        
        Parameters can be accessed by item or attribute
        ie: config18['MESH_FILENAME'] or config18.MESH_FILENAME
        
        Methods:
            read()       - read from a config file
            write()      - write to a config file (requires existing file)
            dump()       - dump a raw config file
            unpack_dvs() - unpack a design vector 
            diff()       - returns the difference from another config
            dist()       - computes the distance from another config
    """    

    _filename = 'bhcfd18.sts.template'
    
    def __init__(self,*args,**kwarg):
        
        # look for filename in inputs
        if args and isinstance(args[0],str):
            filename = args[0]
            args = args[1:]
        elif kwarg.has_key('filename'):
            filename = kwarg['filename']
            del kwarg['filename']
        else:
            filename = ''
        
        # initialize ordered bunch
        super(Config18,self).__init__(*args,**kwarg)
        
        # read config if it exists
        if filename:
            try:
                self.read(filename)
            except:
                raise IOError , 'Could not find config file: %s' % filename
        
        self._filename = filename
    
    def read(self,filename):
        """ reads from a config file """
        konfig = read_config18(filename)
        self.update(konfig)
        
    def write(self,filename=''):
        """ updates an existing config file """
        if not filename: filename = self._filename
        #assert os.path.exists(filename) , 'must write over an existing config file'
        write_config18(filename,self)
        
    def dump(self,filename=''):
        """ dumps all items in the config bunch, without comments """
        if not filename: filename = self._filename
        dump_config18(filename,self)
    
    def __getattr__(self,k):
        try:
            return super(Config18,self).__getattr__(k)
        except AttributeError:
            raise AttributeError , 'Config parameter not found'
        
    def __getitem__(self,k):
        try:
            return super(Config18,self).__getitem__(k)
        except KeyError:
            raise KeyError , 'Config parameter not found: %s' % k


    def __eq__(self,konfig):
        return super(Config18,self).__eq__(konfig)
    def __ne__(self,konfig):
        return super(Config18,self).__ne__(konfig)
    
    
    def local_files(self):
        """ removes path prefix from all *_FILENAME params
        """
        for key,value in self.iteritems():
            if key.split('_')[-1] == 'FILENAME':
                self[key] = os.path.basename(value)    
    
    def __repr__(self):
        #return '<Config> %s' % self._filename
        return self.__str__()
    
    def __str__(self):
        output = 'Config: %s' % self._filename
        for k,v in self.iteritems():
            output +=  '\n    %s= %s' % (k,v)
        return output
#: class Config




# -------------------------------------------------------------------
#  Get ch18 STS Configuration Parameters
# Config类的方法
# -------------------------------------------------------------------

def read_config18(filename):
    """ reads a config ch18 file """
      
    # initialize output dictionary
    data_dict = OrderedDict()
    
    input_file = open(filename)
    
    # process each line
    line_number=0
    while 1:
        # read the line
        line = input_file.readline()
        line_number=line_number+1
        if line_number>30:
            break
        # remove line returns
        line = line.strip('\r\n')
        # make sure it has useful data
        if ("=" in line) or (line[0] == '#') or ("---" in line):
            continue
        if (line_number==1):
            line = line.strip()
            data_dict['TaskName'] = line
            continue  
        #if (filter(str.isalpha,line)) :
        #    continue
        # split across equals sign
        line = line.split()
        #print line
        if (line_number==3):
            data_dict['NONDIMENSION_L'] = line[0]
            data_dict['KIND_GRID'] = line[1]
            data_dict['NTHREAD'] = line[2]
            continue
        if (line_number==5):
            data_dict['NVISC'] = line[0]
            data_dict['IMP'] = line[1]
            data_dict['ISPA'] = line[2]
            data_dict['NLIM'] = line[3]
            data_dict['NVIDI'] = line[4]        
            continue
        if (line_number==7):            
            data_dict['IRSTRT'] = line[0]
            data_dict['MAXSTP'] = line[1]
            data_dict['CFL'] = line[2]
            continue
        if (line_number==9):
            #print line                
            data_dict['HEIGHT'] = line[0]
            data_dict['FSMACH'] = line[1]
            data_dict['ALPHA'] = line[2]
            data_dict['BETA'] = line[3]
            data_dict['TWALL'] = line[4]        
            continue
        if (line_number==11):        
            data_dict['A_REF'] = line[0]
            data_dict['L_REF'] = line[1]
            data_dict['X_REF'] = line[2]
            data_dict['Y_REF'] = line[3]
            data_dict['Z_REF'] = line[4]
            continue
        if (line_number==14):  
            data_dict['ATM_P'] = line[0]
            data_dict['ATM_R'] = line[1]
            data_dict['ATM_T'] = line[2]
            data_dict['GAMMA'] = line[3]
            data_dict['PRL'] = line[4]
            data_dict['PRT'] = line[5]
            continue
        if (line_number==16):  
            data_dict['NFIX'] = line[0]
            data_dict['FIXD'] = line[1]
            data_dict['FIXO'] = line[2]
            data_dict['DIIM'] = line[3]
            data_dict['VIS2'] = line[4]
            data_dict['VIS4'] = line[5]
            continue
        if (line_number==18):  
            data_dict['NT_SEL'] = line[0]
            data_dict['MODI']   = line[1]
            data_dict['NTIME']  = line[2]
            data_dict['IOUT']   = line[3]
            data_dict['ERRTOL'] = line[4]
            data_dict['INIT_IT']= line[5]
            continue
        if (line_number==20):     
            data_dict['MUSC'] = line[0]
            data_dict['NMUSC'] = line[1]
            continue
        if (line_number==22):  
            data_dict['TSIZE'] = line[0]
            data_dict['TMAXSTP'] = line[1]
            data_dict['TEND'] = line[2]
            data_dict['SUBCFL'] = line[3]
            data_dict['N_SUBSTEP'] = line[4]
            data_dict['SUB_ERRTOL'] = line[5]
            data_dict['IPLT'] = line[6]
            data_dict['QST'] = line[7]
            data_dict['QRSTP'] = line[8]
            continue
        if (line_number==24):         
            data_dict['CFL_YNOR'] = line[0]
            data_dict['NCYCLE'] = line[1]
            data_dict['IDES'] = line[2]
            data_dict['I2D'] = line[3]
            continue
        if (line_number==26):            
            data_dict['NCOMP'] = line[0]
            data_dict['CDES'] = line[1]
            data_dict['CS'] = line[2]
            continue
        if (line_number==28):    
            data_dict['IBLK'] = line[0]
            data_dict['ILAMLO'] = line[1]
            data_dict['ILAMHI'] = line[2]
            data_dict['JLAMLO'] = line[3]
            data_dict['JLAMHI'] = line[4]
            data_dict['KLAMLO'] = line[5]
            data_dict['KLAMHI'] = line[6]
            continue
        if (line_number==30):            
            data_dict['Zblk'] = line[0]
            data_dict['Nblk'] = line[1]
            data_dict['Nnode'] = line[2]
            data_dict['Fa0'] = line[3]
            data_dict['blindex'] = line[4]
            continue
        #assert not data_dict.has_key(this_param) , ('Config file has multiple specifications of %s' % this_param )       
            
            # otherwise
            # string parameters
                        
        #: for case     
    #: for line
    input_file.close()

    return data_dict
    
#: def read_config18()



# -------------------------------------------------------------------
#  Set ch18 STS Configuration Parameters
# -------------------------------------------------------------------

def write_config18(filename,param_dict):
    """ updates an existing config ch18 file """
    
    #temp_filename = "temp.sts"
   # shutil.copy(filename,temp_filename)
    output_file = open(filename,"w")

    # break pointers
    param_dict_in = copy.deepcopy(param_dict)
    
    sts_file=[]   
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="NONDIMENSION_L   KIND_GRID   NTHREAD"  
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="NVISC   IMP   ISPA   NLIM   NVIDI"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="IRSTRT   MAXSTP   CFL"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="HEIGHT(m)   FSMACH   ALPHA   BETA   TWALL"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="A_REF   L_REF   X_REF   Y_REF   Z_REF"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="ATM_P(Pa)   ATM_R(kg/m3)   ATM_T(K)   GAMMA   PRL   PRT" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="NFIX   FIXD   FIXO   DIIM   VIS2   VIS4" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="NT_SEL   MODI   NTIME   IOUT   ERRTOL   INIT_IT" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="MUSC   NMUSC" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="TSIZE   TMAXSTP   TEND   SUBCFL   N_SUBSTEP   SUB_ERRTOL   IPLT   QST   QRSTP" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="CFL_YNOR   NCYCLE   IDES   I2D" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="NCOMP   CDES   CS" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="IBLK   ILAMLO   ILAMHI   JLAMLO   JLAMHI   KLAMLO   KLAMHI" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="Zblk   Nblk   Nnode   Fa0   blindex" 
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    
    line_number=1
    sts_file[line_number-1]="{0:s}".format(param_dict_in['TaskName'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    
    line_number=3
    sts_file[line_number-1]="{0:s} {1:s} {2:s} ".format(
        param_dict_in['NONDIMENSION_L'],
        param_dict_in['KIND_GRID'],
        param_dict_in['NTHREAD'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=5
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} ".format(                
        param_dict_in['NVISC'],
        param_dict_in['IMP'],
        param_dict_in['ISPA'],
        param_dict_in['NLIM'],
        param_dict_in['NVIDI'] )           
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=7 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} ".format(        
        param_dict_in['IRSTRT'],
        param_dict_in['MAXSTP'],
        param_dict_in['CFL'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=9
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} ".format(
        param_dict_in['HEIGHT'],
        param_dict_in['FSMACH'],
        param_dict_in['ALPHA'],
        param_dict_in['BETA'],
        param_dict_in['TWALL'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=11 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} ".format(        
        param_dict_in['A_REF'],
        param_dict_in['L_REF'],
        param_dict_in['X_REF'],
        param_dict_in['Y_REF'],
        param_dict_in['Z_REF'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=14
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(            
        param_dict_in['ATM_P'],
        param_dict_in['ATM_R'],
        param_dict_in['ATM_T'],
        param_dict_in['GAMMA'],
        param_dict_in['PRL'],
        param_dict_in['PRT'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=16
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(
        param_dict_in['NFIX'],
        param_dict_in['FIXD'],
        param_dict_in['FIXO'],
        param_dict_in['DIIM'],
        param_dict_in['VIS2'],
        param_dict_in['VIS4'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=18
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s} {5:s}".format(            
        param_dict_in['NT_SEL'],
        param_dict_in['MODI'],
        param_dict_in['NTIME'],
        param_dict_in['IOUT'],
        param_dict_in['ERRTOL'],
        param_dict_in['INIT_IT'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=20
    sts_file[line_number-1]="{0:s} {1:s} ".format(        
        param_dict_in['MUSC'],
        param_dict_in['NMUSC'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'   
    line_number=22
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} {7:s} {8:s} ".format(            
        param_dict_in['TSIZE'],
        param_dict_in['TMAXSTP'],
        param_dict_in['TEND'],
        param_dict_in['SUBCFL'],
        param_dict_in['N_SUBSTEP'],
        param_dict_in['SUB_ERRTOL'],
        param_dict_in['IPLT'],
        param_dict_in['QST'],
        param_dict_in['QRSTP'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=24
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} ".format(            
        param_dict_in['CFL_YNOR'],
        param_dict_in['NCYCLE'],
        param_dict_in['IDES'],
        param_dict_in['I2D'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=26
    sts_file[line_number-1]="{0:s} {1:s} {2:s} ".format(            
        param_dict_in['NCOMP'],
        param_dict_in['CDES'],
        param_dict_in['CS'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=28
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} ".format(            
        param_dict_in['IBLK'],
        param_dict_in['ILAMLO'],
        param_dict_in['ILAMHI'],
        param_dict_in['JLAMLO'],
        param_dict_in['JLAMHI'],
        param_dict_in['KLAMLO'],
        param_dict_in['KLAMHI'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=30 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} ".format(        
        param_dict_in['Zblk'],
        param_dict_in['Nblk'],
        param_dict_in['Nnode'],
        param_dict_in['Fa0'],
        param_dict_in['blindex'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'

    # start writing parameter
    output_file.writelines(sts_file)
    
    output_file.close()
#    os.remove( temp_filename )
    
#: def write_config18()


def dump_config18(filename,config):
    ''' dumps a raw config file with all options in config 
        and no comments
    '''
    
    # HACK - twl
    #if config.has_key('DV_VALUE_NEW'):
    #    config.DV_VALUE = config.DV_VALUE_NEW
        
    #config_file = open(filename,'w')
    # write dummy file
    #for key in config.keys():
    #    config_file.write( '%s= 0 \n' % key )
    #config_file.close()
    # dump data
    #write_config(filename,config)    

# -------------------------------------------------------------------
#  Get ch18 STS Configuration Parameters
# Config类的方法结束
# -------------------------------------------------------------------



# ----------------------------------------------------------------------
#  Configuration ch18 trs file Class
# ----------------------------------------------------------------------

class Config18tr(OrderedBunch):
    """ Config18tr = io.Config18tr(filename="")
        
        Starts a config class, an extension of 
        ordered_bunch()
        
        use 1: initialize by reading config file
            config18tr = io.Config18tr('filename')
        use 2: initialize from dictionary or bunch
            config18tr = io.Config18tr(param_dict_in)
        use 3: initialize empty
            config18tr = io.Config18tr()
        
        Parameters can be accessed by item or attribute
        ie: config18['MESH_FILENAME'] or config18tr.MESH_FILENAME
        
        Methods:
            read()       - read from a config file
            write()      - write to a config file (requires existing file)
            dump()       - dump a raw config file
            unpack_dvs() - unpack a design vector 
            diff()       - returns the difference from another config
            dist()       - computes the distance from another config
    """    

    _filename = 'bhcfd18.trs.template'
    
    def __init__(self,*args,**kwarg):
        
        # look for filename in inputs
        if args and isinstance(args[0],str):
            filename = args[0]
            args = args[1:]
        elif kwarg.has_key('filename'):
            filename = kwarg['filename']
            del kwarg['filename']
        else:
            filename = ''
        
        # initialize ordered bunch
        super(Config18tr,self).__init__(*args,**kwarg)
        
        # read config if it exists
        if filename:
            try:
                self.read(filename)
            except:
                raise IOError , 'Could not find config file: %s' % filename
        
        self._filename = filename
    
    def read(self,filename):
        """ reads from a config file """
        konfig = read_config18tr(filename)
        self.update(konfig)
        
    def write(self,filename=''):
        """ updates an existing config file """
        if not filename: filename = self._filename
        #assert os.path.exists(filename) , 'must write over an existing config file'
        write_config18tr(filename,self)
        
    def dump(self,filename=''):
        """ dumps all items in the config bunch, without comments """
        if not filename: filename = self._filename
        dump_config18tr(filename,self)
    
    def __getattr__(self,k):
        try:
            return super(Config18tr,self).__getattr__(k)
        except AttributeError:
            raise AttributeError , 'Config parameter not found'
        
    def __getitem__(self,k):
        try:
            return super(Config18tr,self).__getitem__(k)
        except KeyError:
            raise KeyError , 'Config parameter not found: %s' % k


    def __eq__(self,konfig):
        return super(Config18tr,self).__eq__(konfig)
    def __ne__(self,konfig):
        return super(Config18tr,self).__ne__(konfig)
    
    
    def local_files(self):
        """ removes path prefix from all *_FILENAME params
        """
        for key,value in self.iteritems():
            if key.split('_')[-1] == 'FILENAME':
                self[key] = os.path.basename(value)    
    
    def __repr__(self):
        #return '<Config> %s' % self._filename
        return self.__str__()
    
    def __str__(self):
        output = 'Config: %s' % self._filename
        for k,v in self.iteritems():
            output +=  '\n    %s= %s' % (k,v)
        return output
#: class Config




# -------------------------------------------------------------------
#  Get ch18 trs Configuration Parameters
# Config类的方法
# -------------------------------------------------------------------

def read_config18tr(filename):
    """ reads a config ch18 trs file """
      
    # initialize output dictionary
    data_dict = OrderedDict()
    
    input_file = open(filename)
    
    # process each line
    line_number=0
    while 1:
        # read the line
        line = input_file.readline()
        line_number=line_number+1
        if line_number>27:
            break
        # remove line returns
        line = line.strip('\r\n')
        # make sure it has useful data
        if ("=" in line) or (line[0] == '#') or ("---" in line):
            continue
        #if (filter(str.isalpha,line)) :
        #    continue
        # split across equals sign
        line = line.split()
        #print line
        if (line_number==5):
            data_dict['FSTI'] = line[0]
            data_dict['itsmod'] = line[1]
            data_dict['trmodel'] = line[2]
            data_dict['c_cor'] = line[3]
            data_dict['CFL2'] = line[4]   
            data_dict['deg'] = line[5]
            data_dict['dmax'] = line[6]
            data_dict['perdeg'] = line[7]  
            continue
        if (line_number==7):            
            data_dict['ue_count'] = line[0]
            data_dict['edge_flag'] = line[1]
            data_dict['edge_para'] = line[2]
            data_dict['mut0'] = line[3]
            continue
        if (line_number==10):              
            data_dict['c2'] = line[0]
            data_dict['c3'] = line[1]
            data_dict['c4'] = line[2]
            data_dict['c5'] = line[3]
            data_dict['c6'] = line[4]    
            data_dict['c7'] = line[5]
            data_dict['c8'] = line[6] 
            continue
        if (line_number==12):        
            data_dict['K11'] = line[0]
            data_dict['K12'] = line[1]
            data_dict['K2'] = line[2]
            data_dict['K3'] = line[3]
            data_dict['K4'] = line[4]
            continue
        if (line_number==15):  
            data_dict['ca1'] = line[0]
            data_dict['ca2'] = line[1]
            data_dict['ce1'] = line[2]
            data_dict['ce2'] = line[3]
            data_dict['sigf'] = line[4]
            data_dict['cqt'] = line[5]
            continue
        if (line_number==17):  
            data_dict['sigqt'] = line[0]
            data_dict['1-Sep'] = line[1]
            data_dict['2-Sep'] = line[2]
            data_dict['3-Sep'] = line[3]
            data_dict['fonset'] = line[4]
            data_dict['k1'] = line[5]
            continue
        if (line_number==20):  
            data_dict['gamma_flag'] = line[0]
            data_dict['tr2xall'] = line[1]
            data_dict['tr2c1'] = line[2]
            data_dict['tr2c2'] = line[3]
            data_dict['ReqMe_crt'] = line[4]
            data_dict['Recf_crt'] = line[5]
            continue
        if (line_number==22):  
            data_dict['tr2m1'] = line[0]
            data_dict['tr2m2'] = line[1]
            data_dict['tr2m31'] = line[2]
            data_dict['tr2m32'] = line[3]
            data_dict['tr2m33'] = line[4]
            data_dict['tr2m34'] = line[5]
            continue
        if (line_number==25):    
            data_dict['pgC1'] = line[0]
            data_dict['FonsetC1'] = line[1]
            data_dict['FonsetC2'] = line[2]
            data_dict['wscrit'] = line[3]
            data_dict['wwcrit'] = line[4]
            data_dict['Recfcrit'] = line[5]
            continue
        if (line_number==27):            
            data_dict['fwsflag'] = line[0]
            data_dict['fRecfflag'] = line[1]
            continue
        #assert not data_dict.has_key(this_param) , ('Config file has multiple specifications of %s' % this_param )       
            
            # otherwise
            # string parameters
                        
        #: for case     
    #: for line
    input_file.close()

    return data_dict
    
#: def read_config18tr()



# -------------------------------------------------------------------
#  Set ch18 trs Configuration Parameters
# -------------------------------------------------------------------

def write_config18tr(filename,param_dict):
    """ updates an existing config ch18 trs file """
    
    #temp_filename = "temp.trs"
   # shutil.copy(filename,temp_filename)
    output_file = open(filename,"w")

    # break pointers
    param_dict_in = copy.deepcopy(param_dict)
    
    sts_file=[]
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="sts for transition model"
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="FSTI   itsmod   trmodel   c_cor   CFL2   deg   dmax   perdeg"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="ue_count   edge_flag   edge_para   mut0"  
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="c2   c3   c4   c5   c6   c7   c8"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="K11   K12   K2   K3   K4"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="ca1   ca2   ce1   ce2   sigf   cqt"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="sigqt   1-Sep   2-Sep   3-Sep   fonset   k1"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="gamma_flag   tr2xall   tr2c1   tr2c2   ReqMe_crt   Recf_crt "
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="tr2m1   tr2m2   tr2m31   tr2m32   tr2m33   tr2m34"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="#======================================================================#"
    sts_file.append(raw_line+'\n')
    raw_line="pgC1   FonsetC1   FonsetC2   wscrit   wwcrit   Recfcrit"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line="fwsflag   fRecfflag"
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
    raw_line=""
    sts_file.append(raw_line+'\n')
        
    line_number=5
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} {7:s} ".format(                
        param_dict_in['FSTI'],
        param_dict_in['itsmod'],
        param_dict_in['trmodel'],
        param_dict_in['c_cor'],
        param_dict_in['CFL2'],
        param_dict_in['deg'],
        param_dict_in['dmax'],
        param_dict_in['perdeg'] )           
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=7 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} ".format(        
        param_dict_in['ue_count'],
        param_dict_in['edge_flag'],
        param_dict_in['edge_para'],
        param_dict_in['mut0'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=10
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} {6:s} ".format(
        param_dict_in['c2'],
        param_dict_in['c3'],
        param_dict_in['c4'],
        param_dict_in['c5'],
        param_dict_in['c6'],
        param_dict_in['c7'],
        param_dict_in['c8'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=12 
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} ".format(        
        param_dict_in['K11'],
        param_dict_in['K12'],
        param_dict_in['K2'],
        param_dict_in['K3'],
        param_dict_in['K4'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'    
    line_number=15
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(            
        param_dict_in['ca1'],
        param_dict_in['ca2'],
        param_dict_in['ce1'],
        param_dict_in['ce2'],
        param_dict_in['sigf'],
        param_dict_in['cqt'] )
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=17
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(
        param_dict_in['sigqt'],
        param_dict_in['1-Sep'],
        param_dict_in['2-Sep'],
        param_dict_in['3-Sep'],
        param_dict_in['fonset'],
        param_dict_in['k1'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=20
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s}  {4:s} {5:s}".format(            
        param_dict_in['gamma_flag'],
        param_dict_in['tr2xall'],
        param_dict_in['tr2c1'],
        param_dict_in['tr2c2'],
        param_dict_in['ReqMe_crt'],
        param_dict_in['Recf_crt'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'  
    line_number=22
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(            
        param_dict_in['tr2m1'],
        param_dict_in['tr2m2'],
        param_dict_in['tr2m31'],
        param_dict_in['tr2m32'],
        param_dict_in['tr2m33'],
        param_dict_in['tr2m34'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=25
    sts_file[line_number-1]="{0:s} {1:s} {2:s} {3:s} {4:s} {5:s} ".format(            
        param_dict_in['pgC1'],
        param_dict_in['FonsetC1'],
        param_dict_in['FonsetC2'],
        param_dict_in['wscrit'],
        param_dict_in['wwcrit'],
        param_dict_in['Recfcrit'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'
    line_number=27
    sts_file[line_number-1]="{0:s} {1:s} ".format(            
        param_dict_in['fwsflag'],
        param_dict_in['fRecfflag'])
    sts_file[line_number-1]= sts_file[line_number-1]+'\n'

    # start writing parameter
    output_file.writelines(sts_file)
    
    output_file.close()
#    os.remove( temp_filename )
    
#: def write_config18tr()


def dump_config18tr(filename,config):
    ''' dumps a raw config file with all options in config 
        and no comments
    '''
    
    # HACK - twl
    #if config.has_key('DV_VALUE_NEW'):
    #    config.DV_VALUE = config.DV_VALUE_NEW
        
    #config_file = open(filename,'w')
    # write dummy file
    #for key in config.keys():
    #    config_file.write( '%s= 0 \n' % key )
    #config_file.close()
    # dump data
    #write_config(filename,config)    

# -------------------------------------------------------------------
#  Get ch18 trs Configuration Parameters
# Config类的方法结束
# -------------------------------------------------------------------
