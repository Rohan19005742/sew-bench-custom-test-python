class Fake:
    def tri_recursion(self,k):
        #This was done by Rohan
        if(k>0):
            result = k+self.tri_recursion(k-1)
            print(result)
        else:
            result = 0
            print("\n\nRohan")
        return result