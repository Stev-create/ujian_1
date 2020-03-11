# No 1

# def Hashtag(string):
#     z = '#'
#     s = string.split()

#     for i in s:
#         z += i.capitalize()

#     if(len(z)>140 or z == '#'):
#         print('False')
    
#     else:
#         print(z)

# Hashtag(" Hello there how are you doing")
# Hashtag('Hello    World')
# Hashtag('')

# No. 2

# def create_phone_number(number):

#     if(len(number)==10):
#         print('({}{}{}) {}{}{}-{}{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]))
#     else: 
#         print('Invalid input. Mohon masukkan 10 digit angka.')

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# create_phone_number([2,3,4])



# No. 3

# def sort_odd_even(num):

#     iganjil = []
#     nganjil = []
#     igenap = []
#     ngenap = []

#     for i,n in enumerate(num):
#         if (n%2==0):
#             igenap.append(i)
#             ngenap.append(n)
#         else:
#             iganjil.append(i)
#             nganjil.append(n)

#     p = 0

#     while(p==0):
    
#         p = 1
        
#         for i in range(len(ngenap)-1):
#             if(ngenap[i]<ngenap[i+1]):
#                 ngenap[i],ngenap[i+1] = ngenap[i+1],ngenap[i]
#                 p = 0
        
#         for i in range(len(nganjil)-1):
#             if(nganjil[i]>nganjil[i+1]):
#                 nganjil[i],nganjil[i+1] = nganjil[i+1],nganjil[i]
#                 p = 0

#     h = []

#     for i in range(len(num)):
#         h.append('x')

#     for o,m in zip(iganjil,nganjil):
#         h[o] = m
    
#     for o,m in zip(igenap,ngenap):
#         h[o] = m

#     print(h)


# sort_odd_even([5, 3, 2, 8, 1, 4])
# sort_odd_even([3,2,1,4])

# No. 4 

# def hollowTriangle(height):
#     z = ''

#     for i in range(1,height):
        
#         for j in range(i,height):
#             z += '_'

#         for j in range(2*i-1):
#             if(j==0 or j==2*i-2):
#                 z += '#'
#             else:
#                 z += '_'

#         for j in range(i,height):
#             z += '_'

        

#         z += '\n'

    
#     for j in range(2*height-1):
#         z += '#'
    
#     print(z)

# hollowTriangle(2)
# hollowTriangle(5)




