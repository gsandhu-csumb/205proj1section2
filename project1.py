from PIL import Image 

pic1 = Image.open('1.png') #Import each Image 
pic2 = Image.open('2.png')
pic3 = Image.open('3.png')
pic4 = Image.open('4.png')
pic5 = Image.open('5.png')
pic6 = Image.open('6.png')
pic7 = Image.open('7.png')
pic8 = Image.open('8.png')
pic9 = Image.open('9.png')

imagergb1 = pic1.convert('RGB') #Convert each image to RGB
imagergb2 = pic2.convert('RGB')
imagergb3 = pic3.convert('RGB')
imagergb4 = pic4.convert('RGB')
imagergb5 = pic5.convert('RGB')
imagergb6 = pic6.convert('RGB')
imagergb7 = pic7.convert('RGB')
imagergb8 = pic8.convert('RGB')
imagergb9 = pic9.convert('RGB')

width, height = 495, 557 #Input Height of the images
imagergb = [] #Empty list to compile new pixels
for y in range(height): #For loop to compile new pixels of width
    for x in range(width): #For loop to compile new pixels of height
        R = [] #Empty list for Red 
        G = [] #Empty list for Green
        B = [] #Empty list for Blue
        
        red_1, green_1, blue_1 = imagergb1.getpixel((x,y))
        R.append(red_1)
        G.append(green_1)
        B.append(blue_1)
        
        red_2, green_2, blue_2 = imagergb2.getpixel((x,y))
        R.append(red_2)
        G.append(green_2)
        B.append(blue_2)
        
        red_3, green_3, blue_3 = imagergb3.getpixel((x,y))
        R.append(red_3)
        G.append(green_3)
        B.append(blue_3)
        
        red_4, green_4, blue_4 = imagergb4.getpixel((x,y))
        R.append(red_4)
        G.append(green_4)
        B.append(blue_4)
        
        red_5, green_5, blue_5 = imagergb5.getpixel((x,y))
        R.append(red_5)
        G.append(green_5)
        B.append(blue_5)
        
        red_6, green_6, blue_6 = imagergb6.getpixel((x,y))
        R.append(red_6)
        G.append(green_6)
        B.append(blue_6)
        
        red_7, green_7, blue_7 = imagergb7.getpixel((x,y))
        R.append(red_7)
        G.append(green_7)
        B.append(blue_7)
        
        red_8, green_8, blue_8 = imagergb8.getpixel((x,y))
        R.append(red_8)
        G.append(green_8)
        B.append(blue_8)
        
        red_9, green_9, blue_9 = imagergb9.getpixel((x,y))
        R.append(red_9)
        G.append(green_9)
        B.append(blue_9)
        
        red = sorted(R)
        green = sorted(G)
        blue = sorted(B)
        imagergb.append((red[len(red)/2],green[len(green)/2],blue[len(blue)/2]))
    complete = Image.new("RGB", (width,height))
    complete.putdata(imagergb)
    complete.save("FinishedImage.png")

