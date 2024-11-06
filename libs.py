def title_program():
    title = "Program Penilaian Akadademik"
    sign = "*"
    sign = sign * (len(title) + 8)
    
    print(sign)
    print(f"*** {title} ***")
    print(sign)
    
def grade_nilai(nilai):
    if nilai >= 9 :
        print("Kamu mendapatkan Grade A+")
        
    elif nilai >= 8 and nilai < 9 :
        print("Kamu mendapatkan Grade A")
    elif nilai > 5 and nilai < 8:
        print("Kamu mendapatkan Grade B")
    else:
        print("Kamu mendapatkan Grade C")
        
