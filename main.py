originalweight=float(input("请输入你的体重(千克):"))
rate=0.165
weightfactor=0.5
for year in range(1,11):
    earthweight=originalweight+weightfactor*year
    moonweight=earthweight*rate
print("10年后你在地球上的体重是:{:.3f}kg,10年后你在月球上的体重是:{:.3f}kg".format(earthweight,moonweight))
