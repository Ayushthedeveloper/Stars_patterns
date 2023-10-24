def roman_number(num):

    if num<=3999:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # num = int(input("Give the number"))
        roman = ""
        i = 0
        while num>0:
            div = num//numbers[i]
            num = num % numbers[i]
            while div>0:
                roman += syms[i]
                div -= 1
            i += 1
        return roman
    else:
        print("Please enter a number smalller than 3999")
print(roman_number(int(input("Give the number"))))