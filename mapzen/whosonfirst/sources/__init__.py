import spec	# as in: utils/mk-spec.py > mapzen/whosonfirst/sources/spec.py

__NAMES__ = {}
__PREFIXES__ = {}

for id, details in spec.__SPEC__.items():
    name = details['name']
    prefix = details['prefix']

    __NAMES__[name] = id
    __PREFIXES__[prefix] = id

def is_valid_source(k):

    if spec.__SPEC__.get(k, False):
        return True

    if __NAMES__.get(k, False):
        return True

    if __PREFIXES__.get(k, False):
        return True

    return False

def get_source_by_name(n):

    id = __NAMES__.get(n, None)

    if not id:
        return None

    return source(id)

def get_source_by_prefix(p):

    id = __PREFIXES__.get(p, None)

    if not id:
        return None

    return source(id)

def get_source_by_id(id):

    if not spec.__SPEC__.get(id, None):
        return None

    return source(id)

class source:

    def __init__(self, id):

        if not spec.__SPEC__.get(id, False):
            raise Exception("Invalid source ID")

        self.details = spec.__SPEC__[id]

    def __repr__(self):
        return self.stringify()

    def __str__(self):
        return self.stringify()
        
    def stringify(self):

        fullname = self.details['fullname']
        name = self.details['name']
        lookup = self.lookup_key()

        if not lookup:
            return "%s (%s)" % (fullname, name)
        
        return "%s (%s)" % (fullname, lookup)

    def lookup_key(self):
        prefix = self.details['prefix']
        key = self.details['key']

        if key == '':
            return None

        return "%s:%s" % (prefix, key)
