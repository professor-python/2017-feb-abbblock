
# нужно сделать класс, который отображает тэг

# SomeClass("tag", 'some text')
# s.execute() # часто метод "работы" так называется

# <tag>some text</tag>


class MyTag:

    def __init__(self, tag_name, tag_text):
        self.tag_name = tag_name
        self.tag_text = tag_text

    def execute(self):
        return '<{tag_name}>{tag_text}</{tag_name}>'.format(
            tag_name=self.tag_name, tag_text=self.tag_text)

# Сделайте 3 класса: H1Tag, BTag и SpanTag
# ( про наследование )

# "<h1>big text</h1>"
# "<b>bold text</b>"
# "<span>local tuned text</span>"

class H1Tag(MyTag):

    def __init__(self, tag_text):
        super().__init__('h1', tag_text)

class BTag(MyTag):

    def __init__(self, tag_text):
        super().__init__('b', tag_text)

class SpanTag(MyTag):

    def __init__(self, tag_text):
        super().__init__('span', tag_text)
    


if __name__=='__main__':

    # tag = MyTag('b', 'test text')
    # print(tag.execute())

    # Напишите строчку пример с помощью этих классов:
    # <h1>Hello from <span>text</span></h1><b>some title</b>

    text_2 = SpanTag('text').execute()
    text_1 = 'Hello from ' + text_2
    h1_1 = H1Tag(text_1).execute()
    b_text = BTag('some title').execute()
    text = h1_1 + b_text
    print(text)

# 3. отобразить эту строчку "более удобно" = то есть улучшить 
#       модель классов

# СОВЕТ:
# 1 правило разработки: все что пишите, пишите удобно!!!