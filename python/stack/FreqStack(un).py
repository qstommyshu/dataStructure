 class FreqStack(object):

    def __init__(self):
        self.values=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.values.append(x)

    def pop(self):
        """
        :rtype: int
        """
        num = {}
        for item in self.values:
            if item not in num:
                num[str(item)]=1
            elif str(item) in num:
                num[str(item)]+=1
        self.values.pop()
        keyList = list(num.keys())
        valList = list(num.values())
        appear = max(valList)
        position = valList.index(appear)

        return  keyList.index(position)
stack = FreqStack()
print(stack.push(5))
print(stack.push(7))
print(stack.push(5))
print(stack.push(7))
print(stack.push(4))
print(stack.push(5))
print(stack.pop())
print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
print(stack.values)

# num ={}
# values=[1,2,3,1,3,4,5,6,7]
# for item in values:
#     if str(item) not in num:
#         num[str(item)]=1
#     elif str(item) in num:
#         num[str(item)]+=1
# print(num)
