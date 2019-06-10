from util import word_density

# File PATH
file = "example_file/Game.of.Thrones.S08E06.srt"
print("{}\nYolundaki dosya analiz ediliyor..\n".format(file))

# Class
word_density = word_density(file)
print("word_density sınıfı oluşturuldu.\n")

# DataFrame
df = word_density.get_df()
print("word_density.get_df() ile DataFrame oluşturuldu.\nDataFrame içerisinde dosya içerisinde geçen kelimeler ve tekrar sayıları var.\n")

print("İlk 5 Satır.\n")
# let's take a quick look
print(df.head())


input("Grafiği Çizdirmek için bir tuşa basın..")
# Make Chart (Default:25)
word_density.get_chart()


# Make Chart (10)
word_density.get_chart(10)