import pdb

def add(a, b):
    return a + b

def cal(a, b):
    pdb.set_trace()
    c = add(a, b)
    print c

if __name__ == "__main__":
    cal(3, 4)