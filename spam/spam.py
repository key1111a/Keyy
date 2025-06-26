import time

print("\n[!] SPAM SMS / WA / CALL")
nomor = input("[?] Masukkan nomor target (contoh: 08xxxx): ")
jumlah = int(input("[?] Jumlah spam: "))

for i in range(jumlah):
    print(f"[+] Mengirim spam ke {nomor} [{i+1}]")
    time.sleep(0.5)

print("\n[✓] Selesai spam!")
