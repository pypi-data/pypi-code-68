# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import builtins
import collections
import collections.abc
import functools
import importlib
import importlib.util
import itertools
import os
import re
import sys
import types

from collections import UserDict
from . import typecheck as typ


def seconds_to_hms(seconds):
    '''Convert time in seconds to hours, minutes and seconds.

    :arg seconds: The time in seconds.
    :returns: A three-element tuple such as ``(hours, minutes, seconds)``.

    :meta private:

    '''

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s


def _get_module_name(filename):
    barename, _ = os.path.splitext(filename)
    if os.path.basename(filename) == '__init__.py':
        barename = os.path.dirname(filename)

    if os.path.isabs(barename):
        raise AssertionError('BUG: _get_module_name() '
                             'accepts relative paths only')

    if filename.startswith('..'):
        return os.path.basename(barename)
    else:
        return barename.replace(os.sep, '.')


def _do_import_module_from_file(filename, module_name=None):
    module_name = module_name or _get_module_name(filename)
    if module_name in sys.modules:
        return sys.modules[module_name]

    spec = importlib.util.spec_from_file_location(module_name, filename)
    if spec is None:
        raise ImportError("No module named '%s'" % module_name,
                          name=module_name, path=filename)

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def import_module_from_file(filename):
    '''Import module from file.

    :arg filename: The path to the filename of a Python module.
    :returns: The loaded Python module.
    '''

    # Expand and sanitize filename
    filename = os.path.abspath(os.path.expandvars(filename))
    if os.path.isdir(filename):
        filename = os.path.join(filename, '__init__.py')

    # Express filename relative to reframe
    rel_filename = os.path.relpath(filename, sys.path[0])
    module_name = _get_module_name(rel_filename)
    if rel_filename.startswith('..'):
        # We cannot use the standard Python import mechanism here, because the
        # module to import is outside the top-level package
        return _do_import_module_from_file(filename, module_name)

    # Extract module name if `filename` is under `site-packages/` or the
    # Debian specific `dist-packages/`
    site_packages = re.compile(r'.*(site|dist)-packages/(?P<rel_filename>.+)')
    match = site_packages.search(filename)
    if match:
        module_name = _get_module_name(match['rel_filename'])

    return importlib.import_module(module_name)


def allx(iterable):
    '''Same as the built-in :py:func:`all`, except that it returns
    :class:`False` if ``iterable`` is empty.
    '''

    # Generators must be treated specially, because there is no way to get
    # their size without consuming their elements.
    if isinstance(iterable, types.GeneratorType):
        try:
            head = next(iterable)
        except StopIteration:
            return False
        else:
            return all(itertools.chain([head], iterable))

    if not isinstance(iterable, collections.abc.Iterable):
        raise TypeError("'%s' object is not iterable" %
                        iterable.__class__.__name__)

    return all(iterable) if iterable else False


def decamelize(s, delim='_'):
    '''Decamelize a string.

    For example, ``MyBaseClass`` will be converted to ``my_base_class``.
    The delimiter may be changed by setting the ``delim`` argument.

    :arg s: A string in camel notation.
    :arg delim: The delimiter that will be used to separate words.
    :returns: The converted string.
    '''

    if not isinstance(s, str):
        raise TypeError('decamelize() requires a string argument')

    if not s:
        return ''

    return re.sub(r'([a-z])([A-Z])', r'\1%s\2' % delim, s).lower()


def toalphanum(s):
    '''Convert string ``s`` by replacing any non-alphanumeric character with
    ``_``.

    :arg s: The string to convert.
    :returns: The converted string.

    :meta private:
    '''

    if not isinstance(s, str):
        raise TypeError('toalphanum() requires a string argument')

    if not s:
        return ''

    return re.sub(r'\W', '_', s)


