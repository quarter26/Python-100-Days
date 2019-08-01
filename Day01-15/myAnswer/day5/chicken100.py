# 百鸡问题
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 翻译：公鸡1只5块，母鸡1只3块，小鸡3只1块。
# 给你一百块买一百只鸡，能买公鸡母鸡小鸡各多少？

# 分析：公鸡做多买19只，母鸡最多买33只
# 考虑公鸡母鸡，走两个循环

for rooster in range(0, 20):
    for hen in range(0, 33):
        poult = 100 - rooster - hen
        if 5 * rooster + 3 * hen + poult / 3 == 100:
            print('Rooster: %d, hen: %d, poult: %d' % (rooster, hen, poult))
