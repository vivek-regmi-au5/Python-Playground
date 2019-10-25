# # print("Twinkle, twinkle, little star, \n \tHow I wonder what you are!\n \t \t Up above the world so high,\nLike a diamond in the sky. \n \tTwinkle, twinkle, little star, \n \tHow I wonder what yor


# # def check_range():
# #     input_num = int(input("Please enter a number: "))
# #     if abs(input_num - 1000) < 100 or abs(input_num - 2000) < 100:
# #         print(True)
# #     else:
# #         print(False)


# # check_range()

# # def add_is():
# #     input_string = input("Enter a string: ")
# #     if input_string[0] == "I" and input_string[1] == "s":
# #         return input_string
# #     else:
# #         return "Is" + input_string


# # print(add_is())

# # n_int = int(input("Please enter a number: "))
# # input_str = input("Please enter a string: ")
# # for num in range(n_int):
# #     print(input_str)

# # n_int = int(input("Please enter a number: "))
# # if n_int % 2 == 0:
# #     print("It is an even number")
# # else:
# #     print("It is odd")

# # count = 0


# # def count_four(listt):
# #     count = 0
# #     for num in range(len(listt)):
# #         if listt[num] == 4:
# #             count += 1
# #     return count


# # print(count_four([1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 4, 4]))

# # def first_two():
# #     input_int = int(input("Please enter a number: "))
# #     input_str = input("Please enter a string: ")
# #     for numn in range(input_int):
# #         print(input_str[0] + " " + input_str[1])


# # first_two()

# # def check_vowel():

# #     input_str = input("Please enter a string: ")
# #     for char in input_str:
# #         if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
# #             print("It is a vowel")
# #         else:
# #             print("Not a vowel")


# # check_vowel()

# # 3
# # [1, 2, 3, 4, 5, 6]

# # check_value = int(input("Please enter what to check: "))
# # check_list = int(input("Enter a list of data"))


# # for char in check_list:
# #     if char == check_value:
# #         print("Exists")
# #     else:
# #         print("Deson't exists")


# # def check_presence():
# #     check_list = [1, 2, 3, 4, 5, 6]
# #     check_value = 3
# #     for char in check_list:
# #         if char == check_value:
# #             print("Exists")
# #             return
# #     print("Doesnot exists")


# # check_presence()\

# # import matplotlib.pyplot as plt
# # import numpy as np
# # import pandas as pd
# # x = np.random.random_integers(1, 100, 5)
# # plt.hist(x, bins=20)
# # plt.ylabel('No of times')
# # plt.show()

# # num_list = [2, 5, 7, 3]

# # for num in num_list:
# #     print("@"*num)
# # n_list = ["d", "d", "d", "d"]

# # print("".join(n_list))

# # numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# #            399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# #            815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
# #            958, 743, 527]
# # for num in numbers:
# #     if num % 2 == 0 and num < 237:
# #         print(num)

# # color_list_1 = set(["White", "Black", "Red"])
# # color_list_2 = set(["Red", "Green"])
# # print(color_list_1.difference(color_list_2))
# # import glob
# # import multiprocessing
# # import math


# # def check_GDB():

# #     int_1 = int(input("Please enter a number: "))
# #     int_2 = int(input("Please enter another number: "))

# #     if int_1 - int_2 < 0:
# #         smaller_num = int_1
# #         big_num = int_2
# #     else:
# #         smaller_num = int_2
# #         big_num = int_1
# #     print(smaller_num)
# #     print(big_num)

# #     if big_num % smaller_num == 0:
# #         print(smaller_num)
# #         return

# #     for num in range(smaller_num, 0, -1):
# #         if big_num % num == 0:
# #             print(num)
# #             return


# # check_GDB()

# # def get_LCM():
# #     int_1 = int(input("Please enter a number: "))
# #     int_2 = int(input("Please enter another number: "))

# #     if int_1 - int_2 < 0:
# #         smaller_num = int_1
# #         big_num = int_2
# #     else:
# #         smaller_num = int_2
# #         big_num = int_1
# #     if big_num % smaller_num == 0:
# #         print(big_num)
# #         return
# #     for num in range(1, smaller_num + 1):
# #         if big_num*num % smaller_num == 0:
# #             print(big_num*num)
# #             return


# # get_LCM()
# # import os.path
# # import struct
# # open("abc.txt", "w")
# # print(os.path.isfile("abc.tx"))
# # print(struct.calcsize("P") * 8)

# # import platform
# # import os

# # print(platform.system())
# # print(platform.release())

# # import site
# # print(site.getsitepackages())

# # from subprocess import call
# # call("touch newfile.txt")

# # import os
# # print("Current File Name : ", os.path.realpath(__file__))
# # print(multiprocessing.cpu_count())

# # print(int(float("274.67")))
# # import glob
# # txtfiles = []
# # for file in glob.glob("*.txt"):
# #     txtfiles.append(file)

# # def count_len(str):
# #     count = 0
# #     for _ in str:
# #         count += 1
# #     print(count)