def ppretty(value, htchar=' ', lfchar='\n', indent=4, basic_offset=0,
            repr=builtins.repr):
    '''Format value in a pretty way.

    If value is a container, this function will recursively format the
    container's elements.

    :arg value: The value to be formatted.
    :arg htchar: Horizontal-tab character.
    :arg lfchar: Linefeed character.
    :arg indent: Number of ``htchar`` characters for every indentation level.
    :arg basic_offset: Basic offset for the representation, any additional
        indentation space is added to the ``basic_offset``.
    :arg repr: A :py:func:`repr`-like function that will be used for printing
        values. This function is allowed to accept all the arguments of
        :func:`ppretty` except the ``repr`` argument.

    :returns: A formatted string of ``value``.

    '''

    ppretty2 = functools.partial(
        ppretty, htchar=htchar, lfchar=lfchar, indent=indent,
        basic_offset=basic_offset+1, repr=repr
    )
    nlch = lfchar + htchar * indent * (basic_offset + 1)
    if isinstance(value, tuple):
        if value == ():
            return '()'

        items = [nlch + ppretty2(item) for item in value]
        return '(%s)' % (','.join(items) + lfchar +
                         htchar * indent * basic_offset)
    elif isinstance(value, list):
        if value == []:
            return '[]'

        items = [
            nlch + ppretty2(item)
            for item in value
        ]
        return '[%s]' % (','.join(items) + lfchar +
                         htchar * indent * basic_offset)
    elif isinstance(value, dict):
        if value == {}:
            return '{}'

        items = [
            nlch + repr(key) + ': ' + ppretty2(value[key]) for key in value
        ]
        return '{%s}' % (','.join(items) + lfchar +
                         htchar * indent * basic_offset)
    elif isinstance(value, set):
        if value == set():
            return 'set()'

        items = [nlch + ppretty2(item) for item in value]
        return '{%s}' % (','.join(items) + lfchar +
                         htchar * indent * basic_offset)
    else:
        try:
            return repr(value, htchar, lfchar, indent, basic_offset)
        except TypeError:
            # Not our custom repr()
            return repr(value)


def _tracked_repr(func):
    objects = set()

    @functools.wraps(func)
    def _repr(obj, *args, **kwargs):
        addr = id(obj)
        if addr in objects:
            return f'{type(obj).__name__}(...)@{hex(addr)}'

        # Do not track builtin objects
        if hasattr(obj, '__dict__'):
            objects.add(addr)

        return func(obj, *args, **kwargs)

    return _repr


@_tracked_repr
def repr(obj, htchar=' ', lfchar='\n', indent=4, basic_offset=0):
    '''A |builtin.repr|_ replacement function for debugging purposes printing
    all object attributes recursively.

    This function does not follow the standard |builtin.repr|_ convention, but
    it prints each object as a set of key/value pairs along with its memory
    location. It also keeps track of the already visited objects, and
    abbreviates their representation.

    :arg obj: The object to be dumped.
        For the rest of the arguments, see :func:`ppretty`.
    :returns: The formatted object dump.

    .. _builtin.repr: https://docs.python.org/3/library/functions.html#repr
    .. |builtin.repr| replace:: :js:func:`repr()`

    '''
    if (isinstance(obj, list) or isinstance(obj, tuple) or
        isinstance(obj, set) or isinstance(obj, dict)):
        return ppretty(obj, basic_offset=basic_offset, repr=repr)

    if not hasattr(obj, '__dict__'):
        return builtins.repr(obj)

    r = ppretty(obj.__dict__, htchar, lfchar, indent, basic_offset, repr)
    return f'{type(obj).__name__}({r})@{hex(id(obj))}'


def shortest(*iterables):
    '''Return the shortest sequence.

    This function raises a :py:class:`TypeError` if any of the iterables is
    not |Sized|_.

    :arg iterables: The iterables to check.
    :returns: The shortest iterable.

    .. _Sized: https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized # noqa: E501
    .. |Sized| replace:: :class:`Sized`
    '''

    ret = None
    for seq in iterables:
        if not isinstance(seq, collections.abc.Sized):
            raise TypeError(f'expected a sized iterable: {seq}')

        if ret is None:
            ret = seq
            continue

        if len(seq) < len(ret):
            ret = seq

    return ret


