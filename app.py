import pandas as pd
import re
import streamlit as st

# Tvoje zdrojová data
sequences = [
    "NO.BP05757001to-bisNO.BP05758000",
    "NO.BP05756001to-bisNO.BP05757000",
    "NO.BP05759001to-bisNO.BP05760000",
    "NO.BP05752001to-bisNO.BP05753000",
    "NO.BP05751001to-bisNO.BP05752000",
    "NO.BP05760001to-bisNO.BP05761000",
    "NO.BP05754001to-bisNO.BP05755000",
    "NO.BP05758851to-bisNO.BP05758900",
    "NO.BP05758901to-bisNO.BP05758950",
    "NO.BP05758951to-bisNO.BP05759000",
    "NO.BP05758651to-bisNO.BP05758700",
    "NO.BP05758601to-bisNO.BP05758650",
    "NO.BP05758001to-bisNO.BP05758050",
    "NO.BP05758801to-bisNO.BP05758850",
    "NO.BP05758701to-bisNO.BP05758750",
    "NO.BP05758751to-bisNO.BP05758800",
    "NO.BP05758501to-bisNO.BP05758550",
    "NO.BP05755651to-bisNO.BP05755700",
    "NO.BP05755201to-bisNO.BP05755250",
    "NO.BP05755501to-bisNO.BP05755550",
    "NO.BP05755551to-bisNO.BP05755600",
    "NO.BP05755051to-bisNO.BP05755100",
    "NO.BP05755001to-bisNO.BP05755050",
    "NO.BP05755401to-bisNO.BP05755450",
    "NO.BP05755751to-bisNO.BP05755800",
    "NO.BP05755851to-bisNO.BP05755900",
    "NO.BP05755701to-bisNO.BP05755750",
    "NO.BP05755601to-bisNO.BP05755650",
    "NO.BP05755351to-bisNO.BP05755400",
    "NO.BP05755151to-bisNO.BP05755200",
    "NO.BP05755251to-bisNO.BP05755300",
    "NO.BP05755451to-bisNO.BP05755500",
    "NO.BP05755951to-bisNO.BP05756000",
    "NO.BP05755101to-bisNO.BP05755150",
    "NO.BP05755801to-bisNO.BP05755850",
    "NO.BP05755301to-bisNO.BP05755350",
    "NO.BP05755901to-bisNO.BP05755950"
]

def generate_serial_columns_safe(seq_list):
    data_dict = {}
    
    for s in seq_list:
        matches = re.findall(r'BP(\d+)', s)
        
        if len(matches) == 2:
            start = int(matches[0])
            end = int(matches[1])
            
            if end - start > 10000:
                st.error(f"⚠️ Přeskočeno: Sekvence {s} má podezřele velký rozsah.")
                continue
            if end < start:
                st.warning(f"⚠️ Přeskočeno: V sekvenci {s} je počáteční číslo větší než koncové.")
                continue
                
            # Zápis čísel pro daný sloupec
            col_data = [f"BP{str(num).zfill(8)}" for num in range(start, end + 1)]
            
            # Název sloupce bude rovnou původní název sekvence (očistíme ho od balastu pro lepší čitelnost)
            col_name = s.replace("NO.", "").replace("to-bis", " - ")
            data_dict[col_name] = col_data
            
        else:
            if s.strip():
                st.warning(f"⚠️ Řádek '{s}' nemá správný formát a byl přeskočen.")
                
    return data_dict

# 1. Vygenerujeme data do slovníku, kde každý klíč je název sloupce a hodnota je seznam čísel
data_columns = generate_serial_columns_safe(sequences)

# 2. Vytvoříme tabulku - 'orient=index' a 'transpose()' zajistí, že se kratší sloupce automaticky zarovnají
df_serials = pd.DataFrame.from_dict(data_columns, orient='index').transpose()

# 3. Místo ošklivých 'NaN' (Not a Number) vložíme prázdné znaky u těch sekvencí, co mají jen 50 kusů
df_serials = df_serials.fillna("")

# 4. Výpis do aplikace se skrytým číslováním řádků
st.success(f"Úspěšně vygenerováno {len(data_columns)} sloupců.")
st.dataframe(df_serials, hide_index=True)
