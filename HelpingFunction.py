import time


def createSplitFilename(fileName, i: int, type: str):
    index = fileName.find(type)
    output_line = fileName[:index] + str(i) + fileName[index:]
    return output_line


def timeit(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        ellapsed_time = t2 - t1
        print(f"function {func.__name__} took {ellapsed_time} seconds and produced: {res}")
        return res

    return wrapper


def TryFileLoading(func):
    def wrapper(*arg, **kw):
        try:
            res = func(*arg, **kw)
            return res
        except:
            print("file Not Found")

    return wrapper

def TryMerging(func):
    def wrapper(*arg, **kw):
        try:
            res = func(*arg, **kw)
            return res
        except:
            print("Merging Not Possible")

    return wrapper

def tryThis(func):
    def wrapper(*arg, **kw):
        try:
            res = func(*arg, **kw)
            return res
        except:
            print("failed in Trying:", func)

    return wrapper