
import pandas as pd

# 1. Leer el archivo sucio
df = pd.read_csv("ventas_sucias.csv")
print("ANTES DE LIMPIAR:")
print(df)
print()

# 2. Limpiar los textos: sacar espacios y unificar mayúsculas
df["cliente"] = df["cliente"].str.strip().str.title()
df["producto"] = df["producto"].str.strip().str.title()

# 3. Completar los clientes vacíos
df["cliente"] = df["cliente"].fillna("Sin nombre")

# 4. Convertir el monto a número (cambiar coma por punto)
df["monto"] = df["monto"].str.replace(",", ".", regex=False).astype(float)

# 5. Unificar las fechas
def parsear_fecha(texto):
    if "-" in texto:
        return pd.to_datetime(texto, format="%Y-%m-%d")
    return pd.to_datetime(texto, format="%d/%m/%Y")

df["fecha"] = df["fecha"].apply(parsear_fecha)

# 6. Eliminar filas repetidas
df = df.drop_duplicates()

# 7. Guardar el resultado limpio
df.to_csv("ventas_limpias.csv", index=False)

print("DESPUÉS DE LIMPIAR:")
print(df)
print()
print("Total de ventas:", df["monto"].sum())