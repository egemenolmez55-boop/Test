import random

# Sorular ve cevaplar
sorular = [
    ("Türkiye Cumhuriyetinin başkenti neresidir?", "ankara"),
        ("Atatürk kaç yılında doğmuştur?", "1881"),
            ("İstiklal Marşı'nın yazarı kimdir?", "mehmet akif ersoy"),
                ("Bir gün kaç saattir?", "24"),
                    ("Bir saat kaç saniyedir?", "3600")
                    ]

                    # Soruların sırasını karıştıralım
                    random.shuffle(sorular)

                    # Skor değişkeni
                    dogru_sayisi = 0
                    toplam_soru = len(sorular)

                    # Soru sorma döngüsü
                    for i, (soru, cevap) in enumerate(sorular, start=1):
                        print(f"\nSoru {i}: {soru}")
                            kullanici_cevabi = input("Cevabın: ").strip().lower()

                                if kullanici_cevabi == cevap.lower():
                                        dogru_sayisi += 1
                                                print("✅ Doğru!")
                                                    else:
                                                            print(f"❌ Yanlış! Doğru cevap: {cevap}")

                                                                print(f"Skor: {dogru_sayisi}/{toplam_soru}")

                                                                # Final sonucu
                                                                print("\n--- Oyun Bitti ---")
                                                                print(f"Toplam Doğru: {dogru_sayisi}/{toplam_soru}")

                                                                if dogru_sayisi == toplam_soru:
                                                                    print("🏆 Mükemmel! Hepsini bildin!")
                                                                    elif dogru_sayisi >= 3:
                                                                        print("🔥 Fena değilsin!")
                                                                        else:
                                                                            print("😅 Biraz çalışmak lazım dostum.")