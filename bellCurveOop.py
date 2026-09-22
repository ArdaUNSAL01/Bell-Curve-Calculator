import numpy as np

class dataPicker:
    def scoreInput(self):
        scoreArray = []
        print("""        Lütfen notları aşağıya sayı olarak giriniz. 
        Her sayı tek tek yazılıp 'Enter' tuşuna basıp onaylayın.
        Bitirmek için 'E' yazıp  enter a basın.""")

        while True:
            enter = input("        Notu buraya girin: ")
            if enter.upper() == "E":
                break
            try:
                sayi = float(enter)
                scoreArray.append(sayi)
            except ValueError:
                print("Hata! Lütfen sadece sayı ya da bitirmek istiyorsanız 'E' giriniz.")

        return np.array(scoreArray)

    def studentScore (self):
        selfscore = int(input("Hesaplanması için notunu gir ve 'Enter' tuşuna bas: "))
        return selfscore
    
       
class dataAnalize:
    def calcu(self):
        mean = np.mean(self.scoreArray)
        std = np.std(self.scoreArray, ddof = 1)
        z_score = (self.selfscore - mean) / std

        print(f"\n--- Sonuçlar ---")
        print(f"Sınıf Ortalaması: {mean:.2f}")
        print(f"Standart Sapma: {std:.2f}")
        print(f"Senin Z-Skorun: {z_score:.2f}")

        if z_score >= -1 :
            print("Çanın üstündesin. Hadi iyisin :)")
        else:
            print("Çanın altındasın. Kaldın:(")

dataPick = dataPicker()
allScores = dataPick.scoreInput()
stuScore = dataPick.studentScore()
calculate = dataAnalize(allScores,stuScore)
calculate.calcu()
