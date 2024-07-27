import pygame as pg
from .Widget import Widget
class Button(Widget):
    __slots__ = ['action','hoverColor','clickColor']
    def __init__(self,surface:pg.Surface,posX:int=0,posY:int=0,width:int=100,height:int=50,textInput:str='text',textSize:int=30,color:pg.Color=pg.Color(50,50,50),**kwargs):
        super().__init__(surface,posX,posY,width,height,textInput,textSize,color,**kwargs)
        self.action=kwargs.get('action',lambda :print('button click '+'"'+textInput+'"'))
        self.hoverColor=kwargs.get('hoverColor',pg.Color(200,200,200))
        self.clickColor=kwargs.get('clickColor',pg.Color(150,150,150))

    def update(self,events:list[pg.event]):
        isPointed=pg.mouse.get_pos()[0] in range(self.posX,self.posX+self.background.get_width()) and pg.mouse.get_pos()[1] in range(self.posY,self.posY+self.background.get_height())
        if isPointed:
            self.background.fill(self.hoverColor)
        else:
            self.background.fill(self.color)
        if pg.mouse.get_pressed()[0] and isPointed:
            self.background.fill(self.clickColor)

        for event in events:
            if event.type==pg.MOUSEBUTTONDOWN and isPointed:
                self.action()
        super().update(events)