a=['疑恍酒美','炉寒温时','炉寒酒美','写懒炉寒','村前花墨','温时温时','疑恍村前','村前看醉','花墨温时','看醉温时','看醉白月','看醉村前','村前花墨','看醉酒美','看醉酒美','花墨诗新','花墨看醉','看醉诗新','看醉花墨','温时村前','村前看醉','看醉花墨','花墨花墨','看醉酒美','看醉村前','酒美花墨','村前看醉','看醉温时','花墨写懒','花墨村前']

enc=''
for i in a:
    enc+=i[::-1]
print(enc)

table="冻笔新诗懒写寒炉美酒时温醉看墨花月白恍疑雪满前村"
index=0
idx_list=[]
while index<=len(enc):
    temp=enc[index:index+2]
    #temp=temp[::-1]
    idx=table.find(temp)//2
    idx_list.append(idx)
    index+=2

char_list=[]
index=0
while index<len(idx_list):
    if idx_list[index]==11:
        char_list.append(chr(61+idx_list[index+1]))
        index+=2
    else:
        char_list.append(chr(idx_list[index]+ord('0')))
        index+=1

flag=''
for i in char_list:
    flag+=i
print(flag)
