# input from user in degree celious and convert into fernhit
fh = open('pactical1.txt','w')
c= int(input('enter a cal value: '))
f=9*c/5 + 33
F= int(input('enter a fer value: '))
c=(F - 32) * 5 / 9
fh.write(str(f))
fh.write('\n')
fh.write(str(c))