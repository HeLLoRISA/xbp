name=input("名前を教えてください")
waist=input("胸囲は？")
age=input("年齢は？")

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40: #ここを変更した
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")


if age< 20:
    print(name,"さん、20歳未満の方はご利用できません")

if age == 20:
    print("ご成人おめでとうございます")