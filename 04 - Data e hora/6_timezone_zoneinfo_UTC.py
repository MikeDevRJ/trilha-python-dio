from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# 1. Captura a hora exata em UTC (Padrão universal)
agora_utc = datetime.now(timezone.utc)

# 2. Converte para exibição no fuso de cada região
data_oslo = agora_utc.astimezone(ZoneInfo("Europe/Oslo"))
data_sp = agora_utc.astimezone(ZoneInfo("America/Sao_Paulo"))

print("UTC:", agora_utc)
print("Oslo:", data_oslo)
print("SP:", data_sp)