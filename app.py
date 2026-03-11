import pandas as pd
import numpy as np

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

def generate_serial_numbers(seq_list):
    # Vytažení počátečních a koncových čísel pomocí stringových operací
    parsed = [(int(s.split('to-bis')[0].replace('NO.BP', '')), 
               int(s.split('to-bis')[1].replace('NO.BP', ''))) for s in seq_list]
    
    # Vektorizované vytvoření všech čísel pro maximální výkon
    all_nums = np.concatenate([np.arange(start, end + 1) for start, end in parsed])
    
    # Zformátování čísel zpět na délku 8 znaků a přidání prefixu BP
    formatted = ["BP" + str(num).zfill(8) for num in all_nums]
    return formatted

# Vytvoření DataFrame
all_serials = generate_serial_numbers(sequences)
df_serials = pd.DataFrame({"Serial_Number": all_serials})

print(f"Úspěšně vygenerováno {len(df_serials)} sériových čísel.")

# Možnost uložení rovnou do Excelu nebo schránky
# df_serials.to_excel("rozepsane_palety.xlsx", index=False)
# df_serials.to_clipboard(index=False)
