from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles.monokai import MonokaiStyle
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

def rounded_rectangle(self: ImageDraw, xy, corner_radius, fill=None, outline=None):
    upper_left_point = xy[0]
    bottom_right_point = xy[1]
    self.rectangle(
        [
            (upper_left_point[0], upper_left_point[1] + corner_radius),
            (bottom_right_point[0], bottom_right_point[1] - corner_radius)
        ],
        fill=fill,
        outline=outline
    )
    self.rectangle(
        [
            (upper_left_point[0] + corner_radius, upper_left_point[1]),
            (bottom_right_point[0] - corner_radius, bottom_right_point[1])
        ],
        fill=fill,
        outline=outline
    )
    self.pieslice([upper_left_point, (upper_left_point[0] + corner_radius * 2, upper_left_point[1] + corner_radius * 2)],
        180,
        270,
        fill=fill,
        outline=outline
    )
    self.pieslice([(bottom_right_point[0] - corner_radius * 2, bottom_right_point[1] - corner_radius * 2), bottom_right_point],
        0,
        90,
        fill=fill,
        outline=outline
    )
    self.pieslice([(upper_left_point[0], bottom_right_point[1] - corner_radius * 2), (upper_left_point[0] + corner_radius * 2, bottom_right_point[1])],
        90,
        180,
        fill=fill,
        outline=outline
    )
    self.pieslice([(bottom_right_point[0] - corner_radius * 2, upper_left_point[1]), (bottom_right_point[0], upper_left_point[1] + corner_radius * 2)],
        270,
        360,
        fill=fill,
        outline=outline
    )

def make(code, filename):
    # create a custom background
    class MS(MonokaiStyle):
        background_color = '#661A0A'

    # config the formatter
    fm = ImageFormatter(
        font_name="Liberation Mono", line_pad=10,
        line_numbers=False, style=MS, font_size=25)

    img = Image.open(BytesIO(highlight(code, PythonLexer(), fm)))


    m = round(max(img.size)*1.05)
    offset = ((m - img.size[0]) // 2, (m - img.size[1]) // 2)
    background = Image.new("RGBA", (m, m), (200,200,200,0))
    draw = ImageDraw.Draw(background)

    box = (((m-img.size[0]*1.03)//2, (m-img.size[1]*1.03)//2), ((m+img.size[0]*1.03)//2, (m+img.size[1]*1.03)//2))

    dt = 50
    color = tuple([20]*3)
    blur = 50
    rounded_rectangle(draw, ((box[0][0]+dt, box[0][1]+dt), (box[1][0]+dt, box[1][1]+dt) ), 20, fill=color)
    background = background.filter(ImageFilter.GaussianBlur(blur))

    draw = ImageDraw.Draw(background)
    rounded_rectangle(draw, box, 20, fill='#661A0A')

    background.paste(img, offset)
    background.save(filename)




with open('snippets/#2.py') as f:
    data = f.readlines()

data = [x.strip('\n') for x in data]

n = 0
while True:
    if not data[n].strip().startswith('#'):
        break
    n += 1

caption = ' '.join([x.strip('# ') if x.strip('# ') else '\n' for x in data[:n]] )
code = '\n'.join(data[n:])

with open('out.txt', 'w') as f:
    f.write(caption)

make(code, 'out.bmp')
