from Crypto.PublicKey import RSA

key = RSA.importKey(open('pub.key').read())
print("N: ",key.n, "E: ",key.e)

def egcd(a, b):
    """Extended Euclidean algorithm"""
    x,y,u,v = 0,1,1,0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b,a,x,y,u,v = a,r,u,v,m,n
    return b, x, y

def modinv(e, m):
    """Modular multiplicative inverse"""
    g, x, y = egcd(e, m)
    if g != 1:
        return None
    else:
        return x % m

def pqe2rsa(p, q, e):
    """Generate an RSA private key from p, q and e"""
    from Crypto.PublicKey import RSA
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    key_params = (int(n), int(e), int(d), int(p), int(q))
    priv_key = RSA.construct(key_params)
    print (priv_key.exportKey())


pqe2rsa(887015894239637,556893302969702090191386807196541351626579623872633,65537)