def longest(*iterables):
    '''Return the longest sequence.

    This function raises a :py:class:`TypeError` if any of the iterables is
    not |Sized|_.

    :arg iterables: The iterables to check.
    :returns: The longest iterable.

    '''

    ret = None
    for seq in iterables:
        if not isinstance(seq, collections.abc.Sized):
            raise TypeError(f'expected a sized iterable: {seq}')

        if ret is None:
            ret = seq
            continue

        if len(seq) > len(ret):
            ret = seq

    return ret


def find_modules(substr, environ_mapping=None):
    '''Return all modules in the current system that contain ``substr`` in
    their name.

    This function is a generator and will yield tuples of partition,
    environment and module combinations for each partition of the current
    system and for each environment of a partition.

    The ``environ_mapping`` argument allows you to map module name patterns to
    ReFrame environments. This is useful for flat module name schemes, in
    order to avoid incompatible combinations of modules and environments.

    You can use this function to parametrize regression tests over the
    available environment modules. The following example will generate tests
    for all the available ``netcdf`` packages in the system:

    .. code:: python

       @rfm.parameterized_test(*find_modules('netcdf'))
       class MyTest(rfm.RegressionTest):
           def __init__(self, s, e, m):
               self.descr = f'{s}, {e}, {m}'
               self.valid_systems = [s]
               self.valid_prog_environs = [e]
               self.modules = [m]
               ...

    The following example shows the use of ``environ_mapping`` with flat
    module name schemes. In this example, the toolchain for which the package
    was built is encoded in the module's name. Using the ``environ_mapping``
    argument we can map module name patterns to ReFrame environments, so that
    invalid combinations are pruned:

    .. code:: python

       my_find_modules = functools.partial(find_modules, environ_mapping={
           r'.*CrayGNU.*': {'PrgEnv-gnu'},
           r'.*CrayIntel.*': {'PrgEnv-intel'},
           r'.*CrayCCE.*': {'PrgEnv-cray'}
       })

       @rfm.parameterized_test(*my_find_modules('GROMACS'))
       class MyTest(rfm.RegressionTest):
           def __init__(self, s, e, m):
               self.descr = f'{s}, {e}, {m}'
               self.valid_systems = [s]
               self.valid_prog_environs = [e]
               self.modules = [m]
               ...

    :arg substr: A substring that the returned module names must contain.
    :arg environ_mapping: A dictionary mapping regular expressions to
        environment names.

    :returns: An iterator that iterates over tuples of the module, partition
        and environment name combinations that were found.
    '''

    import reframe.core.runtime as rt

    if not isinstance(substr, str):
        raise TypeError("'substr' argument must be a string")

    if (environ_mapping is not None and
        not isinstance(environ_mapping, typ.Dict[str, str])):
        raise TypeError(
            "'environ_mapping' argument must be of type Dict[str,str]"
        )

    def _is_valid_for_env(m, e):
        if environ_mapping is None:
            return True

        for patt, environs in environ_mapping.items():
            if re.match(patt, m) and e in environs:
                return True

        return False

    ms = rt.runtime().modules_system
    current_system = rt.runtime().system
    snap0 = rt.snapshot()
    for p in current_system.partitions:
        for e in p.environs:
            rt.loadenv(p.local_env, e)
            modules = ms.available_modules(substr)
            snap0.restore()
            for m in modules:
                if _is_valid_for_env(m, e.name):
                    yield (p.fullname, e.name, m)


