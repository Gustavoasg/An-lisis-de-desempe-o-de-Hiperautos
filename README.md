# Hypercar Performance Analysis 🚀

Este repositorio reúne especificaciones y análisis comparativo de las prestaciones de **hipercoches actuales** (combustión y eléctricos). El foco es comparar: potencia, velocidad máxima reportada, 0-60 mph y notas de verificación.

## Contenido
- `data/hypercar_specs.csv` - dataset compilado con especificaciones públicas y notas.
- `notebooks/analysis.ipynb` - notebook (vacío) para análisis y visualizaciones.
- `requirements.txt` - dependencias sugeridas.
- `README.md` - (este archivo).

## Metodología
1. Recolecté datos de fuentes oficiales del fabricante y medios especializados (ej.: Bugatti, Rimac, Koenigsegg, Hennessey, Autoweek, Car and Driver, Racelogic).
2. Anoté si la cifra es 'claim' (reclamada por fabricante), 'verified' (verificada por terceros como Racelogic) o 'test' (registro en pista, puede ser one-way).
3. Guardé las cifras en `data/hypercar_specs.csv` para que puedas cargarlas en un notebook y analizarlas (boxplots, scatter power vs top speed, tablas).

## Notas rápidas (fuentes principales consultadas)
- Yangwang U9 Xtreme — récord de 308.4 mph reportado en pruebas (Autoweek / medios recientes).  
- Bugatti Chiron Super Sport 300+ — registro histórico de ~304.77 mph (one-way run).  
- Rimac Nevera — top speed registrado 412 km/h (258 mph) y múltiples récords EV según Rimac.  
- Koenigsegg Jesko Absolut — claim teórico >330 mph (fabricante).  
- SSC Tuatara — run verificada de 295 mph registrada por Racelogic en 2022; intentos previos de 316/331 mph fueron disputados.  

(En el chat siguiente incluyo las fuentes citadas para estas afirmaciones.)

## Cómo usar
1. Abre `notebooks/analysis.ipynb` en Jupyter/Colab.  
2. Carga `data/hypercar_specs.csv` y comienza a explorar. Ejemplo (Python):
```python
import pandas as pd
df = pd.read_csv('data/hypercar_specs.csv')
df
```

## Recomendaciones para el análisis
- Normaliza unidades (mph/kmh).  
- Clasifica filas por tipo (EV vs ICE).  
- Grafica potencia vs top_speed, y potencia vs 0-60.  
- Añade una columna `verification` con valores: verified / manufacturer_claim / media_test.

