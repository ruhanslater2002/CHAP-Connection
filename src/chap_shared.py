# Shared secret
SECRET = "password123"


# Hash function
def chap_hash(challenge, secret):
    import hashlib
    return hashlib.md5((challenge + secret).encode()).hexdigest()
