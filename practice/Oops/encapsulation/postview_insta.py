class Postviewer:
    def __init__(self,owner_name,private_account=False):
        self.owner_name = owner_name
        self.__private_account = private_account
        self.posts = []
        self.followers = []
     
    def add_post(self,photo_url):
        self.posts.append(photo_url)
        print(f"{self.owner_name} added a new post.")

        
    def set_privacy(self,private_status):
        self.__private_account = private_status
        if private_status:
            print(f"{self.owner_name}'s account is now private.")
        else:
            print(f"{self.owner_name}'s account is now public.")

    def follow(self,follower_name):
        if follower_name not in self.followers:
            self.followers.append(follower_name)
            print(f"{follower_name} is now following {self.owner_name}.")
        else:
            print(f"{follower_name} is already following {self.owner_name}.")
             
    def view_posts(self,viewer_name):
        if not self.__private_account or viewer_name in self.followers:
            print(f"posts by {self.owner_name}:")
            for post in self.posts:
                print(post)
        else:
            print(f"{self.owner_name}'s account is private. Follow them to view posts.")


goutham = Postviewer("Goutham",True)
goutham.add_post("python course")
goutham.add_post("flask course")
goutham.add_post("sql course")

soul = Postviewer("soul")
post = ["candid pic","professional pic"]
for i in post:
    soul.add_post(i)

soul.follow("Goutham")
goutham.follow("Soul")
goutham.set_privacy(False)
goutham.view_posts("Soul")
soul.view_posts("Goutham")

        
