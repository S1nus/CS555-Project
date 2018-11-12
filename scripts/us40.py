import gedcom

def getLineNum(entry, ID, tag):
    lineNum = 0
    try:
        lineNum = entry['lines'][ID + tag]
    except KeyError:
        print('No line number found for given entry and tag')

    return lineNum
