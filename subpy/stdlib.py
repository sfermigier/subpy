import os
import distutils.sysconfig as sysconfig

jokes = ['antigravity', 'this', 'dbhash', 'bsddb']

def standard_library():
    std_lib = sysconfig.get_python_lib(standard_lib=True)

    for top, dirs, files in os.walk(std_lib):
        for nm in files:
            prefix = top[len(std_lib)+1:]
            if prefix[:13] == 'site-packages':
                continue

            if nm == '__init__.py':
                pack = top[len(std_lib)+1:].replace(os.path.sep,'.')

                if ('.' not in pack) and\
                   (not pack.startswith('_')) and\
                   (pack not in jokes):
                    yield pack

            elif nm[-3:] == '.py':
                pack = os.path.join(prefix, nm)[:-3].replace(os.path.sep,'.')

                if ('.' not in pack) and\
                   (not pack.startswith('_')) and\
                   (pack not in jokes):
                    yield pack

# Python 3.x, todo, this has changed
libraries = [
     'ihooks',
     'quopri',
     'DocXMLRPCServer',
     'shelve',
     'tarfile',
     'CGIHTTPServer',
     'linecache',
     'pdb',
     'sre_parse',
     'user',
     'site',
     'pty',
     'commands',
     'opcode',
     'uu',
     'multifile',
     'pkgutil',
     'dumbdbm',
     'cgi',
     'telnetlib',
     'copy',
     'copy_reg',
     'SimpleXMLRPCServer',
     'textwrap',
     'xmlrpclib',
     'MimeWriter',
     'threading',
     'mailbox',
     'gettext',
     'contextlib',
     'sndhdr',
     'HTMLParser',
     'hashlib',
     'BaseHTTPServer',
     'posixfile',
     'csv',
     'struct',
     'urlparse',
     'rexec',
     'htmllib',
     'asynchat',
     'sha',
     'dis',
     'warnings',
     'heapq',
     'types',
     'token',
     'netrc',
     'mimetypes',
     'anydbm',
     'Bastion',
     'subprocess',
     'imputil',
     'imghdr',
     'macurl2path',
     'trace',
     'atexit',
     'rfc822',
     'imaplib',
     'getpass',
     'md5',
     'base64',
     'sre',
     'cookielib',
     'fileinput',
     'keyword',
     'tty',
     'mutex',
     'timeit',
     'markupbase',
     'stat',
     'mimetools',
     'fpformat',
     'pprint',
     'httplib',
     'fnmatch',
     'zipfile',
     'mhlib',
     'ssl',
     'cProfile',
     'aifc',
     'ftplib',
     'pstats',
     'optparse',
     'dummy_threading',
     'sre_compile',
     'py_compile',
     'uuid',
     'stringold',
     'sunau',
     'Cookie',
     'asyncore',
     'wave',
     'sgmllib',
     'new',
     'getopt',
     'audiodev',
     'fractions',
     'inspect',
     'ast',
     'statvfs',
     'UserString',
     'decimal',
     'codecs',
     'os2emxpath',
     'hmac',
     'genericpath',
     'sunaudio',
     'Queue',
     'sched',
     'cgitb',
     'mailcap',
     'pipes',
     'smtplib',
     'doctest',
     'xmllib',
     'numbers',
     'os',
     'dummy_thread',
     'code',
     'sre_constants',
     'colorsys',
     'modulefinder',
     'bdb',
     'calendar',
     'urllib',
     'abc',
     'SocketServer',
     'UserList',
     'dircache',
     'pydoc',
     'weakref',
     'ConfigParser',
     'pickletools',
     're',
     'posixpath',
     'chunk',
     'mimify',
     'binhex',
     'tabnanny',
     'rlcompleter',
     'runpy',
     'pyclbr',
     'stringprep',
     'glob',
     'nntplib',
     'popen2',
     'formatter',
     'functools',
     'symtable',
     'repr',
     'smtpd',
     'macpath',
     'pickle',
     'sets',
     'string',
     'urllib2',
     'shutil',
     'shlex',
     'xdrlib',
     'sysconfig',
     'profile',
     'gzip',
     'tokenize',
     'robotparser',
     'socket',
     'difflib',
     'UserDict',
     'platform',
     'argparse',
     'plistlib',
     'cmd',
     'nturl2path',
     'locale',
     'tempfile',
     'random',
     'toaiff',
     'webbrowser',
     'SimpleHTTPServer',
     'collections',
     'bisect',
     'symbol',
     'htmlentitydefs',
     'io',
     'whichdb',
     'traceback',
     'filecmp',
     'compileall',
     'ntpath',
     'codeop',
     'StringIO',
     'poplib',
     'email',
     'json',
     'multiprocessing',
     'hotshot',
     'xml',
     'unittest',
     'lib2to3',
     'encodings',
     'distutils',
     'idlelib',
     'wsgiref',
     'curses',
     'importlib',
     'compiler',
     'sqlite3',
     'ctypes',
     'logging'
 ]
