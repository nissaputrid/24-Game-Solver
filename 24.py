import time

def num_p(num):
    if len(num)<2: yield num
    else:
        tList = []
        for x in num:
            tList.append(x)
            if x in tList[:-1]: continue
            temp = num[:]; temp.remove(x)
            for y in num_p(temp):
                yield [x]+y

def c_op():
    temp1, temp2, temp3 = [], [], []
    operator = ['+', '*', '/', '-']
    inp = []

    for x in operator:
        temp1.append(x)
        for y in operator:
            temp2 = temp1
            temp2.append(y)
            for z in operator:
                temp3 = temp2
                temp3.append(z)
                inp = inp + temp3
                if len(inp) != 3:
                    del inp[0:3]
                yield inp
                temp3.pop()
            temp2.pop()
        temp1.pop()

start = time.time()
print("Selamat Datang di 24 Game Solver!")
print("Masukkan input 4 buah angka. (Pisahkan dengan spasi)")
a, b, c, d = input(">> ").split(" ")
r_num = num_p([a,b,c,d])
sol = 0
hsl = 24

for i in list(r_num):
    r_op = c_op()
    for j in list(r_op):
        #CASE 1
        try:
            temp = "((" + i[0] + j[0] + i[1] + ")" + j[1] + i[2] + ")" + j[2] + i[3]
            if eval(temp) == hsl:
                sol = sol+1
                print(temp)
        except:
            hsl = 24
        
        #CASE 2
        try:
            temp = "(" + i[0] + j[0] + i[1] + ")" + j[1] + "(" + i[2] + j[2] + i[3] + ")"
            if eval(temp) == hsl:
                sol = sol+1
                print(temp)
        except:
            hsl = 24
        
        #CASE 3
        try:
            temp = "(" + i[0] + j[0] + "(" + i[1] + j[1] + i[2] + "))" + j[2] + i[3]
            if eval(temp) == hsl:
                sol = sol+1
                print(temp)
        except:
            hsl = 24
        
        #CASE 4
        try:
            temp = i[0] + j[0] + "((" + i[1] + j[1] + i[2] + ")" + j[2] + i[3] + ")"
            if eval(temp) == hsl:
                sol = sol+1
                print(i[0] + j[0] + "((" + i[1] + j[1] + i[2] + ")" + j[2] + i[3] + ")")
        except:
            hsl = 24
if sol == 0:
    print("Tidak ada solusi.")
else:
    print("Terdapat %d solusi." %sol)  
end = time.time()
execution_time = end-start
print("Waktu eksekusi program adalah %d detik." %execution_time)