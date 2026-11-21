import struct,sys
def read(path):
    f=open(path,'rb'); d=f.read(); p=0
    hdr=d[:176]; p=176
    comp=struct.unpack('<i',hdr[72:76])[0]; bias=struct.unpack('<d',hdr[92:100])[0]
    vars_=[]
    while True:
        rt=struct.unpack('<i',d[p:p+4])[0]; p+=4
        if rt==2:
            typ,hl,nm,pf,wf=struct.unpack('<iiiii',d[p:p+20]); p+=20
            name=d[p:p+8].decode('latin1').strip(); p+=8
            if hl: n=struct.unpack('<i',d[p:p+4])[0]; p+=4; p+=(n+3)//4*4
            if nm: p+=8*abs(nm)
            vars_.append((name,typ))
        elif rt==3:
            n=struct.unpack('<i',d[p:p+4])[0]; p+=4
            for _ in range(n):
                p+=8; l=d[p]; p+=(l+1+7)//8*8
        elif rt==4:
            n=struct.unpack('<i',d[p:p+4])[0]; p+=4+4*n
        elif rt==6:
            n=struct.unpack('<i',d[p:p+4])[0]; p+=4+80*n
        elif rt==7:
            sub,sz,cnt=struct.unpack('<iii',d[p:p+12]); p+=12+sz*cnt
        elif rt==999:
            p+=4; break
    assert all(t==0 for _,t in vars_), [v for v in vars_ if v[1]!=0]
    nv=len(vars_); vals=[]
    while p<len(d):
        cmd=d[p:p+8]; p+=8
        stop=False
        for c in cmd:
            if c==0: continue
            if c==252: stop=True;break
            if c==253: vals.append(struct.unpack('<d',d[p:p+8])[0]); p+=8
            elif c==255 or c==254: vals.append(None)
            else: vals.append(c-bias)
        if stop: break
    rows=[vals[i:i+nv] for i in range(0,len(vals)//nv*nv,nv)]
    return [v for v,_ in vars_],rows
