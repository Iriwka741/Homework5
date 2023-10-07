#print("Hello teacher")
#print("Homework №5 Banul")
#1.У списку цілих, заповненому випадковими числами обчислити:
#import random
#nums = [random.randint(-10, 10) for _ in range(10)]
#print(nums)
# Суму від'ємних чисел:
#sum_neg = 0

#for num in nums:
  # if num < 0:
  #     sum_neg += num
#print('sum_neg =', sum_neg)

# Суму парних чисел:
#sum_even = 0

#for num in nums:
  # if num % 2 == 0:
   #    sum_even += num
#print('sum_even =', sum_even)

#Cуму непарних чисел:
#sum_odd = 0

#for num in nums:
 #  if num % 2 != 0:
  #     sum_odd += num
#print('sum_odd =', sum_odd)

#Добуток елементів з кратними індексами 3:
#prod_3 = 1

#for i, num in enumerate(nums):
  # if i % 3 == 0:
  #     prod_3 *= num
#print('prod_3 =', prod_3)

#Добуток елементів між мінімальним та максимальним елементом:
#prod_min_max = 1
#min_num = min(nums)
#max_num = max(nums)

#for num in nums:
  # if num > min_num and num < max_num:
   #    prod_min_max *= num

#print('prod_min_max =', prod_min_max)

#Суму елементів, що знаходяться між першим та останнім позитивними елементами:
#sum_pos = 0

#first_found = False
#last_found = False

#for num in nums:
  # if num > 0 and first_found == False:
      # first_found = True
  # elif first_found == True and num > 0:
     #  sum_pos += num
  # elif first_found == True and num < 0:
    #   last_found = True
  # if last_found == True and num > 0:
  #     break

#print('sum_pos =', sum_pos)

#Є список цілих, заповнений випадковими числами.
#На підставі даних цього масиву потрібно:
#■ Створити список цілих, що містить лише парні числа з першого списку;
#■ Створити список цілих, що містить лише непарні числа з першого списку;
#■ Створити список цілих, що містить лише негативні числа з першого списку;
#■ Створити список цілих, що містить лише позитивні числа з першого списку.
def separate_numbers(numbers):
    even = []
    odd = []
    negative = []
    positive = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)
    return even, odd, negative, positive
even, odd, negative, positive = separate_numbers(nums)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Negative numbers:", negative)
print("Positive numbers:", positive)