n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
MIMEtype = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    MIMEtype[ext] = mt
for i in range(q):
    fname = input()  # One file name per line.
    if '.' in fname :
        fname = fname.split('.')
        if fname[-1].lower() in MIMEtype and fname[-1].isalnum() and ' ' not in fname:
            print(MIMEtype[fname[-1].lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")