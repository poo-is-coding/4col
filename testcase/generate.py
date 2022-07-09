""" 
fi =  open("testcase3_present.txt",'w')
num = 0
while num<59*59:
    if not num%59 and num!=0:fi.write("\n")
    fi.write(str(int(1e9+num))+" ")
    num+=1
fi.close()

 """

""" fi =  open("testcase_violent2.txt",'w')
for i in range(58):
    for j in range(59):
        if j%2:
            fi.write(str(int(1e9+i*j)))
        else:
            fi.write(str(int(1e9+1)))
        fi.write(" ")
    fi.write("\n")
for i in range(59):
    fi.write(str(int(1e9+1))+" ")
fi.close() """

""" fi =  open("testcase_violent3.txt",'w')
num = 0
while num<59*59:
    if not num:
        fi.write(str(0)+" ")
        num+=1
        continue
    if not num%59 and num!=0:fi.write("\n")
    fi.write(str(1)+" ")
    num+=1
fi.close() """

#K-regular
k = 99 #modify the value of k to generate a testcase that is a k-regular graph 

arr = [[i//2 for j in range(2*k-3)]for i in range(2,2*k-1)]
ind = 1
while ind < 2*k-3:
    num = 1
    for i in range(2*k-3):
        arr[ind][i] = num
        num += 1
        num %= k+1
        if not num:num+=1
    ind += 2
#print(arr)
fi =  open("testcase_333.txt",'w')
for i in arr:
    for j in i:
        if len(str(j))==1:
            fi.write(str(j)+" ")
        else:
            fi.write(str(j))
    fi.write("\n")
fi.close()


