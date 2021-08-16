import simplegui,random

sheet_url = "http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png"
sheet_width = 900   
sheet_height = 900
sheet_columns = 9
sheet_rows = 9

class spritesheet:
    def __init__(self,imgurl,width,height,columns,rows):
        self.img = simplegui.load_image(imgurl)
        self.width = width
        self.height= height
        self.columns = columns
        self.rows = rows
        
        self.frame_duration = random.randrange(1, 10)
        self.frame_width = width / columns
        self.frame_height = height / rows
        self.frame_centre_x = self.frame_width  / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [0, 0]
        self.frame_clock = 0
        self.centre_dest = (random.randrange(0, 500), random.randrange(0, 500))
    
    def update_index(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = ((self.frame_index[1] + 1) % self.rows)
        
    def done(self):
        if self.frame_index == [8,8]:
            return True
        
    
    def draw(self, canvas):
        self.frame_clock += 1
        if self.frame_clock % self.frame_duration == 0:
            if self.done() != True:
                self.update_index()

        centre_source = (self.frame_width * self.frame_index[0] + self.frame_centre_x, 
                             self.frame_height * self.frame_index[1] + self.frame_centre_y)
        dims_source = (self.frame_width, self.frame_height)

        dims_dest = (100, 100)

        canvas.draw_image(self.img, centre_source, dims_source, self.centre_dest, dims_dest)

        
explosions = []        
sheet1 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet2 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet3 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet4 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet5 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet6 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet7 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet8 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet9 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)
sheet10 = spritesheet(sheet_url,sheet_width,sheet_height,sheet_columns,sheet_rows)


explosions.append(sheet1)
explosions.append(sheet2)
explosions.append(sheet3)
explosions.append(sheet4)
explosions.append(sheet5)
explosions.append(sheet6)
explosions.append(sheet7)
explosions.append(sheet8)
explosions.append(sheet9)
explosions.append(sheet10)

        
frame = simplegui.create_frame("sprite", 500, 500)        
        
def draw0(canvas):
    for sheet in explosions:
        sheet.draw(canvas)
        
frame.set_draw_handler(draw0)        
        
frame.start()  