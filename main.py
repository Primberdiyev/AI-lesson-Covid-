from PIL import Image
import os

rasmlar = ["rasm1.jpg", "rasm2.jpg", "rasm3.jpg"]

for rasm_nomi in rasmlar:
    try:
       
        rasm = Image.open(rasm_nomi)
        
        oq_qora_rasm = rasm.convert("L")
        
        yangi_nomi = f"oq_qora_{rasm_nomi}"
        
        oq_qora_rasm.save(yangi_nomi)
        
        oq_qora_rasm.show()
        
        print(f"{rasm_nomi} -> {yangi_nomi} ga aylantirildi va ko'rsatildi.")
    except Exception as e:
        print(f"{rasm_nomi} fayli bilan muammo: {e}")
