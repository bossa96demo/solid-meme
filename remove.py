name = input("what is username printed in neofetch? : ")
with open('neofetch.txt', 'r') as f:
    i = 0
    txt = f.readline()
    while txt[i]!=name[0]:
        i+=1
    out = open("out.txt", "w")
    foo = f.readlines()
    for txt in foo:
        for j in range(i):
            try:
                out.write(txt[j])
            except Exception as e:
                pass
        out.write('\n')
    print("Done")
out.close()
f.close()
