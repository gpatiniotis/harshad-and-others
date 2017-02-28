import math
sm2=0
sm1=0
for i in range(1001):
    if (i<100):
        sm1=(i % 10)
        sm2=(((i+100)/10)%10)
        ath=sm1+sm2
        gin=sm1*sm2
        if(i>0):
            h=float((i+0.0)/ath)
            if (h==(i/ath)):
                print i,"is a harshad number!"
                if (i<10):
                    gin=sm1
                    a=float((i+0.0)/gin)
                    if (a==(i/gin)):
                        print i,"is the other"
            if (sm1!=0 and sm2!=0):
                a=float((i+0.0)/gin)
                if (a==(i/gin)):
                    print i,"is the other"

    elif (i<1000):
        sm1=(i % 10)
        sm2=((i/10)%10)
        t=(i+1000)
        sm3=(t/100)
        sm3=(sm3%10)
        ath=sm1+sm2+sm3
        gin=sm1*sm2*sm3
        h=float((i+0.0)/ath)
        if (h==(i/ath)):
            print i,"is a harshad number!"
        if (sm1!=0 and sm2!=0 and sm3!=0):
            a=float((i+0.0)/gin)
            if (a==(i/gin)):
                print i,"is the other"
