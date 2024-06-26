from ..core.element import Element
print("Imported: details")

class details(Element):
    def __init__(self,value:str = None, id:str = None, open:bool = False):
        super().__init__(value=value, id = id)
        self.tag = "details"
        if open is not None:
            self.attrs["open"] = open
        
        

title = "Details"

description = '''
## details(value,id = None)

1. Details elementi. Bilgilerin yalnızca widget "açık" duruma getirildiğinde görülebildiği bir açıklama widget'ı oluşturur.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Details elementinin id'si                         |
| value         | Details elementinin başlığı                       |
| open          | Details elementinin açık olup olmadığı            |

'''

sample = """

def details_example():
    with details(open=True) as details_example:
        text("Details Content")
    return details_example

"""