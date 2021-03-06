def ssha_password_hash(*a, **kw):
    from base64 import b64encode
    from hashlib import sha1
    password = a[0]
    salt = a[1]
    pw_hash = sha1(password + salt).digest()
    return '{SSHA}' + b64encode("{}{}".format(pw_hash, salt))


def sha512_password_hash(*a, **kw):
    from crypt import crypt
    password = a[0]
    salt = a[1]
    return crypt(password, '$6${}$'.format(salt))


class FilterModule(object):
    ''' utility filter hash passwords '''

    def filters(self):
        return { 'ssha_password_hash' : ssha_password_hash,
                 'sha512_password_hash' : sha512_password_hash }

