
def find_sortedfile(target,filename,findfunc=None,outfunc=None,header=0):
    find = False
    infile = open(filename)
    infile.seek(header,0)
    for row in infile:
        info = findfunc(row)
        if target == info:
            find = True
            break
        elif target < info:
            find = False
            break
        else:
            continue
    infile.close()

    if find:
        return outfunc(row)
    else:
        return None


def quickfind_sortedfile(target,filename,findfunc=None,outfunc=None,header=0):
    infile = open(filename)
    infile.seek(header,0)
    # read the first row
    infile.readline()
    # get the length of each row
    rowlen = infile.tell() - header
    # go to the end of file
    infile.seek(0,2)
    # get the length of the data area of the file
    filelen = infile.tell() - header
    # get the number of rows
    nrows = filelen/rowlen
    # go back to the beginning
    infile.seek(header,0)
    # initialize i1 and i2
    i1 = header
    i2 = header + filelen - rowlen

    count = 0
    while((i2-i1)/rowlen > 1):
        count += 1
        i3 = int((i1+i2)/rowlen/2)*rowlen
        infile.seek(i3,0)
        row3 = infile.read(rowlen)
        info = findfunc(row3)

        if target < info:
            i2 = i3
        elif target > info:
            i1 = i3
        else:
            infile.close()
            return outfunc(row3)

    infile.seek(i1,0)
    while(infile.tell()<i2+rowlen):
        row = infile.read(rowlen)
        if target == findfunc(row):
            infile.close()
            return outfunc(row)
    return None
