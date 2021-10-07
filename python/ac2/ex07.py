def f():
   global z
   z = 100
   print('z is: ', z)
   z=50
   print('new value of global z is: ', z)

f()

print('Value of z is: ', z)