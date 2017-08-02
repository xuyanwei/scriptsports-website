from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True,verbose_name='e-mail',null=True)
    def __unicode__(self):
          return self.name

class Newsleixin(models.Model):
    leixinname=models.CharField(max_length=10)
    def __unicode__(self):
          return self.leixinname

class Sportsleixin(models.Model):
    name=models.CharField(max_length=20)
    def __unicode__(self):
          return self.name

class News(models.Model):
    title=models.CharField(max_length=35)
    text=models.TextField()
    time=models.DateTimeField()
    orgin=models.CharField(max_length=20,blank=True,null=True)
    newsleixin=models.ForeignKey(Newsleixin)
    author=models.ForeignKey(Author)
    tag1=models.CharField(max_length=10,blank=True,null=True)
    tag2=models.CharField(max_length=10,blank=True,null=True)
    important=models.BooleanField()
    sportsleixin=models.ForeignKey(Sportsleixin)
    def __unicode__(self):
          return u"%s%s %s"%(self.time,self.newsleixin,self.title)

    class Meta:
        ordering=["-time"]

class Streamtvlogo(models.Model):
    name=models.CharField(max_length=10)
    src=models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s"%(self.name)

class Nation(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
          return self.name

class Career(models.Model):
    career=models.CharField(max_length=20)
    def __unicode__(self):
          return self.career

class Sponser(models.Model):
    sname=models.CharField(max_length=30)
    def __unicode__(self):
          return self.sname

class Position(models.Model):
    pos_exp=models.CharField(max_length=30)
    def __unicode__(self):
          return self.pos_exp

class Team(models.Model):
    chinese_name=models.CharField(max_length=30)
    english_name=models.CharField(max_length=30)
    nation=models.ForeignKey(Nation)
    birthday=models.DateField(blank=True,null=True)
    city=models.CharField(max_length=30)
    ground=models.CharField(max_length=40)
    clo_sponser=models.ForeignKey(Sponser,blank=True,null=True)
    website=models.URLField(blank=True,null=True)

    def __unicode__(self):
          return u"%s %s"%(self.chinese_name,self.english_name)

class Man(models.Model):
    chinese_name=models.CharField(max_length=30)
    english_name=models.CharField(max_length=20)
    career=models.ForeignKey(Career)
    birthday=models.DateField()
    nation=models.ForeignKey(Nation)
    clo_sponser=models.ForeignKey(Sponser,blank=True,null=True)
    position=models.ForeignKey(Position,blank=True,null=True)
    club=models.ForeignKey(Team)
    gamenum=models.IntegerField(blank=True,null=True)
    spleixin=models.ForeignKey(Sportsleixin)

    def __unicode__(self):
          return u"%s %s"%(self.chinese_name,self.english_name)

class Tv(models.Model):
    name=models.CharField(max_length=30)
    langunage=models.CharField(max_length=20,blank=True,null=True)
    address1=models.CharField(max_length=1000)
    address2=models.CharField(max_length=1500,blank=True,null=True)
    address3=models.CharField(max_length=1500,blank=True,null=True)
    mob_addr=models.CharField(max_length=500,blank=True,null=True)
    def __unicode__(self):
        return u"%s"%(self.name)
    class Meta:
        ordering=["id"]

class Gameleixin(models.Model):
    name=models.CharField(max_length=40)
    def __unicode__(self):
          return self.name

class Gameshow(models.Model):
    game_time=models.DateTimeField()
    game_vs=models.CharField(max_length=50)
    game_leixin=models.ForeignKey(Gameleixin)
    game_tv=models.ManyToManyField(Tv)
    sports_leixin=models.ForeignKey(Sportsleixin)
    game_important=models.BooleanField()
    def __unicode__(self):
        return u"%s %s"%(self.game_time,self.game_vs)

    class Meta:
        ordering=["game_time"]

    @property
    def gettvname(self):
        return self.game_tv.all()


class Quality(models.Model):
    qua=models.CharField(max_length=10)
    def __unicode__(self):
        return self.qua

class State(models.Model):
    state=models.CharField(max_length=20)
    def __unicode__(self):
        return self.state

class Language(models.Model):
    name=models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Count(models.Model):
    name=models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Video(models.Model):
    videotvname=models.CharField(max_length=20,blank=True,null=True)
    language=models.ForeignKey(Language)
    addr_baidu=models.URLField()
    addr_xunlei=models.URLField(blank=True,null=True)
    addr_ext_baidu=models.URLField(blank=True,null=True)
    addr_ext_xunlei=models.URLField(blank=True,null=True)
    video_size=models.CharField(max_length=20)
    quality=models.ForeignKey(Quality)
    geshi=models.CharField(max_length=10)
    vidoe_geshi=models.CharField(max_length=10)
    sound_geshi=models.CharField(max_length=10)
    def __unicode__(self):
        return u"%s %s %s"%(self.id,self.quality,self.video_size)

class Stream(models.Model):
    orginname=models.ForeignKey(Streamtvlogo)
    outside=models.BooleanField()
    language=models.ForeignKey(Language)
    quality=models.ForeignKey(Quality)
    video=models.ForeignKey(Video,blank=True,null=True)
    addr_pc_1=models.CharField(max_length=1200)
    addr_pc_2=models.CharField(max_length=1200,blank=True,null=True)
    addr_pc_extr=models.CharField(max_length=1200,blank=True,null=True)
    addr_mobi_1=models.CharField(max_length=1200)
    addr_mobi_2=models.CharField(max_length=1200,blank=True,null=True)
    addr_mobi_extr=models.CharField(max_length=1200,blank=True,null=True)

    def __unicode__(self):
        return u"%s%s%s"%(self.id,self.quality,self.language)

class Jijin(models.Model):
    outside=models.BooleanField()
    language=models.ForeignKey(Language,blank=True,null=True)
    addr_pc=models.CharField(max_length=1000)
    addr_mobi=models.CharField(max_length=1000)
    addr_ss=models.CharField(max_length=1000,blank=True,null=True)
    def __unicode__(self):
        return u"%s%s"%(self.id,self.language)

class Important(models.Model):
    important=models.CharField(max_length=180,default='*')
    def __unicode__(self):
        return self.important

class Gamebigleixin(models.Model):
    bname=models.CharField(max_length=20)
    def __unicode__(self):
        return self.bname

class Regame(models.Model):
    game_time=models.DateTimeField()
    game_leixin=models.ForeignKey(Gameleixin)
    game_leixin_count=models.ForeignKey(Count,blank=True,null=True)
    game_bigleixin=models.ForeignKey(Gamebigleixin)
    game_players=models.CharField(max_length=50)
    important=models.ForeignKey(Important)
    state=models.ForeignKey(State)
    author=models.ForeignKey(Author)
    gmsleixin=models.ForeignKey(Sportsleixin)
    jijin=models.ManyToManyField(Jijin,blank=True,null=True)
    stream=models.ManyToManyField(Stream,blank=True,null=True)
    video=models.ManyToManyField(Video,blank=True,null=True)

    def __unicode__(self):
       return u"%s%s %s"%(self.game_time,self.game_leixin,self.game_players)

    class Meta:
        ordering=["-game_time",'game_leixin']

    @property
    def rejijin(self):
        return self.jijin.filter()

    @property
    def restream(self):
        return self.stream.filter()

    @property
    def revideo(self):
        return self.video.filter()

class Sharing(models.Model):
    sname=models.CharField(max_length=40)
    title=models.CharField(max_length=80)
    address=models.CharField(max_length=1000)
    imp=models.BooleanField()
    share_time=models.DateTimeField()
    like_count=models.IntegerField(blank=True,null=True,default = 0)

    def __unicode__(self):
       return u"%s%s"%(self.sname,self.title)

    class Meta:
        ordering=["-id"]

class Talk(models.Model):
    tname=models.CharField(max_length=40)
    title=models.CharField(max_length=80)
    bbstext=models.TextField()
    ttime=models.DateTimeField()
    ttop=models.BooleanField()
    def __unicode__(self):
       return u"%s%s"%(self.tname,self.title)

    class Meta:
        ordering=["-id"]









