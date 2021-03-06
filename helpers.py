from datetime import datetime

class classproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)

def surround(s, markup):
    return markup + s + markup[::-1]

def bold(s):
    return surround(s, '**')

def underline(s):
    return surround(s, '__')

def code(s):
    return surround(s, '`')

def codeblock(s):
    return '```\n' + s + '\n```'

def at(s):
    return "<@%s>" % s

def noembed(s):
    return "<%s>" % s

def chan(s):
    return "<#%s>" % s

def nick(m):
    return m.nick or str(m).split("#")[0]

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

class CommandFailure(Exception):
    pass
