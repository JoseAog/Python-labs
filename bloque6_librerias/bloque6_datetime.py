from datetime import datetime, timedelta

ahora = datetime.now()
print("Fecha y hora actual:", ahora)

mañana = ahora + timedelta(days=1)
print("Mañana será:", mañana.strftime("%d/%m/%Y %H:%M"))
