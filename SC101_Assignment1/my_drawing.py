"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=500, height=500, title='iron man')
    outline1 = GOval(400, 400, x=50, y=50)
    outline1.color = 'red'
    window.add(outline1)

    outline2 = GOval(395, 395, x=52, y=52)
    outline2.color = 'red'
    window.add(outline2)

    l1 = GLine(155, 125, 190, 100)
    l1.color = 'red'
    window.add(l1)

    l2 = GLine(155, 125, 153, 220)
    l2.color = 'red'
    window.add(l2)

    l3 = GLine(153, 220, 145, 225)
    l3.color = 'red'
    window.add(l3)

    l4 = GLine(145, 225, 147, 280)
    l4.color = 'red'
    window.add(l4)

    l5 = GLine(147, 280, 155, 285)
    l5.color = 'red'
    window.add(l5)

    l6 = GLine(155, 285, 190, 360)
    l6.color = 'red'
    window.add(l6)

    l7 = GLine(190, 360, 175, 390)
    l7.color = 'red'
    window.add(l7)

    l7 = GLine(205, 420, 175, 390)
    l7.color = 'red'
    window.add(l7)

    l8 = GLine(205, 420, 225, 390)
    l8.color = 'red'
    window.add(l8)

    l9 = GLine(290, 390, 225, 390)
    l9.color = 'red'
    window.add(l9)

    l10 = GLine(290, 390, 315, 420)
    l10.color = 'red'
    window.add(l10)

    l11 = GLine(340, 390, 315, 420)
    l11.color = 'red'
    window.add(l11)

    l12 = GLine(340, 390, 325, 360)
    l12.color = 'red'
    window.add(l12)

    l13 = GLine(350, 285, 325, 360)
    l13.color = 'red'
    window.add(l13)

    l14 = GLine(350, 285, 358, 280)
    l14.color = 'red'
    window.add(l14)

    l15 = GLine(360, 225, 358, 280)
    l15.color = 'red'
    window.add(l15)

    l16 = GLine(360, 225, 352, 220)
    l16.color = 'red'
    window.add(l16)

    l17 = GLine(350, 125, 352, 220)
    l17.color = 'red'
    window.add(l17)

    l18 = GLine(350, 125, 315, 100)
    l18.color = 'red'
    window.add(l18)

    l19 = GLine(275, 127, 315, 100)
    l19.color = 'red'
    window.add(l19)

    l20 = GLine(275, 127, 265, 150)
    l20.color = 'red'
    window.add(l20)

    l21 = GLine(240, 150, 265, 150)
    l21.color = 'red'
    window.add(l21)

    l22 = GLine(240, 150, 230, 127)
    l22.color = 'red'
    window.add(l22)

    l22 = GLine(190, 100, 230, 127)
    l22.color = 'red'
    window.add(l22)

    l_eye = GPolygon()
    l_eye.filled = True
    l_eye.fill_color = 'ivory'
    l_eye.color = 'red'
    l_eye.add_vertex((160, 240))
    l_eye.add_vertex((220, 260))
    l_eye.add_vertex((215, 270))
    l_eye.add_vertex((185, 268))
    l_eye.add_vertex((155, 245))
    window.add(l_eye)


    r_eye = GPolygon()
    r_eye.filled = True
    r_eye.fill_color = 'ivory'
    r_eye.color = 'red'
    r_eye.add_vertex((345, 240))
    r_eye.add_vertex((285, 260))
    r_eye.add_vertex((290, 270))
    r_eye.add_vertex((320, 268))
    r_eye.add_vertex((350, 245))
    window.add(r_eye)

    l23 = GLine(220, 260, 285, 260)
    l23.color = 'red'
    window.add(l23)

    l24 = GLine(180, 380, 205, 405)
    l24.color = 'red'
    window.add(l24)

    l25 = GLine(220, 380, 205, 405)
    l25.color = 'red'
    window.add(l25)

    l26 = GLine(220, 380, 295, 380)
    l26.color = 'red'
    window.add(l26)

    l27 = GLine(315, 405, 295, 380)
    l27.color = 'red'
    window.add(l27)

    l28 = GLine(315, 405, 335, 380)
    l28.color = 'red'
    window.add(l28)

    l29 = GLine(155, 245, 153, 220)
    l29.color = 'red'
    window.add(l29)

    l30 = GLine(160, 240, 154, 155)
    l30.color = 'red'
    window.add(l30)

    l31 = GLine(146, 250, 163, 290)
    l31.color = 'red'
    window.add(l31)

    l32 = GLine(225, 390, 163, 290)
    l32.color = 'red'
    window.add(l32)

    l33 = GLine(359, 250, 343, 290)
    l33.color = 'red'
    window.add(l33)

    l34 = GLine(290, 390, 343, 290)
    l34.color = 'red'
    window.add(l34)

    l35 = GLine(345, 240, 351, 160)
    l35.color = 'red'
    window.add(l35)

    l36 = GLine(350, 245, 352, 220)
    l36.color = 'red'
    window.add(l36)

    l37 = GLine(155, 125, 235, 165)
    l37.color = 'red'
    window.add(l37)

    l38 = GLine(235, 165, 275, 165)
    l38.color = 'red'
    window.add(l38)

    l39 = GLine(275, 165, 350, 125)
    l39.color = 'red'
    window.add(l39)

    label = GLabel('IRON MAN')
    label.font = '-35'
    label.color = 'red'
    window.add(label, 175, 495)


if __name__ == '__main__':
    main()
