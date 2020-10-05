import cgi
import sys
import codecs
import os
import http.cookies
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "off")
text2 = form.getfirst("TEXT_2", "off")
text3 = form.getfirst("TEXT_3", "off")
text4 = form.getfirst("TEXT_4", "off")
text5 = form.getfirst("TEXT_5", "off")
text6 = form.getfirst("TEXT_6", "off")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обробка даних форм!</title>
        </head>
        <body>""")

print("<h1>Обробка даних форм!</h1>")
print("<p>Ім'я: {}</p>".format(text1))
print("<p>Прізвище: {}</p>".format(text2))
print("<p>Англійська: {}</p>".format(text3))
print("<p>Російська: {}</p>".format(text4))
print("<p>Математика: {}</p>".format(text5))
print("<p>Хімія: {}</p>".format(text6))

print("""</body>
        </html>""")


hit_count_path = os.path.join(os.path.dirname(__file__), "hit-count.txt")

if os.path.isfile(hit_count_path):
    with open(hit_count_path) as fp:
        hit_count_str = fp.read()
        try:
            hit_count = int(hit_count_str)
        except ValueError:
            hit_count = 0
    hit_count += 1
else:
    hit_count = 1

with open(hit_count_path, 'w') as fp:
    fp.write(str(hit_count))




html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Current date</title>
</head>
<body>
  <p>
  Кількість відкривань: {0}
  </p>
</body>
</html>
""".format(cgi.escape(str(hit_count)))

print(html)