class ScopedDict(UserDict):
    '''This is a special dictionary that imposes scopes on its keys.

    When a key is not found, it will be searched up in the scope hierarchy.
    If not found even at the global scope, a :class:`KeyError` will be raised.

    A scoped dictionary is initialized using a two-level normal dictionary
    that defines the different scopes and the keys inside them. Scopes can be
    nested by concatenating them using the ``:`` separator by default:
    ``scope:subscope``. Below is an example of a scoped dictionary that also
    demonstrates key lookup:

    .. code-block:: python

       d = ScopedDict({
           'a': {'k1': 1, 'k2': 2},
           'a:b': {'k1': 3, 'k3': 4},
           '*': {'k1': 7, 'k3': 9, 'k4': 10}
       })

       assert d['a:k1'] == 1    # resolved in the scope 'a'
       assert d['a:k3'] == 9    # resolved in the global scope
       assert d['a:b:k1'] == 3  # resolved in the scope 'a:b'
       assert d['a:b:k2'] == 2  # resolved in the scope 'a'
       assert d['a:b:k4'] == 10 # resolved in the global scope
       d['a:k5']    # KeyError
       d['*:k2']    # KeyError

    If no scope is specified in the key lookup, the global scope is assumed.
    For example, ``d['k1']`` will return ``7``. The syntaxes ``d[':k1']`` and
    ``d['*:k1']`` are all equivalent.
    If you try to retrieve a whole scope, e.g., ``d['a:b']``,
    :class:`KeyError` will be raised.

    Key deletion follows the same resolution mechanism as key retrieval,
    except that you are allowed to delete whole scopes. For example, ``del
    d['*']`` will delete the global scope, such that subsequent access of
    ``d['a:k3']`` will raise a :class:`KeyError`. If a key specification
    matches both a key and scope, the key will be deleted and not the scope.

    :arg mapping: A two-level mapping of the form

      .. code-block:: python

         {
              scope1: {k1: v1, k2: v2},
              scope2: {k1: v1, k3: v3}
         }

      Both the scope keys and the actual dictionary keys must be
      strings, otherwise a :class:`TypeError` will be raised.

    :arg scope_sep: A character that separates the scopes.
    :arg global_scope: A key that represents the global scope.

    '''

    def __init__(self, mapping={}, scope_sep=':', global_scope='*'):
        super().__init__(mapping)
        self._scope_sep = scope_sep
        self._global_scope = global_scope

    @property
    def scope_separator(self):
        '''The scope separator of this dictionary.'''
        return self._scope_sep

    @property
    def global_scope_mark(self):
        '''The key representing the global scope of this dictionary.'''
        return self._global_scope

    def update(self, other):
        '''Update this dictionary from the values of a two-level mapping as
        described above.

        :arg other: A two-level mapping defining scopes and keys.
        '''
        if not isinstance(other, collections.abc.Mapping):
            raise TypeError('ScopedDict may only be initialized '
                            'from a mapping type')

        for scope, scope_dict in other.items():
            self._check_scope_type(scope, scope_dict)
            self.data.setdefault(scope, {})
            for k, v in scope_dict.items():
                self.data[scope][k] = v

    def __str__(self):
        # just return the internal dictionary
        return str(self.data)

    def _check_scope_type(self, key, value):
        if not isinstance(key, str):
            raise TypeError('scope keys in a ScopedDict must be strings')

        if not isinstance(value, collections.abc.Mapping):
            raise TypeError('scope namespaces must be mappings')

        for k in value.keys():
            if not isinstance(k, str):
                raise TypeError('keys must be strings')

    def _keyinfo(self, key):
        key_parts = key.rsplit(self._scope_sep, maxsplit=1)
        if len(key_parts) == 2:
            return (key_parts[0], key_parts[1])
        else:
            return (self._global_scope, key_parts[0])

    def _parent_scope(self, scope):
        scope_parts = scope.rsplit(':', maxsplit=1)[:-1]
        return scope_parts[0] if scope_parts else self._global_scope

    def _lookup(self, key):
        scope, lookup_key = self._keyinfo(key)
        while scope != self._global_scope:
            if scope in self.data and lookup_key in self.data[scope]:
                return self.data[scope][lookup_key]

            scope = self._parent_scope(scope)

        # last chance to find the key
        if scope in self.data and lookup_key in self.data[scope]:
            return self.data[scope][lookup_key]

        raise KeyError(str(key))

    def __iter__(self):
        for scope, scope_dict in self.data.items():
            for k in scope_dict.keys():
                yield self._scope_sep.join([scope, k])

    def __contains__(self, key):
        try:
            self._lookup(key)
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key):
        try:
            return self._lookup(key)
        except KeyError:
            return self.__missing__(key)

    def __setitem__(self, key, value):
        scope, lookup_key = self._keyinfo(key)
        if scope not in self.data:
            # create the scope if does not exist
            self.data[scope] = {}

        self.data[scope][lookup_key] = value

    def __delitem__(self, key):
        '''Deletes either a key or a scope if key refers to a scope.

        If key refers to both a scope and a key, the key will be deleted.
        If key refers to scope, the whole scope entry will be deleted.
        If not, the exact key requested will be deleted.
        No key resolution will be performed.'''
        scope, lookup_key = self._keyinfo(key)
        if scope in self.data and lookup_key in self.data[scope]:
            del self.data[scope][lookup_key]
        elif key in self.data:
            # key is a scope
            del self.data[key]
        else:
            raise KeyError(str(key))

    def __missing__(self, key):
        raise KeyError(str(key))


