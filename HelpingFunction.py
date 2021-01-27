
def createSplitFilename(fileName, i: int, type: str):
    index = fileName.find(type)
    output_line = fileName[:index] + str(i) + fileName[index:]
    return output_line