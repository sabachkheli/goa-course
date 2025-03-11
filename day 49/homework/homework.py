def dup(arry):
    result = []
    
    for i in arry:
        test = ""

        for x in range(len(i)):
            if test == "" or i[x] != test[-1]:
                test += i[x]
                
        result.append(test)
    return result


# dsrulet saklaso davaleba: classwork in classworks folder