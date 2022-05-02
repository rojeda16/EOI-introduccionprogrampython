from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

fechacastellano= datetime.now()
print(fechacastellano)
print("fecha castellano:",fechacastellano.strftime("%A %d %b %y"))