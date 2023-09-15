

a = 0
b = 0
c = 0
d = 0



while c < 12:

    if c<1:
        print (str(a))
        a = 1
        d = a + b


        while d>0:
            print (".", end="")
            d-=1

        d = a + b
        print (str(d))      

        a = b
        b = d
        c+=1
        a = 0
        b = 1
        d = 0

    else:

        while d>-1:
            print (".", end="")
            d-=1
        d = a + b
        print (str(d))

        a = b
        b = d

        c+=1

        # 0 1 1 2 3 5 8 13 21 etc
        # is there a better way to fibonacci   ? ? ?? ??? ????? ???????? ????????????? ?????????????????????
        # like in 1 loop only ?!?!?!??!?!?!1111?
        # of course thereis! dumbas!!!!!


'''
    global timestart, curtime, clix

    if timestart == 0:
        timestart = time.time()

    if curtime >= 5:
        z = clix // curtime
        label.config(text=str(z)+" clix per sec")
    else:
        curtime = time.time() - timestart
        clix += 1
        label.config(text="click "+str(curtime)+" seconds\n")
'''

