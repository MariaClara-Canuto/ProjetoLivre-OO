import pygame

taskColor = (54, 27, 15)
taskColorDark = (43, 22, 12)

colorText = (211, 219, 224)

class BasicTask():
    def __init__(self, place, y_coord, name, value, speed):
        self.place = place
        self.y_coord = y_coord
        self.name = name
        self.value = value
        self.speed = speed

    def icon(self):
        Iconbutton = pygame.draw.circle(self.place, taskColor, (390, self.y_coord), 30)
        return Iconbutton

    def box(self, font, leng, draw, point):
        pygame.draw.rect(self.place, taskColor, [435, self.y_coord - 30, 200, 60])

        text = font.render(self.name, True, colorText)  
        self.place.blit(text, (450, self.y_coord - 8))

        pygame.draw.rect(self.place, taskColorDark, [585, self.y_coord - 30, 50, 60])
        valueDisplay = font.render("+" + str(self.value), True, colorText)
        self.place.blit(valueDisplay, (600, self.y_coord - 8, 50, 60))

        coinName = font.render("Rbs.", True, colorText)
        self.place.blit(coinName, (592.5, self.y_coord + 14, 50, 60))

        pygame.draw.rect(self.place, taskColorDark, [435, self.y_coord + 16, 150, 14])

        if draw and leng < 150:
            leng += self.speed

        elif leng >= 150:
            draw = False
            leng = 0
            point += self.value

        pygame.draw.rect(self.place, (66, 158, 62), [435, self.y_coord + 16, leng, 14])

        return leng, draw, point

class Helper(BasicTask):
    def __init__(self, place, x_coord):
        super().__init__(place, None, None, None, None)
        self.x_coord = x_coord


    def iconHelp(self, font, name):
        helpButton = pygame.draw.circle(self.place, taskColor, (self.x_coord, 670), 30)
        setname = font.render(name, True, colorText)
        self.place.blit(setname, (self.x_coord - 30, 620))

        return helpButton

    def workHelp(self, font, points, cost, check, owned):
        colorPrice = (201, 26, 38)

        if points >= cost and not owned:
            colorPrice = (96, 173, 36)
            check = True

        if owned:
            sold = font.render('Vendido!', True, colorPrice)
            self.place.blit(sold, (self.x_coord - 30, 710))
            
        else:
            price = font.render(str(cost) + 'Rbs.', True, colorPrice)
            self.place.blit(price, (self.x_coord - 30, 710))

        return points, cost, check, owned

class unlockText():
    def __init__(self, place, var):
        self.place = place
        self.var = var

    def Writetext(self, text_str, font, x, y, condition, value1, value2):
        text = font.render(text_str, True, colorText)

        if condition != True:
            if value1 >= self.var:
                self.place.blit(text, (x, y))
        else:
            if value1 < self.var and self.var < value2:
                self.place.blit(text, (x, y))