num=0
for num in range(120):
    print(num+1,("番目の人ですね"))
    age   =       input("年齢を入力してください")
    hight = float(input("身長(cm)を入力してください"))
    wight = float(input("体重(kg)を入力してください"))
    name  =       input("お名前を入力してください")

    BMI = wight/(hight*hight*10**-4) #BMI計算　　体重kg ÷ (身長m)^2
    rBMI=round(BMI,1)

    print(name,"さんは身長",hight,"CMで体重は",wight,"kgです。BMIは",rBMI,"です。")
    if  18.5<=BMI<25:
        print(name,"さんは普通体重です。")
    elif BMI<18.5:
            print(name,"さんは痩せています")
    else:
            print(name,"さんは太っています")

