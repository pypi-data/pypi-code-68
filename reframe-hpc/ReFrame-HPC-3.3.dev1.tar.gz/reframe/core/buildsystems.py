# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import abc
import os

import reframe.core.fields as fields
import reframe.utility.typecheck as typ
from reframe.core.exceptions import BuildSystemError


class BuildSystem(abc.ABC):
    '''The abstract base class of any build system.

    Concrete build systems inherit from this class and must override the
    :func:`emit_build_commands` abstract function.
    '''

    #: The C compiler to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the compiler defined in the current programming environment will be
    #: used.
    #:
    #: :type: :class:`str`
    #: :default: ``''``
    cc  = fields.TypedField('cc', str)

    #: The C++ compiler to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the compiler defined in the current programming environment will be
    #: used.
    #:
    #: :type: :class:`str`
    #: :default: ``''``
    cxx = fields.TypedField('cxx', str)

    #: The Fortran compiler to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the compiler defined in the current programming environment will be
    #: used.
    #:
    #: :type: :class:`str`
    #: :default: ``''``
    ftn = fields.TypedField('ftn', str)

    #: The CUDA compiler to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the compiler defined in the current programming environment will be
    #: used.
    #:
    #: :type: :class:`str`
    #: :default: ``''``
    nvcc = fields.TypedField('nvcc', str)

    #: The C compiler flags to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the corresponding flags defined in the current programming environment
    #: will be used.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    cflags = fields.TypedField('cflags', typ.List[str])

    #: The preprocessor flags to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the corresponding flags defined in the current programming environment
    #: will be used.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    cppflags = fields.TypedField('cppflags', typ.List[str])

    #: The C++ compiler flags to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the corresponding flags defined in the current programming environment
    #: will be used.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    cxxflags = fields.TypedField('cxxflags', typ.List[str])

    #: The Fortran compiler flags to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the corresponding flags defined in the current programming environment
    #: will be used.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    fflags  = fields.TypedField('fflags', typ.List[str])

    #: The linker flags to be used.
    #: If empty and :attr:`flags_from_environ` is :class:`True`,
    #: the corresponding flags defined in the current programming environment
    #: will be used.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    ldflags = fields.TypedField('ldflags', typ.List[str])

    #: Set compiler and compiler flags from the current programming environment
    #: if not specified otherwise.
    #:
    #: :type: :class:`bool`
    #: :default: :class:`True`
    flags_from_environ = fields.TypedField('flags_from_environ', bool)

    def __init__(self):
        self.cc  = ''
        self.cxx = ''
        self.ftn = ''
        self.nvcc = ''
        self.cflags = []
        self.cxxflags = []
        self.cppflags = []
        self.fflags  = []
        self.ldflags = []
        self.flags_from_environ = True

    @abc.abstractmethod
    def emit_build_commands(self, environ):
        '''Return the list of commands for building using this build system.

        The build commands may always assume to be issued from the top-level
        directory of the code that is to be built.

        :arg environ: The programming environment for which to emit the build
           instructions.
           The framework passes here the current programming environment.
        :type environ: :class:`reframe.core.environments.ProgEnvironment`
        :raises: :class:`BuildSystemError` in case of errors when generating
          the build instructions.

        .. note::
            This method is relevant only to developers of new build systems.
        '''

    def _resolve_flags(self, flags, environ):
        _flags = getattr(self, flags)
        if _flags:
            return _flags

        if self.flags_from_environ:
            return getattr(environ, flags)

        return None

    def _cc(self, environ):
        return self._resolve_flags('cc', environ)

    def _cxx(self, environ):
        return self._resolve_flags('cxx', environ)

    def _ftn(self, environ):
        return self._resolve_flags('ftn', environ)

    def _nvcc(self, environ):
        return self._resolve_flags('nvcc', environ)

    def _cppflags(self, environ):
        return self._resolve_flags('cppflags', environ)

    def _cflags(self, environ):
        return self._resolve_flags('cflags', environ)

    def _cxxflags(self, environ):
        return self._resolve_flags('cxxflags', environ)

    def _fflags(self, environ):
        return self._resolve_flags('fflags', environ)

    def _ldflags(self, environ):
        return self._resolve_flags('ldflags', environ)


