class Zeit:
    def __init__(self,d,h,m,s):
        self.d = d if d>0    else 0
        self.h = h if 24>h>0 else 0
        self.m = m if 60>m>0 else 0
        self.s = s if 60>s>0 else 0

    def d(self):
        return self.d

    def h(self):
        return self.h

    def m(self):
        return self.m

    def s(self):
        return self.s

    def to_seconds(self):
        return self.s + \
               self.m * 60 + \
               self.h * 60**2 + \
               self.d * 24*60**2
    
    def to_dhhmmss(seconds):
        return (seconds// (24*60**2),
                seconds// 60**2%24,
                seconds// 60%60,
                seconds % 60)

    def __add__(self,other):
        result = Zeit.to_dhhmmss(self.to_seconds() + other.to_seconds())
        return Zeit(result[0],result[1],result[2],result[3])

    def __sub__(self,other):
        diff_seconds = self.to_seconds() - other.to_seconds()
        result = Zeit.to_dhhmmss(0) if diff_seconds < 0 else Zeit.to_dhhmmss(diff_seconds)
        return Zeit(result[0],result[1],result[2],result[3])

    def __str__(self):
        return str(self.d) + 'd ' + \
               str(self.h) + 'h ' + \
               str(self.m) + 'm ' + \
               str(self.s) + 's\n' 
