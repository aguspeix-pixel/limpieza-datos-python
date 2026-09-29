import pandas as pd

datos = {
    "cliente": [" Ana Perez", "juan gomez", "ANA PEREZ", "Luis Diaz", None, "juan gomez"],
    "producto": ["Mouse", "teclado ", "Mouse", "Monitor", "Teclado", "teclado "],
    "monto": ["1200", "3500,50", "1200", "45000", "2800", "3500,50"],
    "fecha": ["2026-09-01", "01/09/2026", "2026-09-01", "2026-09-03", "03/09/2026", "01/09/2026"],
}
pd.DataFrame(datos).to_csv("ventas_sucias.csv", index=False)
print("Archivo creado")