import pygame as pg
from .Button import Button
from .lambdaWrap import lambdaWrap
class Dropdown(Button):
    __slots__ = ['options','curOption','isExpanded']
    def __init__(self,surface:pg.Surface,posX:int=0,posY:int=0,width:int=100,height:int=50,textInput:str='text',textSize:int=30,color:pg.Color=pg.Color(50,50,50),**kwargs):
        self.options = []
        kwargs.setdefault('action', self.changeItemsVisibility)
        super().__init__(surface, posX, posY, width, height, textInput, textSize, color, **kwargs)

        count = 0
        names = kwargs.get('options')
        self.curOption=names[0]
        self.text.text=self.curOption
        for i in names:
            self.options.append(Button(surface, posX, posY + self.background.get_height() + 50 * count, self.background.get_width(), 50,i, isHidden=True,action=lambdaWrap(setattr,(self,'curOption',i))))

            count += 1
        self.isExpanded = False

    def changeItemsVisibility(self):
        for i in self.options:
            i.changeVisibility()

    def update(self,events:list[pg.event]):
        self.text.text=self.curOption
        super().update(events)

    def getOption(self):
        return self.curOption