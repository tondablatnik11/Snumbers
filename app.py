import pandas as pd
import re
import streamlit as st

# Sem můžeš zkopírovat všechny své sekvence
sequences = [
"NO.BP05757001to-bisNO.BP05758000"		
"NO.BP05756001to-bisNO.BP05757000"		
"NO.BP05759001to-bisNO.BP05760000"		
"NO.BP05752001to-bisNO.BP05753000"		
"NO.BP05751001to-bisNO.BP05752000"		
"NO.BP05760001to-bisNO.BP05761000"		
"NO.BP05754001to-bisNO.BP05755000"		





"NO.BP05758851to-bisNO.BP05758900"			
"NO.BP05758901to-bisNO.BP05758950"			
"NO.BP05758951to-bisNO.BP05759000"			
"NO.BP05758651to-bisNO.BP05758700"			
"NO.BP05758601to-bisNO.BP05758650"			
"NO.BP05758001to-bisNO.BP05758050"			
"NO.BP05758801to-bisNO.BP05758850"			
"NO.BP05758701to-bisNO.BP05758750"			
"NO.BP05758751to-bisNO.BP05758800"			
"NO.BP05758501to-bisNO.BP05758550"	



"NO.BP05755651to-bisNO.BP05755700"
"NO.BP05755201to-bisNO.BP05755250"
"NO.BP05755501to-bisNO.BP05755550"
"NO.BP05755551to-bisNO.BP05755600"
"NO.BP05755051to-bisNO.BP05755100"
"NO.BP05755001to-bisNO.BP05755050"
"NO.BP05755401to-bisNO.BP05755450"
"NO.BP05755751to-bisNO.BP05755800"
"NO.BP05755851to-bisNO.BP05755900"
"NO.BP05755701to-bisNO.BP05755750"
"NO.BP05755601to-bisNO.BP05755650"
"NO.BP05755351to-bisNO.BP05755400"
"NO.BP05755151to-bisNO.BP05755200"
"NO.BP05755251to-bisNO.BP05755300"
"NO.BP05755451to-bisNO.BP05755500"
"NO.BP05755951to-bisNO.BP05756000"
"NO.BP05755101to-bisNO.BP05755150"
"NO.BP05755801to-bisNO.BP05755850"
"NO.BP05755301to-bisNO.BP05755350"
"NO.BP05755901to-bisNO.BP05755950"	
]

def generate_serial_numbers_safe(seq_list):
    all_serials = []
    
    for s in seq_list:
        # Bezpečné vytažení všech čísel, která následují za 'BP' pomocí RegEx
        matches = re.findall(r'BP(\d+)', s)
        
        if len(matches) == 2:
            start = int(matches[0])
            end = int(matches[1])
            
            # Bezpečnostní pojistka proti překlepům ve vstupních datech
            # (Zabrání pádu aplikace, pokud je rozdíl nesmyslně velký)
            if end - start > 10000:
                st.error(f"⚠️ Přeskočeno: Sekvence {s} má podezřele velký rozsah ({end - start} položek). Zkontroluj překlepy.")
                continue
            if end < start:
                st.warning(f"⚠️ Přeskočeno: V sekvenci {s} je počáteční číslo větší než koncové.")
                continue
                
            # Použití standardního generátoru (šetrnější na paměť než numpy.arange)
            for num in range(start, end + 1):
                all_serials.append(f"BP{str(num).zfill(8)}")
        else:
            if s.strip(): # Ignoruje prázdné řádky
                st.warning(f"⚠️ Řádek '{s}' nemá správný formát a byl přeskočen.")
            
    return all_serials

# Generování a vytvoření DataFrame
all_serials = generate_serial_numbers_safe(sequences)
df_serials = pd.DataFrame({"Serial_Number": all_serials})

# Výpis do Streamlit aplikace
st.success(f"Úspěšně vygenerováno {len(df_serials)} sériových čísel.")
st.dataframe(df_serials)