class Make(BuildSystem):
    '''A build system for compiling codes using ``make``.

    The generated build command has the following form:

    .. code::

      make -j [N] [-f MAKEFILE] [-C SRCDIR] CC="X" CXX="X" FC="X" NVCC="X" CPPFLAGS="X" CFLAGS="X" CXXFLAGS="X" FCFLAGS="X" LDFLAGS="X" OPTIONS

    The compiler and compiler flags variables will only be passed if they are
    not :class:`None`.
    Their value is determined by the corresponding attributes of
    :class:`BuildSystem`.
    If you want to completely disable passing these variables to the ``make``
    invocation, you should make sure not to set any of the correspoding
    attributes and set also the :attr:`BuildSystem.flags_from_environ` flag to
    :class:`False`.
    '''

    #: Append these options to the ``make`` invocation.
    #: This variable is also useful for passing variables or targets to
    #: ``make``.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    options = fields.TypedField('options', typ.List[str])

    #: Instruct build system to use this Makefile.
    #: This option is useful when having non-standard Makefile names.
    #:
    #: :type: :class:`str`
    #: :default: :class:`None`
    makefile = fields.TypedField('makefile', str, type(None))

    #: The top-level directory of the code.
    #:
    #: This is set automatically by the framework based on the
    #: :attr:`reframe.core.pipeline.RegressionTest.sourcepath` attribute.
    #:
    #: :type: :class:`str`
    #: :default: :class:`None`
    srcdir = fields.TypedField('srcdir', str, type(None))

    #: Limit concurrency for ``make`` jobs.
    #: This attribute controls the ``-j`` option passed to ``make``.
    #: If not :class:`None`, ``make`` will be invoked as ``make -j
    #: max_concurrency``.
    #: Otherwise, it will invoked as ``make -j``.
    #:
    #: :type: integer
    #: :default: ``1``
    #:
    #: .. note::
    #:     .. versionchanged:: 2.19
    #:        The default value is now ``1``
    max_concurrency = fields.TypedField('max_concurrency', int, type(None))

    def __init__(self):
        super().__init__()
        self.options = []
        self.makefile = None
        self.srcdir = None
        self.max_concurrency = 1

    def emit_build_commands(self, environ):
        cmd_parts = ['make']
        if self.makefile:
            cmd_parts += ['-f %s' % self.makefile]

        if self.srcdir:
            cmd_parts += ['-C %s' % self.srcdir]

        cmd_parts += ['-j']
        if self.max_concurrency is not None:
            cmd_parts += [str(self.max_concurrency)]

        cc = self._cc(environ)
        cxx = self._cxx(environ)
        ftn = self._ftn(environ)
        nvcc = self._nvcc(environ)
        cppflags = self._cppflags(environ)
        cflags   = self._cflags(environ)
        cxxflags = self._cxxflags(environ)
        fflags   = self._fflags(environ)
        ldflags  = self._ldflags(environ)
        if cc:
            cmd_parts += ['CC="%s"' % cc]

        if cxx:
            cmd_parts += ['CXX="%s"' % cxx]

        if ftn:
            cmd_parts += ['FC="%s"' % ftn]

        if nvcc:
            cmd_parts += ['NVCC="%s"' % nvcc]

        if cppflags:
            cmd_parts += ['CPPFLAGS="%s"' % ' '.join(cppflags)]

        if cflags:
            cmd_parts += ['CFLAGS="%s"' % ' '.join(cflags)]

        if cxxflags:
            cmd_parts += ['CXXFLAGS="%s"' % ' '.join(cxxflags)]

        if fflags:
            cmd_parts += ['FCFLAGS="%s"' % ' '.join(fflags)]

        if ldflags:
            cmd_parts += ['LDFLAGS="%s"' % ' '.join(ldflags)]

        if self.options:
            cmd_parts += self.options

        return [' '.join(cmd_parts)]


