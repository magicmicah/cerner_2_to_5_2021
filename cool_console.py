# cerner_2tothe5th_2021

# Console scripts can be boring. So add some color or emojis with the console package.
from console import fg, bg, fx

input("Aren't console programs boring?"); input("Wouldn't it be nice if they were flashy and cool?")
text = fg.red + 'Well ' + fg.orange + 'now ' + fg.yellow + 'they ' + fg.green + 'can ' + fg.blue  + 'be. ' + fg.default; input(text)
template = bg.i22('{}'); input(template.format('Template your inputs to highlight important text.'))
fstrings = 'fstrings'; input(f"Works with {fg.blue + fstrings + fg.default}, too.")
input(fg.black + 'Hide easter eggs' + fg.default)
input("You're going to " + fg.red + fx.italic + '♥love♥ ' + fx.end + fg.default + 'using console.' )
input("There's lots of possibilities. Learn more at https://mixmastamyk.bitbucket.io/console")