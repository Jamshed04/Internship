f_num = int(input())
s_num = int(input())
t_num = int(input())

if f_num >= s_num and s_num >= t_num:
    print("Largest number:", f_num)
    print("numbers in descending order:", f_num, s_num, t_num)
elif f_num >= t_num and t_num >= s_num:
    print("Largest number:", f_num)
    print("numbers in descending order:", f_num, t_num, s_num)
elif s_num >= f_num and f_num >= t_num:
    print("Largest number:", s_num)
    print("numbers in descending order:", s_num, f_num, t_num)
elif s_num >= t_num and t_num >= f_num:
    print("Largest number:", s_num)
    print("numbers in descending order:", s_num, t_num, f_num)
elif t_num >= f_num and f_num >= s_num:
    print("Largest number:", t_num)
    print("numbers in descending order:", t_num, f_num, s_num)
elif t_num >= s_num and s_num >= f_num:
    print("Largest number:", t_num)
    print("numbers in descending order:", t_num, s_num, f_num)