class SingleSource(BuildSystem):
    '''A build system for compiling a single source file.

    The generated build command will have the following form:

    .. code::

      COMP CPPFLAGS XFLAGS SRCFILE -o EXEC LDFLAGS

    - ``COMP`` is the required compiler for compiling ``SRCFILE``.
      This build system will automatically detect the programming language of
      the source file and pick the correct compiler.
      See also the :attr:`SingleSource.lang` attribute.
    - ``CPPFLAGS`` are the preprocessor flags and are passed to any compiler.
    - ``XFLAGS`` is any of ``CFLAGS``, ``CXXFLAGS`` or ``FCFLAGS`` depending on
      the programming language of the source file.
    - ``SRCFILE`` is the source file to be compiled.
      This is set up automatically by the framework.
      See also the :attr:`SingleSource.srcfile` attribute.
    - ``EXEC`` is the executable to be generated.
      This is also set automatically by the framework.
      See also the :attr:`SingleSource.executable` attribute.
    - ``LDFLAGS`` are the linker flags.

    For CUDA codes, the language assumed is C++ (for the compilation flags) and
    the compiler used is :attr:`BuildSystem.nvcc`.

    '''

    #: The source file to compile.
    #: This is automatically set by the framework based on the
    #: :attr:`reframe.core.pipeline.RegressionTest.sourcepath` attribute.
    #:
    #: :type: :class:`str` or :class:`None`
    srcfile = fields.TypedField('srcfile', str, type(None))

    #: The executable file to be generated.
    #:
    #: This is set automatically by the framework based on the
    #: :attr:`reframe.core.pipeline.RegressionTest.executable` attribute.
    #:
    #: :type: :class:`str` or :class:`None`
    executable = fields.TypedField('executable', str, type(None))

    #: The include path to be used for this compilation.
    #:
    #: All the elements of this list will be appended to the
    #: :attr:`BuildSystem.cppflags`, by prepending to each of them the ``-I``
    #: option.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    include_path = fields.TypedField('include_path', typ.List[str])

    #: The programming language of the file that needs to be compiled.
    #: If not specified, the build system will try to figure it out
    #: automatically based on the extension of the source file.
    #: The automatically detected extensions are the following:
    #:
    #:   - C: `.c` and `.upc`.
    #:   - C++: `.cc`, `.cp`, `.cxx`, `.cpp`, `.CPP`, `.c++` and `.C`.
    #:   - Fortran: `.f`, `.for`, `.ftn`, `.F`, `.FOR`, `.fpp`, `.FPP`, `.FTN`,
    #:     `.f90`, `.f95`, `.f03`, `.f08`, `.F90`, `.F95`, `.F03` and `.F08`.
    #:   - CUDA: `.cu`.
    #:
    #: :type: :class:`str` or :class:`None`
    lang = fields.TypedField('lang', str, type(None))

    def __init__(self):
        super().__init__()
        self.srcfile = None
        self.executable = None
        self.include_path = []
        self.lang = None

    def _auto_exec_name(self):
        return '%s.x' % os.path.splitext(self.srcfile)[0]

    def emit_build_commands(self, environ):
        if not self.srcfile:
            raise BuildSystemError(
                'a source file is required when using the %s build system' %
                type(self).__name__)

        cc = self._cc(environ)
        cxx = self._cxx(environ)
        ftn = self._ftn(environ)
        nvcc = self._nvcc(environ)
        cppflags = self._cppflags(environ) or []
        cflags   = self._cflags(environ) or []
        cxxflags = self._cxxflags(environ) or []
        fflags   = self._fflags(environ)  or []
        ldflags  = self._ldflags(environ) or []

        # Adjust cppflags with the include directories
        # NOTE: We do not use the += operator on purpose, be cause we don't
        # want to change the original list passed by the user
        cppflags = cppflags + [*map(lambda d: '-I ' + d, self.include_path)]

        # Generate the executable
        executable = self.executable or self._auto_exec_name()

        # Prepare the compilation command
        lang = self.lang or self._guess_language(self.srcfile)
        cmd_parts = []
        if lang == 'C':
            if not cc:
                raise BuildSystemError('I do not know how to compile a '
                                       'C program')

            cmd_parts += [cc, *cppflags, *cflags, self.srcfile,
                          '-o', executable, *ldflags]
        elif lang == 'C++':
            if not cxx:
                raise BuildSystemError('I do not know how to compile a '
                                       'C++ program')

            cmd_parts += [cxx, *cppflags, *cxxflags, self.srcfile,
                          '-o', executable, *ldflags]
        elif lang == 'Fortran':
            if not ftn:
                raise BuildSystemError('I do not know how to compile a '
                                       'Fortran program')

            cmd_parts += [ftn, *cppflags, *fflags, self.srcfile,
                          '-o', executable, *ldflags]
        elif lang == 'CUDA':
            if not nvcc:
                raise BuildSystemError('I do not know how to compile a '
                                       'CUDA program')

            cmd_parts += [nvcc, *cppflags, *cxxflags, self.srcfile,
                          '-o', executable, *ldflags]
        else:
            BuildSystemError('could not guess language of file: %s' %
                             self.srcfile)

        return [' '.join(cmd_parts)]

    def _guess_language(self, filename):
        _, ext = os.path.splitext(filename)
        if ext in ['.c', '.upc']:
            return 'C'

        if ext in ['.cc', '.cp', '.cxx', '.cpp', '.CPP', '.c++', '.C']:
            return 'C++'

        if ext in ['.f', '.for', '.ftn', '.F', '.FOR', '.fpp',
                   '.FPP', '.FTN', '.f90', '.f95', '.f03', '.f08',
                   '.F90', '.F95', '.F03', '.F08']:
            return 'Fortran'

        if ext in ['.cu']:
            return 'CUDA'


