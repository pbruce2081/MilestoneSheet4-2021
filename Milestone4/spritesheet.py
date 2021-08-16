import simplegui

#canvas constants
canvasWidth = 500
canvasHeight = 500

#Load image from URL
spriteSheetURL = 'http://www.cs.rhul.ac.uk/courses/CS1830/sprites/runnerSheet.png'
#Image dimensions
spriteSheet_width = 1440
spriteSheet_height = 1480
spriteSheet_columns = 6
spriteSheet_rows = 5

#sprite class
class Spritesheet:
    def __init__(self, imageURL, width, height, columns, rows):
        self.image = simplegui.load_image(imageURL)
        self.width = width
        self.height = height
        self.columns = columns 
        self.rows = rows
        #self.frameDuration = frameDuration

        #set frame dimensions
        self.frame_width = width/columns
        self.frame_height = height/rows
        #set frame coordinates
        self.frame_centre_x = self.frame_width/2
        self.frame_centre_y = self.frame_height/2
        #initial frame index = [0,0]
        self.frame_index = [0,0]
    
    def next_frame(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows
    
    def draw(self, canvas):
        self.next_frame()
        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )
        source_size = (self.frame_width, self.frame_height)
        dest_centre = (canvasWidth/2, canvasHeight/2)
        dest_size = (100, 100)

        canvas.draw_image(self.image, source_centre, source_size, dest_centre, dest_size)

class Clock:
    def __init__(self, frameDuration):
        self.frameDuration = frameDuration
        self.frame_clock = 0
    
    def tick(self):
        self.frame_clock += 1
    
    def transition(self, frameDuration):
        transitioning = self.frame_clock % self.frameDuration
        if transitioning == 0:
            return True
        else:
            return False


frame = simplegui.create_frame("Spritesheet", canvasWidth, canvasHeight)
sheet = Spritesheet(
    spriteSheetURL,
    spriteSheet_width, spriteSheet_height,
    spriteSheet_columns, spriteSheet_rows
)
clock = Clock(5)

def draw(canvas):
    clock.tick()
    if clock.transition == True:
        sheet.next_frame()
    sheet.draw(canvas)

frame.set_draw_handler(draw)
frame.start()