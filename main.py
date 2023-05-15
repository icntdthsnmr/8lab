from PIL import Image, ImageFont, ImageDraw

def z1():
    f = "dr.jpg"

    with Image.open(f) as img:
        img.load()

    img.show()
    obrez_img = img.crop((220, 50, 480, 220))
    obrez_img.show()

    obrez_img.save("otred_dr.jpg")

def z2():
    lib = {1: "dr.jpg", 2: "masl.jpg", 3: "8marta.jpg", 4: "ng.jpg"}

    print("1 - День Рождения,", "2 - Масленица,", "3 - 8 марта,", "4 - Новый год,", end='\n')
    quest = int(input("Какую открытку вы хотите получить?: "))

    f = lib[quest]
    with Image.open(f) as img:
        img.load()
    img.show()

def z3():
    name = input("Введите имя получателя: ")
    f = "dr.jpg"

    with Image.open(f) as img:
        img.load()

    font = ImageFont.truetype("MultiroundPro.otf", 18)
    write_name = ImageDraw.Draw(img)

    write_name.text((img.width // 2 - 50, img.height - 30), name + ", поздравляю!", fill = ('red'), font = font, stroke_width = 1)

    img.show()
    img.save("dr_named.png")

