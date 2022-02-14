#Attempt at hangman game
import turtle as t
import random
import time
#Writing whole program into function to easily be able to restart
def main():
  #Initializing Variables
  name = str()
  state_of_user = str()
  win = str()
  tuiq ='********** Hit 1 to quit at any time ***********'
  num = int()
  word_length = str()
  length = int()
  the_length = str()
  secret_word = str()
  guesses_left = 0
  positions = []
  stle = str()
  style = str()
  #Counter Variables to terminate loops
  leave_code_variable = 0
  variable_for_continuing_to_game = 1
  variable_to_run_game = 1
  total_guesses_alotted = 8
  #Background helper to eliminate excess background when in fullscreen
  #David 
  def bg_helper():
    t.setheading(90)
    t.penup()
    t.pencolor('light sky blue')
    t.fillcolor('light sky blue')
    t.begin_fill()
    t.pendown()
    t.forward(325)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(650)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(325)
    t.end_fill()
  #Method to draw ellipse for the tongue
  #David
  def draw():    
    # rad --> radius of arc 
    for i in range(1): 
      # two arcs 
      t.circle(4,90) 
      t.circle(4,90)
  #Method to draw ellipse for shoulders
  #David
  def draw2():
    for i in range(1):
      t.pencolor('blue2')
      t.fillcolor('blue2')
      t.begin_fill()
      t.circle(8,90)
      t.circle(24,90)
      t.end_fill()
  #Method to draw shoes
  #David
  def draw3():     
    for i in range(2):  
      t.circle(6,90) 
      t.circle(6,90)
  #Function To draw grass lines
  #Jacque
  def grass():
      t.pensize(3)
      t.pencolor('black')
      t.fillcolor('green4')
      t.begin_fill()
      t.pendown()
      t.right(90)
      t.forward(12)
      t.right(157.38)
      t.forward(13)
      t.right(112.62)
      t.forward(9)
      t.penup()
      t.forward(5)
      t.end_fill()
  #Function to draw mountains
  #Jacque
  def mountain():
      t.pensize(4)
      t.pencolor('black')
      t.fillcolor('chocolate4')
      t.begin_fill()
      t.pendown()
      t.right(90)
      t.forward(480)
      t.right(157.38)
      t.forward(520)
      t.right(112.62)
      t.forward(200)
      t.penup()
      t.end_fill()
  #Function to draw white mountain tops
  #Jacque
  def mountain_tops():
      t.pensize(3)
      t.pencolor('black')
      t.fillcolor('white')
      t.begin_fill()
      t.pendown()
      t.right(90)
      t.forward(120)
      t.right(157.38)
      t.forward(130)
      t.right(112.62)
      t.forward(50)
      t.penup()
      t.end_fill()
  #Function to draw the head
  #David
  def dead_head():
      t.setheading(180)
      t.tracer(0,0)
      t.penup()
      t.goto(20,100)
      t.right(270)
      t.pensize(3)
      t.pencolor('black')
      t.fillcolor('tan')
      t.right(90)
      t.pendown()
      t.begin_fill()
      t.circle(20)
      t.end_fill()
      t.penup()
      t.forward(10)
      t.left(90)
      t.forward(10)
      t.left(45)
      t.pendown()
      t.forward(12)
      t.right(180)
      t.right(45)
      t.penup()
      t.forward(8)
      t.left(135)
      t.pendown()
      t.forward(12)
      t.penup()
      t.left(135)
      t.forward(15)
      t.pendown()
      t.left(45)
      t.pendown()
      t.forward(12)
      t.right(180)
      t.right(45)
      t.penup()
      t.forward(8)
      t.left(135)
      t.pendown()
      t.forward(12)
      t.penup()
      t.right(45)
      t.forward(10)
      t.right(90)
      t.forward(12)
      t.pendown()
      t.forward(7)
      t.right(180)
      t.forward(14)
      t.left(180)
      t.forward(8)
      t.left(180)
      t.forward(5)
      t.left(180)
      t.forward(5)
      t.right(90)
      t.fillcolor('red')
      t.begin_fill()
      t.right(180)
      draw()
      t.end_fill()
      t.update()
  #Body function
  #David
  def dead_body():
      t.tracer(0,0)
      t.setheading(90)
      t.penup()
      t.left(180)
      t.goto(20,50)
      t.pendown()
      t.pensize(30)
      t.pencolor('tan')
      t.begin_fill()
      t.forward(60)
      t.end_fill()
      t.fillcolor('blue2')
      t.pencolor('blue2')
      t.penup()
      t.forward(15)
      t.pendown()
      t.pensize(3)
      t.begin_fill()
      t.left(90)
      t.forward(15)
      t.left(90)
      t.forward(80)
      t.left(90)
      t.forward(30)
      t.left(90)
      t.forward(80)
      t.left(90)
      t.forward(15)
      t.end_fill()
      t.penup()
      t.goto(24, 28)
      t.right(25)
      t.pendown()
      draw2()
      t.penup()
      t.goto(16, 65)
      draw2()
      t.penup()
      t.goto(19, 65)
      t.pencolor('black')
      t.pensize(4)
      t.fillcolor('DarkKhaki')
      t.pendown()
      t.begin_fill()
      t.left(25)
      t.forward(12.5)
      t.right(90)
      t.forward(6)
      t.right(90)
      t.forward(25)
      t.right(90)
      t.forward(6)
      t.right(90)
      t.forward(12.5)
      t.end_fill()
      t.penup()
      t.goto(15, 60)
      rope_lines()
      t.goto(22, 60)
      rope_lines()
      t.goto(29, 60)
      rope_lines()
      t.goto(5, 60)
      t.setheading(0)
      t.pensize(4)
      t.pendown()
      t.right(90)
      t.forward(90)
      t.penup()
      t.goto(5, -30)
      t.left(90)
      t.pendown()
      t.forward(30)
      t.left(90)
      t.forward(90)
      t.update()
  #Left arm function
  #David
  def dead_right_arm():
      t.penup()
      t.goto(35, 25)
      t.setheading(272)
      t.tracer(0,0)
      t.pendown()
      t.begin_fill()
      t.pensize(3)
      t.pencolor('black')
      t.fillcolor('tan')
      t.forward(45)
      for i in range(1): 
      # two arcs 
        t.circle(2,90) 
        t.circle(2,90)
      t.forward(10)
      t.left(90)
      t.forward(1)
      t.left(90)
      t.forward(15)
      for i in range(1): 
      # two arcs 
        t.circle(3,90) 
        t.circle(3,90)
      t.right(6)
      t.forward(15)
      t.left(7)
      t.forward(40)
      t.left(90)
      t.forward(7)
      t.end_fill()
      t.update()
  #Right arm function
  #David
  def dead_left_arm():
      t.penup()
      t.goto(5, 25)
      t.setheading(267)
      t.tracer(0,0)
      t.pendown()
      t.begin_fill()
      t.pensize(3)
      t.pencolor('black')
      t.fillcolor('tan')
      t.forward(45)
      for i in range(1): 
      # two arcs 
        t.circle(-2,90) 
        t.circle(-2,90)
      t.forward(10)
      t.right(90)
      t.forward(1)
      t.right(90)
      t.forward(15)
      for i in range(1): 
      # two arcs 
        t.circle(-3,90) 
        t.circle(-3,90)
      t.left(6)
      t.forward(15)
      t.right(7)
      t.forward(40)
      t.right(90)
      t.forward(7)
      t.end_fill()
      t.update()
  #Left leg function
  #David
  def dead_left_leg():
      t.tracer(0,0)
      t.penup()
      t.goto(5, -100)
      t.pencolor('black')
      t.fillcolor('black')
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.goto(8, -100)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.setheading(0)
      t.penup()
      t.setheading(180)
      t.penup()
      t.goto(6, -90)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.goto(0, -90)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.setheading(0)
      t.goto(20,-30)
      t.pencolor('black')
      t.fillcolor('grey')
      t.pendown()
      t.begin_fill()
      t.right(96)
      t.forward(60)
      t.right(80)
      t.forward(9)
      t.right(94)
      t.forward(60)
      t.right(90)
      t.forward(20)
      t.end_fill()
      t.penup()
      t.update()
  #Right leg function
  #David
  def dead_right_leg():
      t.tracer(0,0)
      t.penup()
      t.goto(30, -100)
      t.pencolor('black')
      t.fillcolor('black')
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.goto(33, -100)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.setheading(180)
      t.penup()
      t.goto(42, -93)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.goto(38, -91)
      t.begin_fill()
      draw3()
      t.end_fill()
      t.penup()
      t.goto(20,-30)
      t.pencolor('black')
      t.fillcolor('grey')
      t.pendown()
      t.begin_fill()
      t.left(96)
      t.forward(60)
      t.left(80)
      t.forward(9)
      t.left(94)
      t.forward(60)
      t.left(90)
      t.forward(20)
      t.end_fill()
      t.penup()
      t.update()
  #David
  def right_shirt():
      t.pensize(3)
      t.penup()
      t.goto(35, 30)
      t.setheading(180)
      t.pencolor('black')
      t.fillcolor('blue2')
      t.begin_fill()
      t.pendown()
      t.right(90)
      t.forward(30)
      t.right(157.38)
      t.forward(35)
      t.right(112.62)
      t.forward(15)
      t.penup()
      t.forward(5)
      t.end_fill()
  #David
  def left_shirt():
      t.pensize(3)
      t.penup()
      t.goto(4, 30)
      t.setheading(0)
      t.pencolor('black')
      t.fillcolor('blue2')
      t.begin_fill()
      t.pendown()
      t.left(90)
      t.forward(30)
      t.left(157.38)
      t.forward(35)
      t.left(112.62)
      t.forward(15)
      t.penup()
      t.forward(5)
      t.end_fill()
  # Lines on screen function
  # David
  def lines():
      t.setheading(0)
      t.penup()
      t.goto(-5,-333)
      t.pencolor('white')
      t.fillcolor('white')
      t.begin_fill()
      t.pendown()
      t.forward(333.5)
      t.left(90)
      t.forward(135)
      t.left(90)
      t.forward(665)
      t.left(90)
      t.forward(135)
      t.left(90)
      t.forward(333.5)
      t.end_fill()
      t.penup()
      t.pencolor('black')
      t.goto(0,-300)
      t.pendown()
      t.write(' '.join(the_length), font=style, align="center")
      t.penup()
      t.goto(-270, -270)
      t.pendown()
      stle = ('Times', 20, 'normal')
      t.write('Wrong \nAnswers:', font=stle, align ="center")
      t.penup()
      t.goto(-270, -310)
      t.pendown()
      t.write(num_guesses, font=stle, align="center")
      t.penup()
  #Quit function
  #Brandon
  def quit():
      print('Are you sure you would like to quit? (Y/N ONLY): ')
      leave = str(input())
      if leave == 'Y':
          print("Okay, well thank you for playing feel free to come back!")
          variable_to_run_game = 0
          win = 'q'
          guesses_left = 20
          return win
      elif leave == 'N':
          print('Okay lets continue!')
          return 2
      else:
          print('I didn\'t quite get that.')
  #Split function
  #Brandon
  def split(the_length): 
      return [char for char in the_length]
  #Rope lines
  #Jacque
  def rope_lines():
      t.penup()
      t.setheading(135)
      t.pendown()
      t.pencolor('black')
      t.pensize(3)
      t.forward(6)
      t.penup()

  #t Movements
  t.reset()
  t.tracer(0,0)
  t.hideturtle()
  wn = t.Screen()
  wn.bgcolor("light sky blue")
  wn.setup(width=700, height=700)
  t.penup()
  #Drawing Mountains for background
  t.goto(-150, 200)
  t.pencolor('black')
  t.pensize(100)
  t.right(45)
  mountain()
  t.forward(100)
  t.left(90)
  t.forward(20)
  t.right(90)
  mountain()
  t.left(90)
  t.forward(150)
  mountain()
  t.left(135)
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.right(45)
  t.right(180)
  mountain()
  t.goto(250, 250)
  mountain()
  t.goto(150, 150)
  mountain()
  t.goto(300, 100)
  mountain()
  t.goto(-340, 80)
  mountain()
  t.goto(-210, 100)
  mountain()
  t.goto(0,0)
  mountain()
  t.goto(-130,90)
  mountain()
  t.goto(-260, 310)
  t.right(90)
  mountain_tops()
  t.right(270)
  t.goto(-172, 250)
  t.right(90)
  mountain_tops()
  t.right(270)
  t.goto(-50, 190)
  t.right(90)
  mountain_tops()
  t.right(270)
  t.goto(40, 250)
  mountain_tops()
  t.goto(250, 250)
  mountain_tops()
  t.goto(150, 150)
  mountain_tops()
  t.goto(300, 100)
  mountain_tops()
  t.goto(-130, 90)
  t.right(90)
  mountain_tops()
  t.right(270)
  t.goto(-209, 100)
  t.right(90)
  mountain_tops()
  t.right(270)
  t.goto(0,0)
  t.pencolor('green4')
  t.fillcolor('green4')
  t.pendown()
  t.left(45)
  #Drawing Grass for Background
  t.begin_fill()
  t.right(180)
  t.right(90)
  t.forward(350)
  t.left(90)
  t.forward(350)
  t.left(90)
  t.forward(700)
  t.left(90)
  t.forward(350)
  t.left(90)
  t.forward(350)
  t.end_fill()
  #Moving to make grass blades
  t.penup()
  t.right(180)
  t.forward(350)
  t.right(180)
  t.pendown()
  #Drawing Grass Blades
  m = 1
  while m != 80:
    grass()
    m += 1
  t.penup()
  t.goto(150,-70)
  t.pendown()
  grass()
  grass()
  grass()
  #End of grass blades
  t.pencolor('black')
  t.penup()
  #Border   Looking Down
  t.setheading(180)
  t.goto(-3,-350)
  t.pensize(30)
  t.pendown()
  t.forward(350)
  t.right(90)
  t.forward(700)
  t.right(90)
  t.forward(700)
  t.right(90)
  t.forward(700)
  t.right(90)
  t.forward(700)
  t.penup()
  #End Border
  t.goto(20, 250)
  t.pendown()
  t.write("Game developed by: David Hare III")
  t.penup()
  t.goto(0,0)
  t.pendown()
  wn.tracer(0)
  t.penup()
  t.goto(0,250)
  t.pendown()
  t.pencolor('black')
  style = ('Courier', 60, 'bold')
  t.write("H A N G M A N", font=style, align='center')
  t.penup()
  t.pensize(12)
  t.goto(350,-193)
  t.setheading(180)
  t.pendown()
  t.forward(700)
  t.penup()
  #The hanging tower of death   looking to the left
  t.setheading(180)
  t.goto(0,0)
  t.right(180)
  t.pencolor('black')
  t.pensize(30)
  t.right(90)
  t.forward(150)
  t.right(90)
  t.forward(100)
  t.pendown()
  t.forward(150)
  t.right(180)
  t.forward(300)
  t.right(180)
  t.forward(180)
  t.right(90)
  t.pensize(20)
  t.forward(350)
  t.right(90)
  t.pensize(20)
  t.forward(150)
  t.pensize(3)
  t.fillcolor('DarkKhaki')
  t.penup()
  t.forward(3)
  t.right(90)
  t.forward(6)
  t.pendown()
  t.begin_fill()
  t.right(90)
  t.forward(2)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(4)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(2)
  t.end_fill()
  t.penup()
  t.goto(25, 180)
  rope_lines()
  t.goto(25, 170)
  rope_lines()
  t.goto(25, 160)
  rope_lines()
  t.goto(25, 150)
  rope_lines()
  t.goto(25, 140)
  rope_lines()
  t.goto(25, 130)
  rope_lines()
  t.goto(25, 120)
  rope_lines()
  t.goto(25, 110)
  rope_lines()
  t.goto(25, 100)
  rope_lines()
  #End of Death Tower
  t.goto(-370,0)
  t.pendown()
  bg_helper()
  t.goto(-400,0)
  bg_helper()
  t.penup()
  t.goto(463,0)
  bg_helper()
  t.goto(560,0)
  bg_helper()
  t.goto(650,0)
  bg_helper()
  t.update()
  #Hangman list
  hangman = ['ability','able','about','above','accept','according','account','across','act','action','activity','actually','add','address','administration','admit','adult','affect','after','again','against','age','agency','agent','ago','agree','agreement','ahead','air','all','allow','almost','alone','along','already','also','although','always','American','among','amount','analysis','and','animal','another','answer','any','anyone','anything','appear','apply','approach','area','argue','arm','around','arrive','art','article','artist','as','ask','assume','at','attack','attention','attorney','audience','author','authority','available','avoid','away','baby','back','bad','bag','ball','bank','bar','base','be','beat','beautiful','because','become','bed','before','begin','behavior','behind','believe','benefit','best','better','between','beyond','big','bill','billion','bit','black','blood','blue','board','body','book','born','both','box','boy','break','bring','brother','budget','build','building','business','but','buy','by','call','camera','campaign','can','cancer','candidate','capital','car','card','care','career','carry','case','catch','cause','cell','center','central','century','certain','certainly','chair','challenge','chance','change','character','charge','check','child','choice','choose','church','citizen','city','civil','claim','class','clear','clearly','close','coach','cold','collection','college','color','come','commercial','common','community','company','compare','computer','concern','condition','conference','Congress','consider','consumer','contain','continue','control','cost','could','country','couple','course','court','cover','create','crime','cultural','culture','cup','current','customer','cut','dark','data','daughter','day','dead','deal','death','debate','decade','decide','decision','deep','defense','degree','Democrat','democratic','describe','design','despite','detail','determine','develop','development','die','difference','different','difficult','dinner','direction','director','discover','discuss','discussion','disease','do','doctor','dog','door','down','draw','dream','drive','drop','drug','during','each','early','east','easy','eat','economic','economy','edge','education','effect','effort','eight','either','election','else','employee','end','energy','enjoy','enough','enter','entire','environment','environmental','especially','establish','even','evening','event','ever','every','everybody','everyone','everything','evidence','exactly','example','executive','exist','expect','experience','expert','explain','eye','face','fact','factor','fail','fall','family','far','fast','father','fear','federal','feel','feeling','few','field','fight','figure','fill','film','final','finally','financial','find','fine','finger','finish','fire','firm','first','fish','five','floor','fly','focus','follow','food','foot','for','force','foreign','forget','form','former','forward','four','free','friend','from','front','full','fund','future','game','garden','gas','general','generation','get','girl','give','glass','go','goal','good','government','great','green','ground','group','grow','growth','guess','gun','guy','hair','half','hand','hang','happen','happy','hard','have','he','head','health','hear','heart','heat','heavy','help','her','here','herself','high','him','himself','his','history','hit','hold','home','hope','hospital','hot','hotel','hour','house','how','however','huge','human','hundred','husband','I','idea','identify','if','image','imagine','impact','important','improve','in','include','including','increase','indeed','indicate','individual','industry','information','inside','instead','institution','interest','interesting','international','interview','into','investment','involve','issue','it','item','its','itself','job','join','just','keep','key','kid','kill','kind','kitchen','know','knowledge','land','language','large','last','late','later','laugh','law','lawyer','lay','lead','leader','learn','least','leave','left','leg','legal','less','let','letter','level','lie','life','light','like','likely','line','list','listen','little','live','local','long','look','lose','loss','lot','love','low','machine','magazine','main','maintain','major','majority','make','man','manage','management','manager','many','market','marriage','material','matter','may','maybe','me','mean','measure','media','medical','meet','meeting','member','memory','mention','message','method','middle','might','military','million','mind','minute','miss','mission','model','modern','moment','money','month','more','morning','most','mother','mouth','move','movement','movie','Mr','Mrs','much','music','must','my','myself','name','nation','national','natural','nature','near','nearly','necessary','need','network','never','new','news','newspaper','next','nice','night','no','none','nor','north','not','note','nothing','notice','now','number','occur','of','off','offer','office','officer','official','often','oh','oil','ok','old','on','once','one','only','onto','open','operation','opportunity','option','or','order','organization','other','others','our','out','outside','over','own','owner','page','pain','painting','paper','parent','part','participant','particular','particularly','partner','party','pass','past','patient','pattern','pay','peace','people','per','perform','performance','perhaps','period','person','personal','phone','physical','pick','picture','piece','place','plan','plant','play','player','PM','point','police','policy','political','politics','poor','popular','population','position','positive','possible','power','practice','prepare','present','president','pressure','pretty','prevent','price','private','probably','problem','process','produce','product','production','professional','professor','program','project','property','protect','prove','provide','public','pull','purpose','push','put','quality','question','quickly','quite','race','radio','raise','range','rate','rather','reach','read','ready','real','reality','realize','really','reason','receive','recent','recently','recognize','record','red','reduce','reflect','region','relate','relationship','religious','remain','remember','remove','report','represent','Republican','require','research','resource','respond','response','responsibility','rest','result','return','reveal','rich','right','rise','risk','road','rock','role','room','rule','run','safe','same','save','say','scene','school','science','scientist','score','sea','season','seat','second','section','security','see','seek','seem','sell','send','senior','sense','series','serious','serve','service','set','seven','several','sex','sexual','shake','share','she','shoot','short','shot','should','shoulder','show','side','sign','significant','similar','simple','simply','since','sing','single','sister','sit','site','situation','six','size','skill','skin','small','smile','so','social','society','soldier','some','somebody','someone','something','sometimes','son','song','soon','sort','sound','source','south','southern','space','speak','special','specific','speech','spend','sport','spring','staff','stage','stand','standard','star','start','state_of_user','statement','station','stay','step','still','stock','stop','store','story','strategy','street','strong','structure','student','study','stuff','style','subject','success','successful','such','suddenly','suffer','suggest','summer','support','sure','surface','system','table','take','talk','task','tax','teach','teacher','team','technology','television','tell','ten','tend','term','test','than','thank','that','the','their','them','themselves','then','theory','there','these','they','thing','think','third','this','those','though','thought','thousand','threat','three','through','throughout','throw','thus','time','to','today','together','tonight','too','top','total','tough','toward','town','trade','traditional','training','travel','treat','treatment','tree','trial','trip','trouble','true','truth','try','turn','TV','two','type','under','understand','unit','until','up','upon','us','use','usually','value','various','very','victim','view','violence','visit','voice','vote','wait','walk','wall','want','war','watch','water','way','we','weapon','wear','week','weight','well','west','western','what','whatever','when','where','whether','which','while','white','who','whole','whom','whose','why','wide','wife','will','win','wind','window','wish','with','within','without','woman','wonder','word','work','worker','world','worry','would','write','writer','wrong','yard','yeah','year','yes','yet','you','young','your','yourself']
  #Introduction lists###################################################################################################################################################################################################################################################################
  good_states = ['good', 'Good', 'great', 'Great', 'excellent', 'Excellent', 'Amazing', 'amazing', 'fantastic', 'wonderful', 'pretty good', 'Fantastic', 'dope', 'chill']
  bad_states = ['bad', 'Bad', 'terrible', 'Terrible', 'shit', 'Shit', 'shitty', 'Shitty', 'awful', 'Awful', 'the worst', 'sucky', 'suck']
  meh_states = ['okay', 'Okay', 'alright', 'Alright', 'meh', 'Meh', 'pretty okay', 'eh', 'Eh']

  yes = ['yes', 'Yeah', 'yeah', 'Yes', 'sure', 'okay', 'I\'m ready', 'i\'m ready', 'Yass', 'yass','y', 'Y']
  no = ['no', 'No', 'Naw', 'naw', 'nope', 'Nope', 'n', 'N']
  numbers = ['0' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' ,'11' ,'12' ,'13' ,'14' ,'15' ,'16' ,'17' ,'18' ,'19' ,'20' ,'21' ,'22' ,'23' ,'24' ,'25' ,'26' ,'27' ,'28' ,'29' ,'30' ,'31' ,'32' ,'33' ,'34' ,'35' ,'36' ,'37' ,'38' ,'39' ,'40' ,'41' ,'42' ,'43' ,'44' ,'45' ,'46' ,'47' ,'48' ,'49' ,'50' ,'51' ,'52' ,'53' ,'54' ,'55' ,'56' ,'57' ,'58' ,'59' ,'60' ,'61' ,'62' ,'63' ,'64' ,'65' ,'66' ,'67' ,'68' ,'69' ,'70' ,'71' ,'72' ,'73' ,'74' ,'75' ,'76' ,'77' ,'78' ,'79' ,'80' ,'81' ,'82' ,'83' ,'84' ,'85' ,'86' ,'87' ,'88' ,'89' ,'90' ,'91' ,'92' ,'93' ,'94' ,'95' ,'96' ,'97' ,'98' ,'99' ,'100' ,'101' ,'102' ,'103' ,'104' ,'105' ,'106' ,'107' ,'108' ,'109' ,'110' ,'111' ,'112' ,'113' ,'114' ,'115' ,'116' ,'117' ,'118' ,'119' ,'120' ,'121' ,'122' ,'123' ,'124' ,'125' ,'126' ,'127' ,'128' ,'129' ,'130' ,'131' ,'132' ,'133' ,'134' ,'135' ,'136' ,'137' ,'138' ,'139' ,'140' ,'141' ,'142' ,'143' ,'144' ,'145' ,'146' ,'147' ,'148' ,'149' ,'150' ,'151' ,'152' ,'153' ,'154' ,'155' ,'156' ,'157' ,'158' ,'159' ,'160' ,'161' ,'162' ,'163' ,'164' ,'165' ,'166' ,'167' ,'168' ,'169' ,'170' ,'171' ,'172' ,'173' ,'174' ,'175' ,'176' ,'177' ,'178' ,'179' ,'180' ,'181' ,'182' ,'183' ,'184' ,'185' ,'186' ,'187' ,'188' ,'189' ,'190' ,'191' ,'192' ,'193' ,'194' ,'195' ,'196' ,'197' ,'198' ,'199' ,'200' ,'201' ,'202' ,'203' ,'204' ,'205' ,'206' ,'207' ,'208' ,'209' ,'210' ,'211' ,'212' ,'213' ,'214' ,'215' ,'216' ,'217' ,'218' ,'219' ,'220' ,'221' ,'222' ,'223' ,'224' ,'225' ,'226' ,'227' ,'228' ,'229' ,'230' ,'231' ,'232' ,'233' ,'234' ,'235' ,'236' ,'237' ,'238' ,'239' ,'240' ,'241' ,'242' ,'243' ,'244' ,'245' ,'246' ,'247' ,'248' ,'249' ,'250' ,'251' ,'252' ,'253' ,'254' ,'255' ,'256' ,'257' ,'258' ,'259' ,'260' ,'261' ,'262' ,'263' ,'264' ,'265' ,'266' ,'267' ,'268' ,'269' ,'270' ,'271' ,'272' ,'273' ,'274' ,'275' ,'276' ,'277' ,'278' ,'279' ,'280' ,'281' ,'282' ,'283' ,'284' ,'285' ,'286' ,'287' ,'288' ,'289' ,'290' ,'291' ,'292' ,'293' ,'294' ,'295' ,'296' ,'297' ,'298' ,'299' ,'300' ,'301' ,'302' ,'303' ,'304' ,'305' ,'306' ,'307' ,'308' ,'309' ,'310' ,'311' ,'312' ,'313' ,'314' ,'315' ,'316' ,'317' ,'318' ,'319' ,'320' ,'321' ,'322' ,'323' ,'324' ,'325' ,'326' ,'327' ,'328' ,'329' ,'330' ,'331' ,'332' ,'333' ,'334' ,'335' ,'336' ,'337' ,'338' ,'339' ,'340' ,'341' ,'342' ,'343' ,'344' ,'345' ,'346' ,'347' ,'348' ,'349' ,'350' ,'351' ,'352' ,'353' ,'354' ,'355' ,'356' ,'357' ,'358' ,'359' ,'360' ,'361' ,'362' ,'363' ,'364' ,'365' ,'366' ,'367' ,'368' ,'369' ,'370' ,'371' ,'372' ,'373' ,'374' ,'375' ,'376' ,'377' ,'378' ,'379' ,'380' ,'381' ,'382' ,'383' ,'384' ,'385' ,'386' ,'387' ,'388' ,'389' ,'390' ,'391' ,'392' ,'393' ,'394' ,'395' ,'396' ,'397' ,'398' ,'399' ,'400' ,'401' ,'402' ,'403' ,'404' ,'405' ,'406' ,'407' ,'408' ,'409' ,'410' ,'411' ,'412' ,'413' ,'414' ,'415' ,'416' ,'417' ,'418' ,'419' ,'420' ,'421' ,'422' ,'423' ,'424' ,'425' ,'426' ,'427' ,'428' ,'429' ,'430' ,'431' ,'432' ,'433' ,'434' ,'435' ,'436' ,'437' ,'438' ,'439' ,'440' ,'441' ,'442' ,'443' ,'444' ,'445' ,'446' ,'447' ,'448' ,'449' ,'450' ,'451' ,'452' ,'453' ,'454' ,'455' ,'456' ,'457' ,'458' ,'459' ,'460' ,'461' ,'462' ,'463' ,'464' ,'465' ,'466' ,'467' ,'468' ,'469' ,'470' ,'471' ,'472' ,'473' ,'474' ,'475' ,'476' ,'477' ,'478' ,'479' ,'480' ,'481' ,'482' ,'483' ,'484' ,'485' ,'486' ,'487' ,'488' ,'489' ,'490' ,'491' ,'492' ,'493' ,'494' ,'495' ,'496' ,'497' ,'498' ,'499' ,'500' ,'501' ,'502' ,'503' ,'504' ,'505' ,'506' ,'507' ,'508' ,'509' ,'510' ,'511' ,'512' ,'513' ,'514' ,'515' ,'516' ,'517' ,'518' ,'519' ,'520' ,'521' ,'522' ,'523' ,'524' ,'525' ,'526' ,'527' ,'528' ,'529' ,'530' ,'531' ,'532' ,'533' ,'534' ,'535' ,'536' ,'537' ,'538' ,'539' ,'540' ,'541' ,'542' ,'543' ,'544' ,'545' ,'546' ,'547' ,'548' ,'549' ,'550' ,'551' ,'552' ,'553' ,'554' ,'555' ,'556' ,'557' ,'558' ,'559' ,'560' ,'561' ,'562' ,'563' ,'564' ,'565' ,'566' ,'567' ,'568' ,'569' ,'570' ,'571' ,'572' ,'573' ,'574' ,'575' ,'576' ,'577' ,'578' ,'579' ,'580' ,'581' ,'582' ,'583' ,'584' ,'585' ,'586' ,'587' ,'588' ,'589' ,'590' ,'591' ,'592' ,'593' ,'594' ,'595' ,'596' ,'597' ,'598' ,'599' ,'600' ,'601' ,'602' ,'603' ,'604' ,'605' ,'606' ,'607' ,'608' ,'609' ,'610' ,'611' ,'612' ,'613' ,'614' ,'615' ,'616' ,'617' ,'618' ,'619' ,'620' ,'621' ,'622' ,'623' ,'624' ,'625' ,'626' ,'627' ,'628' ,'629' ,'630' ,'631' ,'632' ,'633' ,'634' ,'635' ,'636' ,'637' ,'638' ,'639' ,'640' ,'641' ,'642' ,'643' ,'644' ,'645' ,'646' ,'647' ,'648' ,'649' ,'650' ,'651' ,'652' ,'653' ,'654' ,'655' ,'656' ,'657' ,'658' ,'659' ,'660' ,'661' ,'662' ,'663' ,'664' ,'665' ,'666' ,'667' ,'668' ,'669' ,'670' ,'671' ,'672' ,'673' ,'674' ,'675' ,'676' ,'677' ,'678' ,'679' ,'680' ,'681' ,'682' ,'683' ,'684' ,'685' ,'686' ,'687' ,'688' ,'689' ,'690' ,'691' ,'692' ,'693' ,'694' ,'695' ,'696' ,'697' ,'698' ,'699' ,'700' ,'701' ,'702' ,'703' ,'704' ,'705' ,'706' ,'707' ,'708' ,'709' ,'710' ,'711' ,'712' ,'713' ,'714' ,'715' ,'716' ,'717' ,'718' ,'719' ,'720' ,'721' ,'722' ,'723' ,'724' ,'725' ,'726' ,'727' ,'728' ,'729' ,'730' ,'731' ,'732' ,'733' ,'734' ,'735' ,'736' ,'737' ,'738' ,'739' ,'740' ,'741' ,'742' ,'743' ,'744' ,'745' ,'746' ,'747' ,'748' ,'749' ,'750' ,'751' ,'752' ,'753' ,'754' ,'755' ,'756' ,'757' ,'758' ,'759' ,'760' ,'761' ,'762' ,'763' ,'764' ,'765' ,'766' ,'767' ,'768' ,'769' ,'770' ,'771' ,'772' ,'773' ,'774' ,'775' ,'776' ,'777' ,'778' ,'779' ,'780' ,'781' ,'782' ,'783' ,'784' ,'785' ,'786' ,'787' ,'788' ,'789' ,'790' ,'791' ,'792' ,'793' ,'794' ,'795' ,'796' ,'797' ,'798' ,'799' ,'800' ,'801' ,'802' ,'803' ,'804' ,'805' ,'806' ,'807' ,'808' ,'809' ,'810' ,'811' ,'812' ,'813' ,'814' ,'815' ,'816' ,'817' ,'818' ,'819' ,'820' ,'821' ,'822' ,'823' ,'824' ,'825' ,'826' ,'827' ,'828' ,'829' ,'830' ,'831' ,'832' ,'833' ,'834' ,'835' ,'836' ,'837' ,'838' ,'839' ,'840' ,'841' ,'842' ,'843' ,'844' ,'845' ,'846' ,'847' ,'848' ,'849' ,'850' ,'851' ,'852' ,'853' ,'854' ,'855' ,'856' ,'857' ,'858' ,'859' ,'860' ,'861' ,'862' ,'863' ,'864' ,'865' ,'866' ,'867' ,'868' ,'869' ,'870' ,'871' ,'872' ,'873' ,'874' ,'875' ,'876' ,'877' ,'878' ,'879' ,'880' ,'881' ,'882' ,'883' ,'884' ,'885' ,'886' ,'887' ,'888' ,'889' ,'890' ,'891' ,'892' ,'893' ,'894' ,'895' ,'896' ,'897' ,'898' ,'899' ,'900' ,'901' ,'902' ,'903' ,'904' ,'905' ,'906' ,'907' ,'908' ,'909' ,'910' ,'911' ,'912' ,'913' ,'914' ,'915' ,'916' ,'917' ,'918' ,'919' ,'920' ,'921' ,'922' ,'923' ,'924' ,'925' ,'926' ,'927' ,'928' ,'929' ,'930' ,'931' ,'932' ,'933' ,'934' ,'935' ,'936' ,'937' ,'938' ,'939' ,'940' ,'941' ,'942' ,'943' ,'944' ,'945' ,'946' ,'947' ,'948' ,'949' ,'950' ,'951' ,'952' ,'953' ,'954' ,'955' ,'956' ,'957' ,'958' ,'959' ,'960' ,'961' ,'962' ,'963' ,'964' ,'965' ,'966' ,'967' ,'968' ,'969' ,'970' ,'971' ,'972' ,'973' ,'974' ,'975' ,'976' ,'977' ,'978' ,'979' ,'980' ,'981' ,'982' ,'983' ,'984' ,'985' ,'986' ,'987' ,'988' ,'989' ,'990' ,'991' ,'992' ,'993' ,'994' ,'995' ,'996' ,'997' ,'998' ,'999' ,'1000'] 
  #Introduction#########################################################################################################################################################################################################################################################################
  #Quit menu dictionary
  quit_menu = ['1', 'lemme out', 'Let me out', 'Lemme out', 'lemme Out', 'Lemme Out', 'let Me out', 'let me Out', 'Let me Out', 'Let Me Out', 'let Me Out']
  #Invalid input dictionary
  invalid = ['\n', '\t', '\\', ',', '\ESC', ' ', '', '?', ':', ';', '>', '<', '/', '%', '^', '&', '*', '(', ')', '=', '+', '$', '#', '@', '!', '-', '_', '[', ']', '{', '}', '|', '~', '`', '\'', '"', 'str()', 'int()', '.']
  #Telling User about quit option
  print(tuiq)
  #Detrmining size and writing letters
  ############################David#####################################
  if length <= 5:
    style = ('Times', 60, 'normal')
  elif (length > 5) and (length <= 10):
    style = ('Times', 30, 'normal')
  elif (length > 10) and (length <=15):
    style = ('Times', 20, 'normal')
  elif length > 15:
    style = ('Times', 10, 'normal')
  t.penup()
  t.pencolor('black')
  t.goto(200,-300)
  t.pendown()
  t.write(' '.join(the_length), font=style, align="center")

  #While statement for the game
  #Brandon
  while variable_to_run_game == 1:
    name = str(input('Hello, welcome to Hangman!\nLets start by getting your name: '))
    if name == '1':
      quit_variable = quit()
      if quit_variable == 2:
        continue
      elif quit_variable == 'q':
        win = 'q'
        variable_to_run_game = 0
        return 'q'
      else:
        quit()
    else:
      while leave_code_variable != 1:
          state_of_user = str(input('Hi ' + name + ', how are you doing today?: '))
          #Introduction if statement############################################################################################################################################################################################################################################################
          #Brandon
          if state_of_user in good_states:
              print('Well I\'m glad you\'re doing', state_of_user + '.')
              print('Lets get started!')
              break
          elif state_of_user in bad_states:
              print('Well I\'m sorry you are feeling', state_of_user + '.')
              print('Lets try and get started.')
              break
          elif state_of_user in meh_states:
              print('Well that\'s nice.')
              print('Lets get started I guess.')
              break
          elif state_of_user in quit_menu:
              print('Are you sure you would like to quit? (Y/N ONLY): ')
              leave = str(input())
              if leave == 'Y':
                  print("Okay, well thank you for playing feel free to come back!")
                  leave_code_variable = 1
                  variable_to_run_game = 0
                  variable_for_continuing_to_game = 0
                  guesses_left = 6
                  win = 'q'
                  return 'q'
              elif leave == 'N':
                  print('Okay lets continue ' + name + '!')
                  break
              else:
                  print('I didn\'t quite get that.')
          else:
              print('I don\'t quite understand that.')
            
  #Print statment to open the other tab
  #Brandon
      while variable_for_continuing_to_game != 0:
          ready = str(input('Are you ready to continue?: '))
          if ready in yes:
              print('Great lets do it '+ name +'\n')
              break
          elif ready in numbers:
              print('That is a number, I need you to tell me if you\'re ready to continue')
          elif ready in no:
              print('Okay well I\'m gonna wait until you are. :/')
          elif ready in quit_menu:
              if quit() == 2:
                  continue
              else:
                  return 'q'
                  break
          else:
              print('I\'m sorry I didn\'t understand that.')
  #Hangman code
  #Brandon
      already_guessed = []
      already_guessed_right = []
      if guesses_left == 0:
          print('*Make sure you open the other tab with the visual output.*')
          num = random.randint(0,999)
          secret_word = hangman[num]
          length = len(secret_word)
          the_length = ('_' * length )
          the_length = split(the_length)
          while guesses_left <= 8:
              num_guesses = total_guesses_alotted - guesses_left
              if num_guesses == 1:
                  word_length = print('\nThe secret word is',length,'characters long.\n\nYou have', total_guesses_alotted - guesses_left,'more wrong answer allowed. Make it count.')
              else:
                  word_length = print('\nThe secret word is',length,'characters long.\n\nYou have', total_guesses_alotted - guesses_left,'wrong answers allowed.')
              word_length
              print(' '.join(the_length))
              lines()
              if list(secret_word) == the_length:
                  print('Congratulations, you have won!')
                  variable_to_run_game = 0
                  win = 'W'
                  break
              else:
                  print('These characters have already been guessed and were wrong:', ', '.join(already_guessed))
                  print('These characters have already been guessed and are corrct:', ', '.join(already_guessed_right))
                  guess = str(input('Please enter a guess(can be lowercase letter or whole word guess): '))
                  if guess in already_guessed:
                          print('\nYou already guessed this letter.\n')
                  elif (len(guess) < len(secret_word)) and (len(guess) > 1):
                      print('\nThat is not a valid length')
                  elif guess in invalid:
                      print('\nThat is not a valid operation')
                  elif len(guess) > len(secret_word):
                      print('\nThat is not a valid guess')
                  elif guess in numbers:
                      print('\nThat is a number, we are playing hangman')
                  elif guess in quit_menu:
                      print('\nAre you sure you would like to quit? (Y/N ONLY): ')
                      leave = str(input())
                      if leave == 'Y':
                          print("Okay, well thank you for playing feel free to come back!")
                          variable_to_run_game = 0
                          guesses_left = 6
                          win = 'q'
                          break
                      elif leave == 'N':
                          print('Okay lets continue!')
                      else:
                          print('I didn\'t quite get that.')
                  elif guess == secret_word:
                      print('\n' +name +', you Guessed the whole word, ' + secret_word + '. Good Job! Gotta admit I\'m impressed.\n')
                      variable_to_run_game = 0
                      win = 'W'
                      break
                  elif guess in already_guessed_right:
                      print('\nYou already guessed this and it was right')
                  elif guess in secret_word:
                      print('\nYes, ' + guess +' that was in the word!')
                      already_guessed_right.append(guess)
                      index = (secret_word.find(guess))
                      index2 = (secret_word.find(guess, index + 1, 20))
                      index3 = (secret_word.find(guess, index2 + 1, 20))
                      index4 = (secret_word.find(guess, index3 + 1, 20))
                      for i in range(len(the_length)):
                          if i == index:
                              the_length[i] = guess
                          elif i == index2:
                              the_length[i] = guess
                          elif i == index3:
                              the_length[i] = guess
                          elif i == index4:
                              the_length[i] = guess
                          else:
                              continue                         
                  elif guess not in secret_word:
                      guesses_left += 1
                      already_guessed.append(guess)
                      print('\nNo, ' + guess +' was not in the word')
                      if guesses_left == 1:
                          dead_head()
                      elif guesses_left == 2:
                          dead_body()
                      elif guesses_left == 3:
                          right_shirt()
                      elif guesses_left == 4:
                          left_shirt()
                      elif guesses_left == 5:
                          dead_right_arm()
                      elif guesses_left == 6:
                          dead_left_arm()
                      elif guesses_left == 7:
                          dead_right_leg()
                      elif guesses_left == 8:
                          dead_left_leg()
                          print('\nThe secret word is ' + secret_word + '.')
                          print("You lost :( Maybe next time.\n")
                          variable_to_run_game = 0
                          win = 'L'
                          break
                  elif guess in already_guessed:
                      print('You already guessed this letter.')
          t.setheading(0)
          t.penup()
          t.goto(-5,-333)
          t.pencolor('white')
          t.fillcolor('white')
          t.begin_fill()
          t.pendown()
          t.forward(333.5)
          t.left(90)
          t.forward(135)
          t.left(90)
          t.forward(665)
          t.left(90)
          t.forward(135)
          t.left(90)
          t.forward(333.5)
          t.end_fill()
          t.penup()
          t.pencolor('black')
          t.goto(0,-300)
          t.pendown()
          t.write(' '.join(secret_word), font=style, align="center")
          return win
#David
question_count = 1
style = ('Courier', 100, 'bold')
question_answer = str()
while question_count == 1:
  a = main()
  t.setheading(0)
  t.pencolor('red')
  t.penup()
  t.goto(0,0)
  t.right(25)
  if a == 'q':
    t.write("QUITTER", font=style, align="center")
  elif a == 'L':
    t.write("LOSER", font=style, align="center")
  elif a == 'W':
    t.write("WINNER", font=style, align="center")
  #to determine if they quit or not
  #Jacque
  if a == 'q':
    question_count = 100
    break
  elif a != 'q':
    question_answer = str(input('\nWould you like to restart?(Y/N): '))
    if question_answer == 'Y' or question_answer == 'y':
      print('Okay!\n\n\n')
    elif question_answer == 'N' or question_answer == 'n':
      print('Alright\n')
      question_count = 100
      break
print('Thank you very much for playing my game, I hope you enjoyed this program')
time.sleep(3)


  
