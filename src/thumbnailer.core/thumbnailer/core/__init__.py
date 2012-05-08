"""thumbnailer.core package."""


class LazyVersion(object):
    """Lazy version information, fetched from file."""
    def __init__(self):
        self._version = None  # Version cache.

    def read_version_file(self):
        """Read version file."""
        import os
        current_dirname = os.path.dirname(os.path.abspath(__file__))
        version_dirname = os.path.normpath(os.path.join(current_dirname, '..',
                                                        '..'))
        version_filename = os.path.join(version_dirname, 'version.txt')
        with open(version_filename) as f:
            return f.readline()

    def __str__(self):
        if self._version is None:
            self._version = self.read_version_file()
        return self._version


version = LazyVersion()
