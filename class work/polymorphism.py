#method overriding

class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with:\n1.Normal Quality\n2.Ads run\n3.No Background Play\n4.Limited Videos Download\n5.Music with Ads")
    def like(self):
        pass
    def share(self):
        pass
    def subscribe(self):
        pass
    def comment(self):
        pass

class premiumuser(normaluser):
    def playvideo(self,name):
        print(f"\n{name} is playing video with:\n1.Primium Quality\n2.No Ads run\n3.Background Play\n4.Videos Download\n5.Music without Ads")
    def like(self):
        pass
    def share(self):
        pass
    def subscribe(self):
        pass
    def comment(self):
        pass



def play_video(user,username):
    user.playvideo(username)

goutham = normaluser()
soul = premiumuser()
vishwa = normaluser()
varma = premiumuser()


play_video(goutham,"goutham")
play_video(soul,"soul")
play_video(vishwa,"vishwa")
play_video(varma,"varma")




#operator overloading
class number:
    def __init__(self,n):
        self.n = n
    
    def __add__(self,other):
        return self.n+other.n

    def __sub__(self,other):
        return self.n-other.n
    
    def __mul__(self,other):
        return self.n*other.n
    
    
    
number1 = number(10)
number2 = number(20)

print(number1+number2)
print(number1-number2)
print(number1*number2)        