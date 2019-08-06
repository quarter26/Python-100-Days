# 练习5：计算指定的年月日是这一年的第几天

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def day_in_year(year, month, day):
    month_list = (1,2,3,4,5,6,7,8,9,10,11,12)
    if type(year) != int or type(day) != int:
        print("Wrong type")
    elif year == 0 or day < 1 or day > 31 or month not in month_list:
        print('Wrong input')
    else:
        days_of_month = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ]
        #     days_of_month = [
        # [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        # [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # ][is_leap_year(year)]
        # 答案上这么些写的，不太明白
        return (day + sum(days_of_month[1][:month - 1])) if is_leap_year(year) else (day + sum(days_of_month[0][:month - 1]))

def main():
    print(day_in_year(1980, 11, 28))
    print(day_in_year(1981, 12, 31))
    print(day_in_year(2018, 1, 1))
    print(day_in_year(2016, 3, 1))

if __name__ == '__main__':
    main()
