from fontTools.ttLib import TTFont
f = TTFont('LXGWWenKaiScreenR.ttf')
f.flavor = 'woff2'
f.save('LXGWWenKaiScreenR.woff2')