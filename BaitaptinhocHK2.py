#Bài 1: xếp loại học sinh
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


#Bài 2: In 2 dãy số chẵn và lẻ, chẵn từ 1 đến 2n, lẻ từ 1 đến 2n+1
#n = int(input())
#for i in range(1, n + 1):
#    print(2 * i, end=" ")
#print()
#for i in range(0, n + 1):
#    print(2 * i + 1, end=" ")


#Bài 3: cho n, tính tổng các số nguyên từ 1 đến n, tính tích các số nguyên từ 1 đến n, tính tổng các bình phương các số từ 1 đến n
#tong=0;tich=1;tongmu=0;i=1;n=int(input())
#if n in range(1,21):
#    while i<=n:
#        tong+=i;tich*=i;tongmu+=i**2;i+=1
#    print(tong,tich,tongmu)
#else:
#    print("n không hợp lệ")


#Bài 4: In ra dãy số là bội của t nhỏ hơn n
#t,n=(int(x) for x in input().split());i=t
#if t<=n:
#    while i<=n:
#        print(i,end=" ");i+=t
#else:
#    print("Không có bội nào của t nhỏ hơn n")


#Bài 5: tính tổng các chữ số trong 1 số n bất kì
#n=int(input());tong=0
#while n>0:
#    tong+=n%10;n//=10  
#print(tong)

# Cấu trúc rẽ nhánh:
# Nhập 3 số a,b,c. Sắp xếp 3 số a,b,c theo thứ tự tăng dần rồi in ra lại
# a, b, c = (float(x) for x in input().split())
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a, b, c)

# Giải và biện luận phương trình ax + b =0
# a, b = (float(x) for x in input().split())
# if a == 0:
#     if b == 0:
#         print("Phuong trinh vo so nghiem")
#     else:
#         print("Phuong trinh vo nghiem")
# else:
#     x = -b / a
#     print("Phuong trinh co nghiem:", x)

# Giải và biện luận pt ax^2 + bx + c = 0
# a, b, c = (float(x) for x in input().split())
# if a == 0:
#     if b == 0:
#         if c == 0:
#             print("Phuong trinh vo so nghiem")
#         else:
#             print("Phuong trinh vo nghiem")
#     else:
#         x = -c / b
#         print("Phuong trinh co 1 nghiem:", x)
# else:
#     delta = b*b - 4*a*c
#     if delta < 0:
#         print("Phuong trinh vo nghiem")
#     elif delta == 0:
#         x = -b / (2*a)
#         print("Phuong trinh co nghiem kep:", x)
#     else:
#         x1 = (-b + delta**0.5) / (2*a)
#         x2 = (-b - delta**0.5) / (2*a)
#         print("Phuong trinh co 2 nghiem phan biet:", x1, x2)

# Cho 3 số thực a,b,c dương. Kiểm tra xem a,b,c có cấu thành tam giác được không?Tam giác gì?(đều,cân, vuông, vuông cân, thường)
# a, b, c = (float(x) for x in input().split())
# if a + b <= c or a + c <= b or b + c <= a:
#     print("Khong phai tam giac")
# else:
#     if a == b and b == c:
#         print("Tam giac deu")
#     elif (a == b and a*a + b*b == c*c) or \
#          (a == c and a*a + c*c == b*b) or \
#          (b == c and b*b + c*c == a*a):
#         print("Tam giac vuong can")
#     elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#         print("Tam giac vuong")
#     elif a == b or a == c or b == c:
#         print("Tam giac can")
#     else:
#         print("Tam giac thuong")

# Nhập tháng, năm, tính số ngày của tháng đó
# thang, nam = (int(x) for x in input().split())
# if thang < 1 or thang > 12:
#     print("Thang khong hop le")
# else:
#     if thang == 2:
#         if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
#             print(29)
#         else:
#             print(28)
#     elif thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
#         print(31)
#     else:
#         print(30)