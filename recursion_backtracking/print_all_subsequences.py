def all_subsequences(l, index, ds):
    if index == len(l)-1:
        print(ds)
        return

    ds.append(l[index])
    all_subsequences(l,index+1,ds)
    ds.pop()
    all_subsequences(l,index+1,ds)

if __name__=="__main__":
    l = [3,1,4,2]
    ds = []
    all_subsequences(l,0,ds)
