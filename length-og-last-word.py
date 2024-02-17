        i = len(s) - 1
        while i>=0 and s[i] == ' ':
            i-=1
        Last = i
        while i>=0 and s[i] != ' ':
            i-=1
        return (Last-i)