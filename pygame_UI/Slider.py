import pygame as pg
from .Widget import Widget
class Slider(Widget):
    __slots__ = ['onDrag','isVertical','value','minValue','maxValue','handleColor','isMousePressed','handle','handlePos']
    def __init__(self,surface:pg.Surface,posX:int=0,posY:int=0,width:int=200,height:int=30,textInput:str='',textSize:int=30,color:pg.Color=pg.Color(50,50,50),**kwargs):
        super().__init__(surface,posX,posY,width,height,textInput,textSize,color,**kwargs)
        self.onDrag=kwargs.get('onDrag',lambda x:print(x))
        self.isVertical=kwargs.get('isVertical',False)
        self.value=0
        self.minValue=kwargs.get('minValue',0)
        self.maxValue=kwargs.get('maxValue',100)
        self.handleColor=kwargs.get('handleColor',pg.Color(250,250,250))
        self.isMousePressed=False

        if self.isVertical:
            self.handle = pg.Surface((width*2, height//25))
        else:
            self.handle=pg.Surface((width//25,height*2))
        self.handle.set_alpha(Widget.alpha)
        self.handle.fill(self.handleColor)

        if self.isVertical:
            self.handlePos=posY+self.background.get_height()//2
        else:
            self.handlePos = posX + self.background.get_width() // 2


    def update(self,events:list[pg.event]):
        for event in events:
            if event.type==pg.MOUSEBUTTONDOWN and pg.mouse.get_pos()[0] in range(self.posX,self.background.get_width()+self.posX) and pg.mouse.get_pos()[1] in range(self.posY,self.background.get_height()+self.posY):
                self.isMousePressed=True
            if event.type==pg.MOUSEBUTTONUP:
                self.isMousePressed=False
        super().update(events)
        if self.isMousePressed:
            if self.isVertical:
                if pg.mouse.get_pos()[1] in range(self.posY, self.posY + self.background.get_height()):
                    self.handlePos=pg.mouse.get_pos()[1]
                elif pg.mouse.get_pos()[1]<self.posY:
                    self.handlePos=self.posY
                else:
                    self.handlePos=self.posY+self.background.get_height()

                self.value=self.maxValue-((pg.mouse.get_pos()[1]-self.posY)/self.background.get_height())*self.maxValue

            else:
                if pg.mouse.get_pos()[0] in range(self.posX,self.posX+self.background.get_width()):
                    self.handlePos = pg.mouse.get_pos()[0]
                elif pg.mouse.get_pos()[0]<self.posX:
                    self.handlePos=self.posX
                else:
                    self.handlePos=self.posX+self.background.get_width()

                self.value = ((pg.mouse.get_pos()[0] - self.posX) / self.background.get_width()) * self.maxValue
            self.onDrag(self.value)
        if self.isVertical:
            self.surface.blit(self.handle, self.handle.get_rect(center=(self.background.get_width() // 2 + self.posX, self.handlePos)))
        else:
            self.surface.blit(self.handle, self.handle.get_rect(center=(self.handlePos, self.background.get_height() // 2 + self.posY)))