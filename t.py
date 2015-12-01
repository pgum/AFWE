import re
tt = "f/p/1\n\
s1/100/20/10/10/20/40/0/0/0/0/0/0/0\n\
s2/50/0/0/0/5/5/40/0/0/0/0/0/0"
print(tt)

class fheader():
    def __init__(self,hline):
        splitted=hline.split("/")
        self.fname=splitted[0]
        self.fp=splitted[1]
        self.sp=splitted[2]
    def pr(self):
        print("fname: %s, fp: %s, sp: %s" % (self.fname, self.fp, self.sp))

class sline():
    def __init__(self,sline,ssp):
        self.ssp=int(ssp)
        splitted=sline.split("/")
        self.fts=len(splitted) < 3
        if self.fts: return
        self.sname=splitted[0]
        self.i=splitted[1]
        self.rl=splitted[2:]
        self.rl_sum=[x for x in self.rl if x.isdigit()]
    def pr(self):
        if self.fts: return
        st = "sname: %s, in: %s, " % (self.sname, self.i)
        st+= "v: %s" % (", #@ ".join(map(str,self.rl)))
        for x in range(self.ssp,self.ssp+len(self.rl)):
            st=st.replace("@",str(x),1)
        st+= ", rl: %s" % (sum(map(int,self.rl_sum)))
        return st

class ft():
    def __init__(self,txt):
        splitted=txt.split("\n")
        self.hdr=fheader(splitted[0])
        self.sb=list(sline(x,self.hdr.sp) for x in splitted[1:])
        #print(len(list(self.sb)))
        
    def pr(self):
        print("ft pr")
        self.hdr.pr()
        for s in self.sb:
            print(s.pr())
            
    
a=ft(tt)
a.pr()

