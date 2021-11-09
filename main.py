def div(num1,num2):
  sum=num1/num2
  return sum
def mult(num1,num2):
  sum=num1*num2
  return sum
def add(num1,num2):
  sum=num1+num2
  return sum
def sub(num1,num2):
  sum=num1-num2
  return sum
def exp(num1,num2):
  og_num1=num1
  for i in range (num2-1):
    num1=num1*og_num1
  sum=num1
  return sum
process=0
con=""
save_value=""
value=list()
while con!="n":
  while process!="x" and process!="/" and process!="-" and process!="+" and process!="^":
    process= input("would you like to x,/,-,+,^\n>")
  numbers=input("give me two numbers\n if you would like to call on a saved value use this format\n value 'the round in which you saved the number'\n>")
  seperate=numbers.split()

  if len(seperate)==3:
    num=int(seperate[2])-1
    seperate.insert(1,value[num])
    seperate.remove(seperate[2])
  if process=="/":
    result1=div(int(seperate[0]),int(seperate[1]))
    save_value=result1
    print(result1)
  if process=="x":
    result2=mult(int(seperate[0]),int(seperate[1]))
    save_value=result2
    print(result2)
  if process=="+":
    result3=add(int(seperate[0]),int(seperate[1]))
    save_value=result3
    print(result3)
  if process=="-":
    result4=sub(int(seperate[0]),int(seperate[1]))
    save_value=result4
    print(result4)
  if process=="^":
    result5=exp(int(seperate[0]),int(seperate[1]))
    save_value=result5
    print(result5)
  save=input("would you like to save your value(y/n)\n>")
  if save=="y":
    value.append(save_value)
  con=input("would you like to continue(y/n)\n>")
