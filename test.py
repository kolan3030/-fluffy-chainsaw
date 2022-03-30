# import turtle
# import math
# def drawCircleTurtle(x,y,r):
#     turtle.up()
#     turtle.setpos(x + r,y)
#     turtle.down()
#     for i in range(0,365,5):
#         a = math.radians(i)
#         turtle.setpos(x + r*math.cos(a),y+r*math.sin(a))
#
# drawCircleTurtle(100,100,50)
# turtle.mainloop()



# from lxml import etree
# # text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
#          <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
#          <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
#          <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
#          <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
#
# text = '''
# <li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
# '''
#
# text = '''
# <li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
# '''
#
# result = etree.tostring(html)
# print(result.decode('utf-8'))
# result = html.xpath('//ul/a')
# result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
# result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/parent::*/@class')
# result = html.xpath("//li[@class='item-0']//text()")
# result = html.xpath("//li[@class='item-0']/a/text()")
# result = html.xpath('//li[contains(@class,"li-first")]/a/text()')
# result = html.xpath('//li[contains(@class,"li")]/a/text() ')

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
#          <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
#          <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
#          <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
#          <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# # result = html.xpath('//li[position()<3]/a/text()')
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)
# # print(id(result[0]))



from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)

result = html.xpath('//li[1]/ancestor::div')
print(result)

result = html.xpath('//li[1]/attribute::*')
print(result)

result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
print(result)

result = html.xpath('//li[1]/descendant::span')
print(result)

result = html.xpath('//li[1]/following::*[2]')
print(result)

result = html.xpath('//li[1]/following-sibling::*')
print(result)