@functools.total_ordering
class OrderedSet(collections.abc.MutableSet):
    '''An ordered set.

    This container behaves like a normal set but remembers the insertion order
    of its elements. It can also inter-operate with standard Python sets.

    Operations between ordered sets respect the order of the elements of the
    operands. For example, if ``x`` and ``y`` are both ordered sets, then ``x
    | y`` will be a new ordered set with the (unique) elements of ``x`` and
    ``y`` in the order they appear in ``x`` and ``y``. The same holds for all
    the other set operations.

    '''

    def __init__(self, *args):
        # We need to allow construction without arguments
        if not args:
            iterable = []
        elif len(args) == 1:
            iterable = args[0]
        else:
            # We use the exact same error message as for the built-in set
            raise TypeError('%s expected at most 1 arguments, got %s' %
                            type(self).__name__, len(args))

        if not isinstance(iterable, collections.abc.Iterable):
            raise TypeError("'%s' object is not iterable" %
                            type(iterable).__name__)

        # We implement an ordered set through the keys of an OrderedDict;
        # its values are all set to None
        self.__data = collections.OrderedDict(
            itertools.zip_longest(iterable, [], fillvalue=None)
        )

    def __repr__(self):
        vals = self.__data.keys()
        if not vals:
            return type(self).__name__ + '()'
        else:
            return '{' + ', '.join(repr(v) for v in vals) + '}'

    # Container i/face
    def __contains__(self, item):
        return item in self.__data

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    # Set i/face
    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            if len(self) != len(other):
                return False

            for x, y in zip(self, other):
                if x != y:
                    return False

            return True
        elif isinstance(other, collections.abc.Set):
            return set(self.__data.keys()) == other
        else:
            return NotImplemented

    def __gt__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        return set(self.__data.keys()) > other

    def __and__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        ret = type(self)()
        for x in shortest(self, other):
            if x in self and x in other:
                ret.add(x)

        return ret

    def __or__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        ret = type(self)()
        for x in itertools.chain(self, other):
            ret.add(x)

        return ret

    def __sub__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        ret = type(self)(self.__data.keys())
        for x in other:
            if x in ret:
                ret.remove(x)

        return ret

    def __xor__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        ret = type(self)()
        for x in itertools.chain(self, other):
            if x in self and x in other:
                continue

            ret.add(x)

        return ret

    def isdisjoint(self, other):
        '''See same method in :py:class:`set`.'''

        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        return set(self.__data.keys()).isdisjoint(other)

    def issubset(self, other):
        '''See same method in :py:class:`set`.'''

        return self <= other

    def issuperset(self, other):
        '''See same method in :py:class:`set`.'''

        return self >= other

    def symmetric_difference(self, other):
        '''See same method in :py:class:`set`.'''

        return self ^ other

    def union(self, *others):
        '''See same method in :py:class:`set`.'''

        ret = type(self)(self)
        for s in others:
            ret |= s

        return ret

    def intersection(self, *others):
        '''See same method in :py:class:`set`.'''

        ret = type(self)(self)
        for s in others:
            ret &= s

        return ret

    def difference(self, *others):
        '''See same method in :py:class:`set`.'''

        ret = type(self)(self)
        for s in others:
            ret -= s

        return ret

    # MutableSet i/face

    def add(self, elem):
        '''See same method in :py:class:`set`.'''

        self.__data[elem] = None

    def remove(self, elem):
        '''See same method in :py:class:`set`.'''

        del self.__data[elem]

    def discard(self, elem):
        '''See same method in :py:class:`set`.'''

        try:
            self.remove(elem)
        except KeyError:
            pass

    def pop(self):
        '''See same method in :py:class:`set`.'''

        return self.__data.popitem()[0]

    def clear(self):
        '''See same method in :py:class:`set`.'''

        self.__data.clear()

    def __ior__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        for e in other:
            self.add(e)

        return self

    def __iand__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        discard_list = [e for e in self if e not in other]
        for e in discard_list:
            self.discard(e)

        return self

    def __isub__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        for e in other:
            self.discard(e)

        return self

    def __ixor__(self, other):
        if not isinstance(other, collections.abc.Set):
            return NotImplemented

        discard_list = [e for e in self if e in other]
        for e in discard_list:
            self.discard(e)

        return self

    # Other functions
    def __reversed__(self):
        return reversed(self.__data.keys())