# # str_inp = input("Please enter a string: ")
# # result = {}
# # for char in str_inp:
# #     if not char in result.keys():
# #         result[char] = 1
# #     else:
# #         result[char] += 1
# # print(result)
# # num = {'w': 1, 's': 2, 'd': 1, 'e': 2, 'f': 2, 'g': 1}

# # for k in num.items():
# #     print(k)

# # inp_str = input("Please enter a str: ")
# # result = "".join([inp_str[0], inp_str[1], inp_str[-1], inp_str[-2]])
# # print(result)
# # def conv_str():

# #     inp_str = input("Please enter a string: ")
# #     first_char = inp_str[0]
# #     result = first_char
# #     for char in inp_str[1:]:
# #         if char == first_char:
# #             char = "$"
# #             result += char
# #         else:
# #             result += char
# #     print(result)


# # conv_str()
# # str = "Abcdeedrfgtyj"


# # str = str + "abc"
# # print(str)

# # def swap_char():
# #     first_str = input("Please enter a str: ")
# #     second_str = input("Please enter a str: ")
# #     first_two = first_str[0:2]
# #     second_two = second_str[0:2]
# #     print(first_two)
# #     print(second_two)
# #     first_str = first_str.replace(first_str[0:2], second_two)
# #     second_str = second_str.replace(second_str[0:2], first_two)
# #     print(first_str + " " + second_str)


# # swap_char()
# # str = "asdfggjhsdfdfgk"
# # print(str[-:])


# # def add_ing():
# #     user_str = input("enter a string: ")
# #     if user_str[-3:] == "ing":
# #         user_str += "ly"
# #     else:
# #         user_str += "ing"
# #     print(user_str)


# # add_ing()

# # def check_sub():
# #     str = input("Please enter a string:")
# #     not_index = str.index("not")
# #     poor_index = str.index("poor")
# #     if not_index < poor_index:
# #         str = str.replace(str[not_index:(poor_index + 4)], "good")
# #         print(str)

# # check_sub()

# # def longest_str(words):
# #     result = ""
# #     result_len = 0
# #     for word in words:
# #         length = len(word)
# #         if length > result_len:
# #             result_len = length
# #             result = word
# #     print(result)


# # longest_str(["abd", "wdf", "swfdafg", "As",
# #              "asdsgerhyrth", "k", "hgfgrfdrfedsghvhgvhg"])

# # my_list = ["abc", "def"]
# # my_list.append("lmn")
# # print(my_list)

# # def nt_index():
# #     str = "This is the new shit"
# #     inp = int(input("Enter a number: "))
# #     str = str.replace(str[inp], "", 1)
# #     print(str)


# # nt_index()

# # def exchanged():
# #     str = input("Please enter a str: ")
# #     first = str[0]
# #     #last = str[-1]
# #     str = str.replace(str[0], str[-1])
# #     str = str.replace(str[-1], first)

# #     # # str = input("Please enter a str: ")
# #     #first = str[0]
# #     #last = str[-1]
# #     #str1 = str.replace(str[0], last)
# #     #str2 = str1.replace(str1[-1], first)
# #     #print(str[-1] + str[1:-1] + str[0])
# #     print(str)


# # exchanged()
# # # str = "Vivek"
# # # print(str[-1])

# # ikasjhfksd
# # 0123456789


# # def removeOdd():
# #     user_input = input("Please enter a string: ")
# #     for char in user_input:
# #         if user_input.index(char) % 2 != 0:
# #             user_input = user_input.replace(char, "")
# #     print(user_input)


# # removeOdd()

# # user_input = "adsdghgfjhgf"
# # result = []
# # for i in range(0, len(user_input), 2):
# #     result.append(user_input[i])
# # print("".join(result))

# # user_input = "This is a word and word"
# # user_list = user_input.split(" ")
# # uniq = set(user_list)
# # result = []
# # # print(user_list)
# # for i in uniq:
# #     count = user_list.count(i)
# #     result.append(count)
# # abc = dict(zip(uniq, result))
# # print(abc)

# # user_input = "Apple trees are large if grown from seed. Generally, apple cultivars are propagated by grafting onto rootstocks, which control the size of the resulting tree. There are more than 7,500 known cultivars of apples, resulting in a range of desired characteristics. Different cultivars are bred for various tastes and use, including cooking, eating raw and cider production. Trees and fruit are prone to a number of fungal, bacterial and pest problems, which can be controlled by a number of organic and non-organic means. In 2010, the fruit's genome was sequenced as part of research on disease control and selective breeding in apple production."
# # user_list = user_input.split(" ")
# # obj_words = {"this": 1, "is": 1, "word": 1}

# # for item in user_list:
# #     if item not in obj_words.keys():
# #         obj_words[item] = 1
# #     else:
# #         obj_words[item] += 1
# # print(obj_words)

# # user_input = input("give input:")
# # a = str.lower(user_input)
# # b = str.upper(user_input)
# # print(a, "    ", b)
# # a = []
# # print(type(a))

# # input = "red", "white", "black", "red", "green", "black"
# # input_list = list(set(list(input)))
# # input_list.sort()
# # print(input_list)

