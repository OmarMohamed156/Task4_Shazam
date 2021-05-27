import imagehash

class Hash():
    def generate_hash_code(array) :
        hash = imagehash.phash(array,hash_size=15)
        return hash

