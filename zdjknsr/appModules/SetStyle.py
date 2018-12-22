import xlwt

def set_style():
    #   设置颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 17
    #   设置边框
    borders = xlwt.Borders()
    borders.bottom = xlwt.Borders.THIN
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom_colour = 0x40
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40

    style = xlwt.XFStyle()
    style.pattern = pattern
    style.borders = borders

    return style