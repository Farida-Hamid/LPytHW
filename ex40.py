class Song(object):
  def __init__(self, lyrics):
    self.lyrics = lyrics
  
  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So, I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

some_one_like_you = Song('')
some_one_like_you.lyrics = ["Never minde I'll find someone like you",
                            "I wish nothing but the best for you",
                            "Don't forget me",
                            "I bet I'll remember you said",
                            "Sometimes ot lasts in love and some times it hurts instead"]

some_one_like_you.sing_me_a_song()