class ConfigureBasedBuildSystem(BuildSystem):
    '''Abstract base class for configured-based build systems.'''

    #: The top-level directory of the code.
    #:
    #: This is set automatically by the framework based on the
    #: :attr:`reframe.core.pipeline.RegressionTest.sourcepath` attribute.
    #:
    #: :type: :class:`str`
    #: :default: :class:`None`
    srcdir = fields.TypedField('srcdir', str, type(None))

    #: The CMake build directory, where all the generated files will be placed.
    #:
    #: :type: :class:`str`
    #: :default: :class:`None`
    builddir = fields.TypedField('builddir', str, type(None))

    #: Additional configuration options to be passed to the CMake invocation.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    config_opts = fields.TypedField('config_opts', typ.List[str])

    #: Options to be passed to the subsequent ``make`` invocation.
    #:
    #: :type: :class:`List[str]`
    #: :default: ``[]``
    make_opts = fields.TypedField('make_opts', typ.List[str])

    #: Same as for the :attr:`Make` build system.
    #:
    #: :type: integer
    #: :default: ``1``
    max_concurrency = fields.TypedField('max_concurrency', int, type(None))

    def __init__(self):
        super().__init__()
        self.srcdir = None
        self.builddir = None
        self.config_opts = []
        self.make_opts = []
        self.max_concurrency = 1


