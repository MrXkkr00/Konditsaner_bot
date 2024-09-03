def find_nomer(msg):
    nomer = "0"
    f = open("./data/reg/hammasi.txt", "r")
    while 1 == 1:
        f_qator = f.readline()
        if msg in f_qator:
            sum = len(f_qator)
            for j in range(sum-14):
                if f_qator[j] == " " and f_qator[j+13]:
                    nomer = f_qator[j+1:j+13]
                if f_qator[j] == " " and f_qator[j+14]:
                    nomer = f_qator[j+1:j+14]
            break
        if f_qator == "":
            break
    f.close()
    return nomer

# print(find_nomer("5542049549"))




