import csv

from reportlab.pdfgen import canvas

from reportlab.platypus import SimpleDocTemplate, TableStyle, Table
from reportlab.platypus import Paragraph, Spacer

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

GROUP1_ROW = 2
GROUP2_ROW = 3
GROUP3_ROW = 4
GROUP4_ROW = 5
GROUP5_ROW = 6
GROUP6_ROW = 7
GROUP7_ROW = 8
GROUP8_ROW = 9

FINAL_RANK_COL = 14

w, h = A4
with open("./score_sheet - scoresheet1.csv", 'r', encoding="utf8", newline='') as file:
    csvreader = csv.reader(file)
    scoresheet = list(csvreader)

sample_style_sheet = getSampleStyleSheet()

styleNormalCustom = ParagraphStyle(
    'styleNormalCustom',
    fontName='STSong-Light',
    parent=sample_style_sheet["Title"]
)

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

doc = SimpleDocTemplate('hello-world.pdf')

flowable = []

def firstPageSetup(canvas, doc):
    canvas.saveState()
    canvas.drawImage('./images/report_template1.png', 0, 0)
    textObject = canvas.beginText()
    canvas.drawImage('./images/icon.png', 235, h-222, width=50, height=50, mask='auto')
    textObject.setTextOrigin(277, h-206)
    textObject.setFont("STSong-Light", 16)
    textObject.textLine("團體評評理")
    textObject.moveCursor(0,8)
    textObject.setFont("STSong-Light", 13)
    textObject.setLeading(20)
    textObject.textLines('''
        恭喜玩家們在一連串的關卡中脫穎而出，在所有
        關卡中分數加總最高，是今天的佼佼者啊！
        森林之王頒給你們是實至名歸。
    ''')
    canvas.drawImage('./images/icon.png', 59, h-333, width=50, height=50, mask='auto')
    textObject.setTextOrigin(101, h-316)
    textObject.setFont("STSong-Light", 16)
    textObject.textLine("身體健康望周知")
    textObject.setFont("STSong-Light", 13)
    textObject.textLines('''
        嘿～剛剛從回饋問卷中依照長者健康整合式評估的結果出爐！
        你們這組高年級玩家的身體狀態：非常健康，老當益壯！
    ''')
    canvas.drawImage('./images/icon.png', 59, h-393, width=50, height=50, mask='auto')
    textObject.setTextOrigin(101, h-377)
    textObject.setFont("STSong-Light", 16)
    textObject.textLine("你的感受我在乎")
    textObject.moveCursor(0,8)
    textObject.setFont("STSong-Light", 13)
    textObject.textLines('''
        今天的關卡設計中，我們其實有暗藏一些小巧思。第一是我們四個關卡分別以平衡、
        敏捷、肌力與柔軟四大面向來規劃！第二呢，那就是設計發想皆是來自於
        高齡者體適能檢測項目喔！ 希望你們在做些關卡的時候也對這些項目更有認識！
    ''')
    textObject.setTextOrigin(101, h-670)
    textObject.setFont("STSong-Light", 13)
    textObject.textLine("之後回去也不妨多練習這些動作來提升體適能唷！")
    canvas.drawText(textObject)
    canvas.restoreState()


bogustext = "動一動報告書"
table_data = [['關卡名稱', '檢測項目'],
              ['平衡超雞群', '30秒單腳站立'],
              ['路很難走', '8 英呎起身繞行（2.44公尺）'],
              ['站立起乩', '椅子坐立'],
              ['軟爛的人', '抓背測驗、椅子坐姿體前彎']]

tableStyle = TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # 置中對齊
    ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'), # 字體
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), # 上下置中
    ('GRID', (0, 0), (-1, -1), 1, colors.Color(1.00000,0.60000,0.60000)), # width 0.5
    ('BACKGROUND', (0, 0), (-1, 0), colors.Color(1.00000,0.80392,0.80392)),
])

p = Paragraph(bogustext, styleNormalCustom)
s = Spacer(0, 337)
table = Table(table_data, [150,250],40, style=tableStyle)
flowable.append(p)
flowable.append(s)
flowable.append(table)
doc.build(flowable, onFirstPage=firstPageSetup)