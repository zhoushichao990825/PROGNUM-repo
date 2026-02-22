D=float(input("enter the day"))
M=float(input("enter the month"))
Y=float(input("enter the year"))
Julian_Date=367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"The Julian date is:{Julian_Date}, years")