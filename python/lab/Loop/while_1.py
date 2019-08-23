import random
ans =  random.randint(0,10) #取從1到10的亂數
print('請猜一個0~10的數字')
play = True
while(play):
    guess = int(input('來隨便猜一個數字吧: ')) #input出來預設為str，轉型為int
    if (guess > ans):
        print('喔你猜得太大囉')
    elif (guess < ans):
        print('喔你猜得太小囉')
    else:
        print('恭喜你猜對了！')
        play = False