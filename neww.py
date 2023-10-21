with open('dz.txt','r') as file:# получаем строку из текстового файла
    str_value = file.read()
def q_str(a,b=2):#функция изменяющая значение переменной str
    global str_value
    str_value *=a
q_str(3)#дублируем
print(str_value)

def dd(*args,**kwargs):
    return args, kwargs
print(1,2,3)
print(dd(d=1,n=2))