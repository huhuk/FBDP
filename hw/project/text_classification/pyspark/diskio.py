
import pickle
def dump(obj, filename):
    f = open(filename, 'wb')
    pickle.dump(obj, f)
    f.close()
def load(filename):
    f = open(filename, 'rb')
    obj = pickle.load(f)
    f.close()
    return obj
