class A(object):
    def __init__(self,num):
        self.num = num
        self.start_num = -1
    
    def __iter__(self):
        """
        @summary: 迭代器，生成迭代对象时调用，返回值必须是对象自己,然后for可以循环调用next方法
        :return: 
        """

        print ("__iter__")
        return next_ty(self)


def next_ty(self):
        """
        @summary: 每一次for循环都调用该方法（必须存在）
        """

        self.start_num += 1
        if self.start_num >= self.num:
            raise StopIteration()
        return self.start_num
    
if __name__ == "__main__":
    for i in A(10):
        print(i)
