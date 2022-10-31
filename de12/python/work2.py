name="aaa"
waist=85
age=19

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40: #ここを変更した
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")


if age< 20:
    print(name,"さん、20歳未満の方はご利用できません")