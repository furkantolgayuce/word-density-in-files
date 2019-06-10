from util import word_density

# File PATH
file = "example_file/Game.of.Thrones.S08E06.srt"

# Class
word_density = word_density(file)

# DataFrame
df = word_density.get_df()

# let's take a quick look
print(df.head())


# Make Chart (Default:25)
word_density.get_chart()


# Make Chart (10)
word_density.get_chart(10)