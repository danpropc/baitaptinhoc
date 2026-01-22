#Bài 1:
#t,v,a = (float(x) for x in input("Hãy nhập điểm toán văn anh:").split())
#if 0<=t<=10 and 0<=v<=10 and 0<=a<=10:
#    if ((t+v+a)/3)>=8 and t>=8 and v>=8 and a>=6.5:
#        print("Bạn là học sinh giỏi!")
#    elif ((t+v+a)/3)>=6.5 and t>=6.5 and v>= 6.5 and a>=5:
#        print("Bạn là học sinh khá!")
#    elif ((t+v+a)/3)>=5 and t>=5 and v>=5 and a>=3.5:
#        print("Bạn là học sinh trung bình!")
#    elif ((t+v+a)/3)>=3.5 and t>=3.5 and v>= 3.5 and a>=2:
#        print("Bạn là học sinh yếu!")
#    else:
#        print("Bạn là học sinh yếu kém!!!")
#else:
#    print("Điểm không hợp lệ!")


#Bài 2:
#n = int(input())
#for i in range(1, n + 1):
#    print(2 * i, end=" ")
#print()
#for i in range(0, n + 1):
#    print(2 * i + 1, end=" ")


#Bài 3:
#tong=0;tich=1;tongmu=0;i=1;n=int(input())
#while i<=n:
#    tong+=i;tich*=i;tongmu+=i**2;i+=1
#print(tong,tich,tongmu)


#Bài 4:
#t,n=(int(x) for x in input().split());i=t
#while i<n:
#    i+=t;print(t,i,end=" ")


#Bài 5:
#n=int(input());tong=0
#while n>0:
#    tong+=n%10;n//=10  
#print(tong)