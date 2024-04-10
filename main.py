try:
    user_num = int(input())
    div_num = int(input())
    print(user_num // div_num)
except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')
except ValueError as excpt:
    print('Input Exception: '+str(excpt))