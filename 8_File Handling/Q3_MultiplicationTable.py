# WAP to generate multiplication tables of 2 to 20 in different files and place them in 
# a single folder 

for i in range(2,21):
    with open(f'Tables/{i}.txt','w') as m:
        for j in range(1,11):
            m.writelines(f'{i}*{j}={i*j}\n')
    