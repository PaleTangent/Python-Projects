while True:
    try:
        temp = input('BYTE YOUR TEMP(F OR C)')
        temp_pattern = temp[-1]
        temp_value = float(temp[0:-1])
        if temp_pattern in ['F', 'f']:
            temp_out = ((temp_value - 32) / 1.8)
            print(temp_out)
        elif temp_value in ['C', 'c']:
            # 摄氏度转华氏度，暂无法计算
            # temp_out = ？？？
            # print(temp_out)
            print("Sorry,I can't do it")
            pass
        elif temp_pattern == 'q':
            print('\n用户已通过指令结束程序.')
            break
        else:
            print('error')
    except KeyboardInterrupt:
        print('\n用户已通过快捷键结束程序.')
        break
    except ValueError:
        print('ValueError')
    except Exception as e:
        print('未知错误', e)