class SequenceView(collections.abc.Sequence):
    '''A read-only view of a sequence.

    See :py:class:`collections.abc.Sequence` for a list of supported of
    operations.

    :arg container: The container to create a view on.
    :raises TypeError: If the container does not fulfill the
        :py:class:`collections.abc.Sequence` interface.

    '''

    def __init__(self, container):
        if not isinstance(container, collections.abc.Sequence):
            raise TypeError('container must be of type Sequence')

        self.__container = container

    def count(self, value):
        '''Count occurrences of ``value`` in the container.

        :arg value: The value to search for.
        :returns: The number of occurrences.
        '''
        return self.__container.count(value)

    def index(self, value, start=0, stop=None):
        '''Return the first index of ``value``.

        :arg value: The value to search for.
        :arg start: The position where the search starts.
        :arg stop: The position where the search stops. The element at this
            position is not looked at. If :class:`None`, this equals to the
            sequence's length.
        :returns: The index of the first element found that equals ``value``.
        :raises ValueError: if the value is not present.

        '''

        if stop is None:
            stop = len(self.__container)

        return self.__container.index(value, start, stop)

    def __contains__(self, value):
        return self.__container.__contains__(value)

    def __getitem__(self, index):
        return self.__container.__getitem__(index)

    def __iter__(self):
        return self.__container.__iter__()

    def __len__(self):
        return self.__container.__len__()

    def __reversed__(self):
        return self.__container.__reversed__()

    def __add__(self, other):
        if not isinstance(other, collections.abc.Sequence):
            return NotImplemented

        return SequenceView(self.__container + other)

    def __iadd__(self, other):
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, SequenceView):
            return self.__container == other.__container

        return self.__container == other

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.__container)

    def __str__(self):
        return str(self.__container)


class MappingView(collections.abc.Mapping):
    '''A read-only view of a mapping.

    See :py:class:`collections.abc.Mapping` for a list of supported of
    operations.
    '''

    def __init__(self, mapping):
        if not isinstance(mapping, collections.abc.Mapping):
            raise TypeError('container must be of type Mapping')

        self.__mapping = mapping

    def get(self, key, default=None):
        '''Return the value mapped to ``key`` or ``default``, if ``key`` does
        not exist.

        :arg key: The key to look up.
        :arg default: The default value to return if the key is not present.
        :returns: The value associated to the requested key.
        '''
        return self.__mapping.get(key, default)

    def keys(self):
        '''Return a set-like object providing a view on the underlying
        mapping's keys.'''
        return self.__mapping.keys()

    def items(self):
        '''Return a set-like object providing a view on the underlying
        mapping's items.'''
        return self.__mapping.items()

    def values(self):
        '''Return a set-like object providing a view on the underlying
        mapping's values.'''
        return self.__mapping.values()

    def __contains__(self, key):
        return self.__mapping.__contains__(key)

    def __getitem__(self, key):
        return self.__mapping.__getitem__(key)

    def __iter__(self):
        return self.__mapping.__iter__()

    def __len__(self):
        return self.__mapping.__len__()

    def __eq__(self, other):
        if isinstance(other, MappingView):
            return self.__mapping == other.__mapping

        return self.__mapping.__eq__(other)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.__mapping)

    def __str__(self):
        return str(self.__mapping)
