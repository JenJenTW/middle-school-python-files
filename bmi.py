print("本系統採用四捨五入法到個位，若有不便敬請見諒。>w<")
h = float(input("請問您身高多少公分")) / 100.0
w = float(input("請問您體重多少公斤"))
bmi = w / (h * h)
bmi = round(bmi)
print("您的BMI值為",bmi,"。")
#if bmi >= 25:
    #print("您的BMI值為",bmi,"。","有一點胖了喔要記得減肥喔。ξ( ✿＞◡❛)")
    #if bmi >= 35:
        #print("您的BMI值為",bmi,"。","你很胖了喔要記得減肥喔。Σ(lliдﾟﾉ)ﾉ")
