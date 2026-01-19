#Bài 1:
t,v,a = (float(x) for x in input("Hãy nhập điểm toán văn anh:").split())
if 0<=t<=10 and 0<=v<=10 and 0<=a<=10:
    if ((t+v+a)/3)>=8 and t>=8 and v>=8 and t>=6.5 and v>=6.5 and a>=6.5:
        print("Bạn là học sinh giỏi:")
    elif ((t+v+a)/3)>=6.5 and t>=6.5 and v>= 6.5 and 

else:
    print("Điểm không hợp lệ!")