# # def add_tag(tag, string):
# #     result = "<%s>%s</%s>" % (tag, string, tag)
# #     return result

# # def add_tag(tag, string):
# #     result = f"<{tag}>{string}<{tag}/>"
# #     return result


# # print(add_tag("i", "Python"))
# # def add_mid(str1, str2):
# #     print(type(len(str1)/2))
# #     print(f"{str1[0:len(str1)//2]}{str2}{str1[len(str1)//2:len(str1)]}")


# # add_mid("{{}}", "Vivek")

# # user_input = input("enter string: ")
# # new_str = user_input[-2:]*4
# # print(new_str)
# # my_str = "Hello, I am Vivek And I am from Guwahati"
# # result = my_str.rsplit("a", 1)[0]
# # print(result)


# # string = input("enter str :")
# # if len(string) % 4 == 0:
# #     print(string[-1:0:-1]+string[0])
# # else:
# #     print(string)

# # string = input("Please neter a string: ")
# # first_four = string[0:4]
# # print(first_four)
# # count = 0
# # for char in first_four:
# #     if char.upper() == char:
# #         count += 1
# # if count >= 2:
# #     print(string.upper())
# # else:
# #     print(string)
# # string = input("Please neter a string: ")
# # str_list = []
# # for char in string:
# #     str_list.append(char)
# # str_list.sort()
# # result = "".join(str_list)
# # print(result)

# # alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnop"
# # ALPHA = alpha.upper()
# # inp = input("Please enter a string: ")
# # code = int(input("Please enter a number: "))
# # result = ""
# # for char in inp:
# #     if char in alpha:
# #         char = alpha[alpha.index(char) + code]
# #         result += char
# #     else:
# #         char = ALPHA[ALPHA.index(char) + code]
# #         result += char

# # print(result)

# # inp = input("Enter a string: ")
# # obb = inp.split()
# # result = {}
# # for i in obb:
# #     if i not in result.keys():
# #         result[i] = 1
# #     else:
# #         result[i] += 1

# # query_sub = input("please enter a substring: ")
# # print(result[query_sub])

# # strn = "jdfhksdfj"
# # print(strn[-1:0:-1] + strn[0])

# # strp = "aeiou"
# # strn = "Aman Regmi"

# # for item in strp:
# #     for char in strn:
# #         if char == item:
# #             strn = strn.replace(char, "")

# # print(strn)

# # inp = input("Enter a string: ")
# # result = {}
# # for i in inp:
# #     if i not in result.keys():
# #         result[i] = 1
# #     else:
# #         result[i] += 1
# # for key, value in result.items():
# #     if value != 1:
# #         print(key, "> ", value)

# # inp = input("Enter a string: ")
# # for i in inp:
# #     print(f"the index of {i} is {inp.index(i)}")

# # inp = input("Enter a string: ")
# # n = 5
# # print(inp[0:5].lower() + inp[5:])

# # inp = "55.66,33,.7.4,.5"
# # print(inp.index(",", 3))
# #inp2 = inp1.replace(".", ",")
# #  "skjdhsgkapgksjhgkisfhui"
# # vowels = "aeiou"
# # result = {}
# # inp = input("Please enter a string: ")
# # for char in inp:
# #     for vowel in vowels:
# #         if char == vowel:
# #             if char not in result.keys():
# #                 result[char] = 1
# #             else:
# #                 result[char] += 1
# # print(result)

# # dg = "a,s,d,f,g,h,j,k,l"
# # df = dg.split(",")
# # print(df[-2:])
# # jashdlfoewkhbjcak
# # inp = input("Please enter a string: ")
# # res = {}
# # for i in inp:
# #     if i not in res.keys():
# #         res[i] = 1
# #     else:
# #         res[i] += 1
# # for key, value in res.items():
# #     if value == 1:
# #         print(key, "> ", value)
# #         break
# # import random
# # inp = input("Please enter a string: ")
# # intt = int(inp("Please enter an integer: "))

# # inp2 = inp*intt
# # for i in range(Infi)


# # ind = float("inf")
# # print(random.randint(1, 3))

# import json
# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print("Original Python object:")
# print(python_obj)
# json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
# # print(json_obj)

# import json
# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print("Original Python object:")
# print(python_obj)
# json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
# print(json_obj)
# result = float("inf")

# listt = [1, 2, 5, 7, 66, -6, 9]
# for num in listt:
#     if num < result:
#         result = num
# print(result)
# count = 0
# listt = ['abc', 'xyz', 'aba', '1221', "keek"]
# for item in listt:
#     if len(item) > 2 and item[0] == item[-1]:
#         count += 1
# print(count)
# sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# def last(n): return n[-1]
# print(sorted(sample, key=last))

# word_list = ["sdfjvdf", 'aqsdhgvje', "wedfhgvj", "cbgwgwdjhqwd", "wqd", "WQd"]
# num = 4
# result = []
# for i in word_list:
#     if len(i) > num:
#         result.append(i)
# print(result)

# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(True)
s = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
s = s.remove(s[0])
s = s.remove(s[4])
s = s.remove(s[5])
print(s)
