# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:54:25 2019

@author: Salim
"""
import pygame
import random
import time
pygame.init()

ekran_gen=500
ekran_yük=500

renk=(0,0,0)
ekran=pygame.display.set_mode((ekran_gen,ekran_yük))
pygame.display.set_caption("İlk oyunumuz")
saat=pygame.time.Clock()
   
class Kare():
    def __init__(self,x_kord,y_kord):
        self.x_kord=x_kord
        self.y_kord=y_kord
        self.gen=100
        self.yük=25
    def çiz(self):
        pygame.draw.rect(ekran,renk,[self.x_kord,self.y_kord,self.gen,self.yük])

class Daire():
    def __init__(self):
        self.x_kord=150 #random.randint(0,500)
        self.y_kord=50
        self.r=15
    def çiz(self):
        pygame.draw.circle(ekran,renk,(self.x_kord,self.y_kord),self.r)


def yazı_objesi(mesaj,font):
    yazı=font.render(mesaj,True,renk)
    return yazı,yazı.get_rect()
def Yanma(mesaj):
    font=pygame.font.Font("freesansbold.ttf",100)
    yazı,yazı_karesi=yazı_objesi(mesaj,font)
    yazı_karesi.center=(ekran_gen/2,ekran_yük/2)
    ekran.blit(yazı,yazı_karesi)
    pygame.display.update()
    time.sleep(1)
    Oyun()
    
renk2=(100,100,100)
def Giriş_Ekranı():
    ekran.fill((255,255,255))    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        
        font=pygame.font.Font("freesansbold.ttf",100)
        yazı,yazı_karesi=yazı_objesi("MERHABA",font)
        yazı_karesi.center=(ekran_gen/2,ekran_yük/3)
        ekran.blit(yazı,yazı_karesi)
        
        Button("Oyna",200,300,50,30,(255,255,0),"giriş")
        Button("Çıkış",200,400,50,30,(255,255,0),"cıkış")

        pygame.display.update()
        
def Button(yazı,x_kor,y_kor,gen,yük,renk,olay=None):
    fare=pygame.mouse.get_pos()
    tıkla=pygame.mouse.get_pressed()
    pygame.draw.rect(ekran,renk,[x_kor,y_kor,gen,yük])
    if fare[0]>x_kor and fare[0]<x_kor+gen and fare[1]>y_kor and fare[1]<y_kor+yük:
        pygame.draw.rect(ekran,(0,255,0),[x_kor,y_kor,gen,yük])
        if olay!=None and tıkla[0]==1:
            if olay=="giriş":
                Oyun()
            if olay=="cıkış":
                pygame.quit()
    font=pygame.font.Font("freesansbold.ttf",15)
    yazı,yazı_karesi=yazı_objesi(yazı,font)
    yazı_karesi.center=(x_kor+gen/2,y_kor+yük/2)
    ekran.blit(yazı,yazı_karesi)
            
def Skor(skor):
    font=pygame.font.SysFont(None,20)
    yazı=font.render("Skor ::"+str(skor),True,(0,0,0))   
    ekran.blit(yazı,(0,0))     
                  
def Oyun():
    kare=Kare(ekran_gen/2,ekran_yük-50)
    kare2=Kare(50,25)
    daire=Daire()
    hız=0
    skor=0
    yerx=10
    yery=10
    while True:
        
        ekran.fill((120,33,230))
        kare.çiz()
        kare2.çiz()
        daire.çiz()
        daire.y_kord+=yery
        daire.x_kord+=yerx
        if daire.x_kord+daire.r>=ekran_gen:
            yerx=yerx*(-1)
        if daire.x_kord<=0:
            yerx=yerx*(-1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    hız-=10
                if event.key==pygame.K_RIGHT:
                    hız+=10
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    hız=0
        if daire.x_kord>kare.x_kord and daire.x_kord<kare.x_kord+kare.gen and daire.y_kord>kare.y_kord:
            yery=yery*(-1)
            
        if kare.x_kord<=0:
            kare.x_kord=0
        if kare.x_kord+kare.gen>=ekran_gen:
            kare.x_kord=ekran_gen-kare.gen
        kare2.x_kord=daire.x_kord-kare2.gen/2
        
        if daire.x_kord>kare2.x_kord and daire.x_kord<kare2.x_kord+kare2.gen and daire.y_kord>kare2.y_kord and daire.y_kord<kare2.y_kord+kare2.yük:
            yery*=-1
            skor+=10
        
        if daire.y_kord>=ekran_yük:
            Yanma("Yandınız")
            
    
        
        
        kare.x_kord+=hız
        Skor(skor)
            
        pygame.display.update()
        saat.tick(60)

Giriş_Ekranı()


    
    




  
    


