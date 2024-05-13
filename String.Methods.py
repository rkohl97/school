#course = 'Python for Beginners'
#print(course.upper())
#print(course.lower())
#print(course.find('B'))


import qrcode
from PIL import Image

data = 'https://www.youtube.com/watch?v=OXRWQefGh1U'
img = qrcode.make(data)
img.save('qrcode1.png')


DOB = (input('Your Birth year '))
print(type(DOB))



