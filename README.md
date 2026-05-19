# Resistansbaserad temperaturuppskattning i kraftledningar med tvåänds fasormätningar
### En analys av mätkrav och känslighet  
Sævar Ingi Sveinsson, Mittuniversitetet, 2026

Detta repo innehåller all kod, datahantering och figurgenerering som används i mitt examensarbete 
"Resistansbaserad temperaturuppskattning i kraftledningar med tvåänds fasormätningar: en analys av mätkrav och känslighet".
Det bör nämnas att spänningsfallsbaserade impedansmetoden hade arbets namnet Z-drop i kodningen.

## 📌 Innehål
Projektet undersöker:
- hur temperaturinformation kan extraheras från synkroniserade fasormätningar
- hur framåtriktade modeller uppskattar den elektriska temperatursignalens storlek
- hur tre bakåtriktade metoder (Singh, SI, effektmetoden) beter sig på verklig tvåändsdata
- hur känsliga metoderna är för små magnitud- och vinkelavvikelser
- vilka mätkrav som krävs för praktisk användning

## 📁 Struktur
```
SIS/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── notebooks/
│   ├── 01_forward_model.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_backward_methods.ipynb
│   ├── 04_sensitivity_analysis.ipynb
│   └── 05_plot_generation.ipynb
│
├── src/
│   ├── forward_model.py
│   ├── backward_methods.py
│   ├── sensitivity.py
│   ├── utils.py
│   ├── data_loader.py
│   └── __init__.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── example/
│
├── results/
│   ├── tables/
│   └── figures/
│
└── thesis/
    └── BS_thesis_01.pdf
```

## 🧪 Körning
Installera beroenden:
```
pip install -r requirements.txt
```

Starta Jupyter:
```
jupyter lab
```

## 📊 Data
- `data/raw/` innehåller rådata från sändar- och mottagarstation.
- `data/processed/` innehåller synkad och rensad data.

## 📈 Resultat
Alla figurer och tabeller som används i thesis finns i `results/`.

## 🔒 Licens
Detta projekt är **inte licensierat**.  
Kod och figurer får **inte användas, kopieras eller distribueras** utan tillstånd.
