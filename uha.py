def uHash(stat):
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
            if not(len(str(q)) <2):
                stat_list.append(ord(stat[q]))
            else:
                stat_list.append(ord(stat[int("0" + str(q))]))

        for t in range(len(stat_list)):
            slice16 = ""
            for m in range(length):
                    idx = int(keys.index(stat_list[t]))
                    number = str((keys[(idx + m)]))
                    if(len(number) < 3):
                        number = "0" + number
                    slice16 += number
                    
            stat_list[t] = slice16
            slice16 = ""
        
        loop = True
        o = 0
        while(loop == True):
            if(o >= (len(stat_list) - 1)):
                o = 0
            if(len(stat_list) == 1):
                loop = False
            else:
                holder = ""
                slice_a = stat_list[o]
                slice_b = stat_list[o + 1]
                slicea = re.findall('..', slice_a)
                sliceb = re.findall('..', slice_b)
                for i in range(len(slicea)):
                    try:
                        num2 = int(sliceb[i])
                    except:
                        pass
                    num3 = int(slicea[i]) + num2
                    if(len(str(num3)) > 2):
                        num3 -= (int(str(num3)[0]) * 100)
                    if(len(str(num3)) != 2):
                        holder += ("0" + str(num3))
                    else:
                        holder += str(num3)
                
                if not(len(stat_list) < 2):
                    stat_list.pop(o + 1)
                    stat_list.pop(o)

                stat_list.append(holder)
                o += 1
            o += 1

        return stat_list[0]