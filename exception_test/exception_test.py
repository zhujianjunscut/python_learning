try:
    x = 1
    y = 0
    x/y
except (ZeroDivisionError,TypeError) as e:
    print("y must not set zero",e)


try:
    x = 3;
    y = 0;
    x/y
except:
    print("""xxxx""")
finally:
    print("errno has not handle")