# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf8 -*-
#
# Copyright 2011 Fabian Topfstedt <topfstedt@schneevonmorgen.com>
#
# This module is included with granted permission from the original author.
# The original source is available at http://bitbucket.org/fabian/filechunkio

import io
import os


SEEK_SET = getattr(io, u'SEEK_SET', 0)
SEEK_CUR = getattr(io, u'SEEK_CUR', 1)
SEEK_END = getattr(io, u'SEEK_END', 2)


class FileChunkIO(io.FileIO):
    u"""
    A class that allows you reading only a chunk of a file.
    """
    def __init__(self, name, mode=u'r', closefd=True, offset=0, bytes=None,  # pylint: disable=redefined-builtin
                 *args, **kwargs):  # pylint: disable=redefined-builtin
        u"""
        Open a file chunk. The mode can only be 'r' for reading. Offset
        is the amount of bytes that the chunks starts after the real file's
        first byte. Bytes defines the amount of bytes the chunk has, which you
        can set to None to include the last byte of the real file.
        """
        if not mode.startswith(u'r'):
            raise ValueError(u"Mode string must begin with 'r'")
        self.offset = offset
        self.bytes = bytes
        if bytes is None:
            self.bytes = os.stat(name).st_size - self.offset
        super(FileChunkIO, self).__init__(name, mode, closefd, *args, **kwargs)
        self.seek(0)

    def seek(self, offset, whence=SEEK_SET):
        u"""
        Move to a new chunk position.
        """
        if whence == SEEK_SET:
            super(FileChunkIO, self).seek(self.offset + offset)
        elif whence == SEEK_CUR:
            self.seek(self.tell() + offset)
        elif whence == SEEK_END:
            self.seek(self.bytes + offset)

    def tell(self):
        u"""
        Current file position.
        """
        return super(FileChunkIO, self).tell() - self.offset

    def read(self, n=-1):
        u"""
        Read and return at most n bytes.
        """
        if n >= 0:
            max_n = self.bytes - self.tell()
            n = min([n, max_n])
            return super(FileChunkIO, self).read(n)
        else:
            return self.readall()

    def readall(self):
        u"""
        Read all data from the chunk.
        """
        return self.read(self.bytes - self.tell())

    def readinto(self, b):
        u"""
        Same as RawIOBase.readinto().
        """
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
