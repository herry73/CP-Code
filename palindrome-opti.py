        temp=x
        rev=0
        while(x>0):
            rev=rev*10+x%10
            x=x//10
        return temp==rev