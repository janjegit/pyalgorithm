class Tree:
    def __init__(self,left=None,value=None,right=None):
        self.parent=None
        if value==None or left==None or right==None:
            self.empty=True
        else:
            self.empty=False
            self.value=value
            self.left=left
            self.right=right

    def to_list(self):
        if self.empty:
            return []
        else:
            ll=self.left.to_list()
            lr=self.right.to_list()
            return ll+[self.value]+lr

    def add_parents(self,prev=None):
        self.parent=prev
        if not self.left.empty:
            self.left.add_parents(self)
        if not self.right.empty: 
            self.right.add_parents(self)

    def empty_stack(self):
        return ()
    
    def is_empty(self,s):
        return s == ()

    def push(self,v,s):
        return (v,s)

    def top(self,s):
        return None if self.is_empty(s) else s[0]

    def pop(self,s):
        return self.empty_stack() if self.is_empty(s) else s[1]

    def to_list_iter(self):
        st = self.empty_stack()
        ret_st = self.empty_stack()
        st = self.push(('list',self),st)
        while not self.is_empty(st):
            nxt = self.top(st)
            st = self.pop(st)
            fun = nxt[0]
            if fun=='list':
                tree = nxt[1]
                if tree.empty:
                    ret_st = self.push([],ret_st)
                else:
                    ll=tree.left
                    lr=tree.right
                    st = self.push(('+',),st)
                    ret_st = self.push([tree.value],ret_st)
                    st = self.push(('list',lr),st)
                    st = self.push(('list',ll),st)
            elif fun=='+':
                r0 = self.top(ret_st)
                ret_st = self.pop(ret_st)
                r1 = self.top(ret_st)
                ret_st = self.pop(ret_st)
                r2 = self.top(ret_st)
                ret_st = self.pop(ret_st)
                ret_st = self.push(r1+r2+r0,ret_st)
        return self.top(ret_st)

test_tree1 = Tree(Tree(Tree(),42,Tree()),55,Tree(Tree(),73,Tree()))
test_tree2 = Tree(test_tree1,0,test_tree1)
print(test_tree1.to_list_iter())
print(test_tree2.to_list_iter())

test_tree2.add_parents()
print(test_tree2.left.left.parent.value) #55
print(test_tree2.left.parent.right.left.value) #42