class CMake(ConfigureBasedBuildSystem):
    '''A build system for compiling CMake-based projects.

    This build system will emit the following commands:

    1. Create a build directory if :attr:`builddir` is not :class:`None` and
       change to it.
    2. Invoke ``cmake`` to configure the project by setting the corresponding
       CMake flags for compilers and compiler flags.
    3. Issue ``make`` to compile the code.
    '''

    def _combine_flags(self, cppflags, xflags):
        if not cppflags:
            return xflags

        ret = list(cppflags)
        if xflags:
            ret += xflags

        return ret

    def emit_build_commands(self, environ):
        prepare_cmd = []
        if self.srcdir:
            prepare_cmd += ['cd %s' % self.srcdir]

        if self.builddir:
            prepare_cmd += ['mkdir -p %s' % self.builddir,
                            'cd %s' % self.builddir]

        cmake_cmd = ['cmake']
        cc = self._cc(environ)
        cxx = self._cxx(environ)
        ftn = self._ftn(environ)
        nvcc = self._nvcc(environ)
        cppflags = self._cppflags(environ)
        cflags   = self._combine_flags(cppflags, self._cflags(environ))
        cxxflags = self._combine_flags(cppflags, self._cxxflags(environ))
        fflags   = self._combine_flags(cppflags, self._fflags(environ))
        ldflags  = self._ldflags(environ)
        if cc:
            cmake_cmd += ['-DCMAKE_C_COMPILER="%s"' % cc]

        if cxx:
            cmake_cmd += ['-DCMAKE_CXX_COMPILER="%s"' % cxx]

        if ftn:
            cmake_cmd += ['-DCMAKE_Fortran_COMPILER="%s"' % ftn]

        if nvcc:
            cmake_cmd += ['-DCMAKE_CUDA_COMPILER="%s"' % nvcc]

        if cflags:
            cmake_cmd += ['-DCMAKE_C_FLAGS="%s"' % ' '.join(cflags)]

        if cxxflags:
            cmake_cmd += ['-DCMAKE_CXX_FLAGS="%s"' % ' '.join(cxxflags)]

        if fflags:
            cmake_cmd += ['-DCMAKE_Fortran_FLAGS="%s"' % ' '.join(fflags)]

        if ldflags:
            cmake_cmd += ['-DCMAKE_EXE_LINKER_FLAGS="%s"' % ' '.join(ldflags)]

        if self.config_opts:
            cmake_cmd += self.config_opts

        if self.builddir:
            cmake_cmd += [os.path.relpath('.', self.builddir)]
        else:
            cmake_cmd += ['.']

        make_cmd = ['make -j']
        if self.max_concurrency is not None:
            make_cmd += [str(self.max_concurrency)]

        if self.make_opts:
            make_cmd += self.make_opts

        return prepare_cmd + [' '.join(cmake_cmd), ' '.join(make_cmd)]


class Autotools(ConfigureBasedBuildSystem):
    '''A build system for compiling Autotools-based projects.

    This build system will emit the following commands:

    1. Create a build directory if :attr:`builddir` is not :class:`None` and
       change to it.
    2. Invoke ``configure`` to configure the project by setting the
       corresponding flags for compilers and compiler flags.
    3. Issue ``make`` to compile the code.
    '''

    def emit_build_commands(self, environ):
        prepare_cmd = []
        if self.srcdir:
            prepare_cmd += ['cd %s' % self.srcdir]

        if self.builddir:
            prepare_cmd += ['mkdir -p %s' % self.builddir,
                            'cd %s' % self.builddir]

        if self.builddir:
            configure_cmd = [os.path.join(
                os.path.relpath('.', self.builddir), 'configure')]
        else:
            configure_cmd = ['./configure']

        cc = self._cc(environ)
        cxx = self._cxx(environ)
        ftn = self._ftn(environ)
        cppflags = self._cppflags(environ)
        cflags   = self._cflags(environ)
        cxxflags = self._cxxflags(environ)
        fflags   = self._fflags(environ)
        ldflags  = self._ldflags(environ)
        if cc:
            configure_cmd += ['CC="%s"' % cc]

        if cxx:
            configure_cmd += ['CXX="%s"' % cxx]

        if ftn:
            configure_cmd += ['FC="%s"' % ftn]

        if cppflags:
            configure_cmd += ['CPPFLAGS="%s"' % ' '.join(cppflags)]

        if cflags:
            configure_cmd += ['CFLAGS="%s"' % ' '.join(cflags)]

        if cxxflags:
            configure_cmd += ['CXXFLAGS="%s"' % ' '.join(cxxflags)]

        if fflags:
            configure_cmd += ['FCFLAGS="%s"' % ' '.join(fflags)]

        if ldflags:
            configure_cmd += ['LDFLAGS="%s"' % ' '.join(ldflags)]

        if self.config_opts:
            configure_cmd += self.config_opts

        make_cmd = ['make -j']
        if self.max_concurrency is not None:
            make_cmd += [str(self.max_concurrency)]

        if self.make_opts:
            make_cmd += self.make_opts

        return prepare_cmd + [' '.join(configure_cmd), ' '.join(make_cmd)]


class BuildSystemField(fields.TypedField):
    def __init__(self, fieldname, *other_types):
        super().__init__(fieldname, BuildSystem, *other_types)

    def __set__(self, obj, value):
        if isinstance(value, str):
            try:
                value = globals()[value]()
            except KeyError:
                raise ValueError('unknown build system: %s' % value) from None

        super().__set__(obj, value)
