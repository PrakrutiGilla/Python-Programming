class time:

    def __init__(self,h,m):
        self.h=h
        self.m=m

    def addtime(t1,t2):
        t3=time(0,0)
        if (t1.m+t2.m >=60):
            t3.h=int((t1.m+t2.m)/60)
            t3.h=t3.h + t1.h+t2.h
            t3.m=(t1.m+t2.m)%60
        else:    
            t3.h=t1.h+t2.h
            t3.m=t1.m+t2.m
        return t3
    
    def displaytime(self):
        print(" {0}hrs and {1}min ".format(self.h,self.m))

    def displayminute(t3):
        print("minutes = ",t3.h*60+t3.m)

    
a=time(2.0,50)
b=time(1.0,20)
c=time.addtime(a,b)
# the below 2 steps do the same job but are declared differently
c.displaytime()          
e=time.displayminute(c)


