import sys;import os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import sav,statistics as s
n,r=sav.read(sys.argv[1])
r=[[None if v is None else v-100 for v in x] for x in r]
dom=[('العلمية',11),('الاقتصادية',12),('الاجتماعية',13),('الجمالية',15),('السياسية',15),('الدينية',14)]
idx={};c=5
for d,k in dom: idx[d]=list(range(c,c+k)); c+=k
def sc(row,cols):
    v=[4-row[j] for j in cols if row[j] is not None]; return s.mean(v)
def summ(rows,label):
    out={}
    for d,_ in dom:
        m=[sc(x,idx[d]) for x in rows]; out[d]=(round(s.mean(m),2),round(s.stdev(m),2))
    tot=[sc(x,list(range(5,85))) for x in rows]
    print(label,len(rows),sorted(out.items(),key=lambda t:-t[1][0]),'TOTAL',round(s.mean(tot),2))
    return out
summ(r,'ALL')
# economic leave-one-out
for k in range(12):
    cols=[j for j in idx['الاقتصادية'] if j!=idx['الاقتصادية'][k]]
    print('eco drop',k+1,round(s.mean(sc(x,cols) for x in r),3))
summ([x for x in r if x[0]==1],'M'); summ([x for x in r if x[0]==2],'F')
for cval,cn in [(1,'Eng'),(2,'Bus'),(3,'IT')]: summ([x for x in r if x[4]==cval],cn)
# missing
print('missing',sum(v is None for x in r for v in x))
# item level: % choosing A (high) per item
for d,_ in dom:
    for i,j in enumerate(idx[d]):
        col=[x[j] for x in r if x[j] is not None]
        print(d,i+1,'A%',round(100*col.count(1)/len(col)),'B%',round(100*col.count(2)/len(col)),'C%',round(100*col.count(3)/len(col)))
