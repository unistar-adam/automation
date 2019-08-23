import random
ans =  random.randint(0,10) #取從1到10的亂數
times = 0
print('請猜一個0~10的數字')
play = True

while(play):
    try:
        guess = int(input('來隨便猜一個數字吧: ')) #input出來預設為str，轉型為int
    except:
        print('程式出現非預期的錯誤，遊戲結束，答案是'+str(ans))
        #str()是將數字轉文字，'+'串接的必須是同樣的型態。
        play = False
    else:
        times = times+1 #每猜一次就要+1
        if (guess > ans):
            print('喔你猜得太大囉')
        elif (guess < ans):
            print('喔你猜得太小囉')
        else:
            print('恭喜你猜對了！')
            play = False
    finally:
        print('你猜了'+str(times)+'次') 