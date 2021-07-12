import pygame, sys
from pygame.locals import *

class Gui:
    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption('Log In')
        
        self.mainClock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((500, 500), 0, 32) #Initialize a display surface
        
        self.font = pygame.font.SysFont('Times New Roman', 20)
        
        self.click = False
        
        self.user_text = ''
        
        self.username_active = False
        self.password_active = False
        self.famous_person_account_active = False
        
        self.user_text_username = ''
        self.user_text_password = ''
        self.user_text_famous_person_account = ''
    
    def draw_text(self, text, color, x, y):
            textobj = self.font.render(text, 2, color) # returns a new surface
            
            textrect = textobj.get_rect() #Returns a new rectangle covering the entire surface returned by the text
            textrect.topleft = (x, y) #moves the rectangle to the x,y coordinate
            
            self.screen.blit(textobj, textrect) #draws the source object to the rectangle
            
    def main_menu(self):
        white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
        text_surface1 = ''
        text_surface2 = ''
        text_surface3 = ''
        
        while True:
            self.screen.fill(white)
    
            mx, my = pygame.mouse.get_pos()
    
            username = pygame.Rect(40, 100, 100, 50)
            username_box = pygame.Rect(140, 100, 300, 49)
            password = pygame.Rect(40, 200, 100, 50)
            password_box = pygame.Rect(140, 200, 300, 49)
            famous_person_account = pygame.Rect(40, 300, 100, 50)
            famous_person_account_box = pygame.Rect(140, 300, 300, 49)
            log_in = pygame.Rect(100, 400, 300, 50)
            
            pygame.draw.rect(self.screen, red, username)
            pygame.draw.rect(self.screen, black, username_box, 2)
            pygame.draw.rect(self.screen, red, password)
            pygame.draw.rect(self.screen, black, password_box, 2)
            pygame.draw.rect(self.screen, red, famous_person_account)
            pygame.draw.rect(self.screen, black, famous_person_account_box, 2)
            pygame.draw.rect(self.screen, red, log_in)
            
            self.draw_text('Instagram Followers Bot', black, 40, 20)
            self.draw_text('By John Laidler', black, 40, 40)
            self.draw_text('Username', white, 40, 110)
            self.draw_text('Password', white, 40, 210)
            self.draw_text('Celebrity', white, 40, 305)
            self.draw_text('Username', white, 40, 325)
            self.draw_text('Log In', white, 215, 400)
                   
            click = pygame.mouse.get_pressed()[0]
                        
            if username_box.collidepoint((mx, my)):
                if click:
                    self.username_active = True
                    self.password_active, self.famous_person_account_active = False, False
            elif password_box.collidepoint((mx, my)):
                if click:
                     self.password_active = True
                     self.username_active, self.famous_person_account_active = False, False
            elif famous_person_account_box.collidepoint((mx, my)):
                if click:
                    self.famous_person_account_active = True
                    self.username_active, self.password_active = False, False
            elif log_in.collidepoint((mx, my)):
                if click:
                    return self.user_text_username, self.user_text_password, self.user_text_famous_person_account
            else:
                self.username_active = False
                self.password_active = False
                self.famous_person_account_active = False
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.username_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text_username = self.user_text_username[:-1] #Takes everything but the last character
                        else:
                            self.user_text_username += event.unicode
                        text_surface1 = self.font.render(self.user_text_username, True, black)
                    if self.password_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text_password = self.user_text_password[:-1] #Takes everything but the last character
                        else:
                            self.user_text_password += event.unicode
                        text_surface2 = self.font.render(self.user_text_password, True, black)
                    if self.famous_person_account_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text_famous_person_account = self.user_text_famous_person_account[:-1] #Takes everything but the last character
                        else:
                            self.user_text_famous_person_account += event.unicode
                        text_surface3 = self.font.render(self.user_text_famous_person_account, True, black)
                                   
            if text_surface1 != '':
                self.screen.blit(text_surface1, username_box)
            if text_surface2 != '':     
                self.screen.blit(text_surface2, password_box)
            if text_surface3 != '':      
                self.screen.blit(text_surface3, famous_person_account_box)
                    
            pygame.display.update()
            self.mainClock.tick(60)
            
                