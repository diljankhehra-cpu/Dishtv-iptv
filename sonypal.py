from datetime import datetime, timedelta

now = datetime.utcnow()

programs = [
    ("Taarak Mehta Ka Ooltah Chashmah","Comedy"),
    ("Crime Patrol","Crime"),
    ("Mere Sai","Drama"),
    ("Adaalat","Courtroom Drama"),
]

xml = ['<?xml version="1.0" encoding="UTF-8"?><tv>']
xml.append('<channel id="sonypal.in"><display-name>Sony Pal</display-name></channel>')

start = now

for title,cat in programs:
    stop = start + timedelta(minutes=30)
    xml.append(f'<programme start="{start.strftime("%Y%m%d%H%M%S")} +0530" stop="{stop.strftime("%Y%m%d%H%M%S")} +0530" channel="sonypal.in">')
    xml.append(f'<title>{title}</title><category>{cat}</category></programme>')
    start = stop

xml.append('</tv>')

open("sonypal.xml","w").write("\n".join(xml))
