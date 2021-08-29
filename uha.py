def uha(stat):
    import re

    keys = []

    stat= str(stat)

    for z in range(256):
        if(len(str(z)) <2):
            add = "0"
            use = str(z)
            keys.append(add + use)
        else:
            keys.append(z)

    stat_list = []
    length = 32

    for q in range(len(stat)):
        if(len(str(q)) <2):
            add = "0"
            use = str(q)
            stat_list.append(ord(stat[int(add + use)]))
        else:
            stat_list.append(ord(stat[q]))

    for t in range(len(stat_list)):
        slice16 = ""
        letter = stat_list[t]
        for m in range(length):
                idx = int(keys.index(letter))
                number = str((keys[(idx + m)]))
                if(len(number) < 3):
                    number = "0" + number
                slice16 += number
                
        stat_list[t] = slice16
        slice16 = ""

    for o in range(len(stat_list)):
        if((o + 1) > (len(stat_list) - 1)):
            pass
        else:
            holder = ""
            backup = []
            slice_a = stat_list[o]
            slice_b = stat_list[o + 1]
            slicea = re.findall('..', slice_a)
            sliceb = re.findall('..', slice_b)
            for i in range(len(slicea)):
                num1 = int(slicea[i])
                try:
                    num2 = int(sliceb[i])
                except:
                    pass
                num3 = num1 + num2
                if(num3 >= 200):
                    num3 -= 200
                elif(num3 >= 100):
                    num3 -= 100
                elif(num3 >= 300):
                    num3 -= 300
                elif(num3 >= 400):
                    num3 -= 400
                elif(num3 >= 500):
                    num3 -= 500
                if(len(str(num3)) != 2):
                    holder += ("0" + str(num3))
                else:
                    holder += str(num3)
            
            if(len(stat_list) < 2):
                pass
            else:
                backup = stat_list
                backup.pop(o + 1)
                backup.pop(o)
                stat_list = backup
                backup.clear()
            stat_list.append(holder)
            o += 1
        
    # new_list = re.findall('..', stat_list[0])
    # string = ""
    # for b in range(len(new_list)):
    #     string += chr(int(new_list[b]))

    return stat_list[0]