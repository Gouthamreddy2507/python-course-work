
class Status:
    def uploadimage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class Statusv1(Status): 
    def addcaption(self,text=None):
        self.caption = text
        print(f"{self.caption} is added to your status")

class Statusv2(Status):
    def like(self):
        print("you can like status")

class Statusv3(Statusv1,Statusv2):
    def addmusic(self,music):
        self.music = music
        print(f"{self.music} is added to your status")

class Statusv4(Statusv3):
    def videolength(self,video):
        self.video = video
        print(f"{self.video} is uploaded to your status")

goutham = Status()
goutham.uploadimage("selfie")

print("----single inheritance-----")

soul = Statusv1()
soul.uploadimage("good mrng.png")
soul.addcaption("Good Morning!!")

print("--------multi level-----")

crazy = Statusv2()
crazy.uploadimage("selfie.png")
crazy.like()

print("---hierechical----")

chintu = Statusv3()
chintu.uploadimage("mountains and trees.png")
chintu.addcaption("no wifi")
chintu.like()
chintu.addmusic("mature.mp3")

print("-----multiple-------")

vishwa = Statusv4()
vishwa.uploadimage("sunrise.png")
vishwa.addcaption("nothing")
vishwa.like()
vishwa.addmusic("music.mp3")
vishwa.videolength("video.mp4")





#super
class Instagram():
    def __init__(self,username):
        self.username = username
        self.post=[]
        print(f"{self.username.center(40,'-')}")     

    def uploadpost(self,image):
        self.post.append(image)
        print(f"{image} is posted")

class Instagramv1(Instagram):
    def __init__(self, username,bio):
        super().__init__(username)  
        self.bio = bio
        print(f"bio uploaded")

    def uploadpost(self,post,music):
        super().uploadpost(post)
        self.music = music
        print(f"{self.music} is uploaded")

goutham = Instagram("goutham123")
goutham.uploadpost("Good Morning.png")
soul = Instagramv1("soul123","coder")
soul.uploadpost("Good Evening.png","music.mp3")