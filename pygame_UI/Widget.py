import pygame as pg


class Text():
    freeInstances=[]
    __slots__ = ['surface','text','size','pos']
    def __init__(self,surface:pg.Surface,text:str='text',size:int=50,**kwargs):
        self.surface=surface
        self.text=text
        self.size=size
        self.pos=kwargs.get('pos',(self.surface.get_width()//2,self.surface.get_height()//2))
        if kwargs.get('isIndependent',True):
            Text.freeInstances.append(self)

    def draw(self):
        render=pg.font.Font(None,self.size).render(self.text,1,pg.Color(220,220,220))
        render.set_alpha(Widget.alpha)
        self.surface.blit(render,render.get_rect(center=self.pos))

    def setText(text:str):
        self.text=text

    @staticmethod
    def update():
        for i in Text.freeInstances:
            i.draw()

class Widget():
    alpha=150
    widgets=[]
    __slots__ = ['posX','posY','surface','color','text','background','isHidden']
    def __init__(self,surface:pg.Surface,posX:int=0,posY:int=0,width:int=100,height:int=50,textInput:str='text',textSize:int=30,color:pg.Color=pg.Color(50,50,50),**kwargs):
        Widget.widgets.append(self)
        self.posX=posX
        self.posY=posY
        self.surface=surface
        self.color=color
        self.background=pg.Surface((width,height))
        self.background.set_alpha(Widget.alpha)
        self.background.fill(color)
        self.isHidden=kwargs.get('isHidden',False)
        self.text: Text = Text(self.background,textInput, textSize,isIndependent=False)

    @staticmethod
    def updateWidgets(events:list[pg.event]):
        for widget in Widget.widgets:
            if not(widget.isHidden):
                widget.update(events)

    def update(self,events:list[pg.event]):
        if not(self.isHidden):
            self.text.draw()
            self.background.set_alpha(Widget.alpha)

            self.surface.blit(self.background, (self.posX, self.posY))

    def changeVisibility(self):
        self.isHidden=not(self.isHidden)
