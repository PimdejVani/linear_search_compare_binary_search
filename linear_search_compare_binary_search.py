from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet import clock
import random
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

def side_and_position_x(gap_edge=None, gap=None, window_x=None, num_in_list=None):
    side = ((window_x - (2 * gap_edge) + gap) / (num_in_list)) - gap
    position_x = []

    for i in range(num_in_list):

        if i == 0:
            start = gap_edge

        else:
            start += side + gap

        position_x.append(start)

    return side, position_x

def generate_list(target = None,num_in_list  = None):
    if num_in_list < 1:
        print("edit self.num_in_list it must more than 1")
        return 

    number = []

    while len(number) < num_in_list - 1:
        num = random.randint(0, 100)

        if num != target and num not in number:
            number.append(num)

    number.append(target)
    list = []
    random_numbers = random.sample(range(0, num_in_list ), num_in_list)

    for i in random_numbers :
        list.append(number[i])

    return list

class Renderer(Window):
    def __init__(self):
        ### set up ### you can edit it
        self.linear_sort = '2' # if you want sort linear number press 'yes' but if you don't want you can press anything
        self.target = 2 # if you don't want order you can press anything but do not press numbers from 0 to 100 type int
        #color over all
        self.color_text_target = "#F00F0F"
        self.color_text_main = "#FFFFFF"
        #color linear
        self.color_text_linear_search = "#FF00FF"
        self.color_on_linear_box = "#FFFFFF"
        self.color_text_linear_round = "#FFFFFF"
        self.color_text_linear_text_on_box = "#000000"
        self.color_linear_box_has_not_been_check = "#FFFFFF"
        self.color_linear_box_checking = "#0FFF0F"
        self.color_linear_box_checked = "#F000F0"
        self.color_text_sequence_linear_box = "#F000F0"
        #color binary
        self.color_text_binary_search = "#FF00FF"
        self.color_on_binary_box = "#FFFFFF"
        self.color_text_binary_round = "#FFFFFF"
        self.color_text_binary_text_on_box = "#000000"
        self.color_binary_box_has_not_been_check = "#FFFFFF"
        self.color_binary_box_checking = "#0FFF0F"
        self.color_binary_box_checked = "#F000F0"
        self.color_text_sequence_binary_box = "#F000F0"

        ### start
        self.num_in_list = 20
        self.window_ratio = 0.5
        self.window_x_full, self.window_y_full = 1920, 1080
        self.edge_gap = 30
        self.gap_box = 10
        
        if type(self.target) is not int :
            self.target = random.randint(0, 100)

        elif self.target < 0 or self.target > 100 :
            self.target = random.randint(0, 100)

        self.list_num = generate_list(self.target,self.num_in_list)
        self.window_x_ratio, self.window_y_ratio = math.floor(self.window_x_full * self.window_ratio), math.floor(self.window_y_full * self.window_ratio)
        self.side, self.position_list_num = side_and_position_x (self.edge_gap, self.gap_box, self.window_x_ratio, self.num_in_list)

        ### visual
        super().__init__(self.window_x_ratio, self.window_y_ratio, "Compare Linear Search AND Binary Search")
        self.batch = Batch()
        self.bars = []
        self.labels = []

        self.labels.append(Label('START!', font_name='Cascadia Code', font_size=30, x=self.window_x_ratio / 2, y=self.window_y_ratio / 2,
                                color=hex_to_rgb(self.color_text_main), anchor_x='center', anchor_y='center', batch=self.batch))
        self.labels.append(Label('TARGET = ' + str(self.target), font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.925,
                                color=hex_to_rgb(self.color_text_target), anchor_x='center', anchor_y='baseline', batch=self.batch))

        self.labels.append(Label('LINEAR SEARCH', font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.85,
                                color=hex_to_rgb(self.color_text_linear_search), anchor_x='center', anchor_y='baseline', batch=self.batch))
        
        for i, value in enumerate(self.list_num):
            color = hex_to_rgb(self.color_on_linear_box)
            self.bars.append(Rectangle(self.position_list_num[i], self.window_y_ratio * 0.65 - (self.side / 2),
                                       self.side, self.side, color=color, batch=self.batch))
            self.labels.append(Label(str(value), font_name='Cascadia Code', font_size=15,x=self.position_list_num[i] + (self.side / 2), y=self.window_y_ratio * 0.65,
                                     color=hex_to_rgb(self.color_text_linear_text_on_box), anchor_x='center', anchor_y='center',batch=self.batch))
            self.labels.append(Label(str(i), font_name='Cascadia Code', font_size=12, x=self.position_list_num[i] + (self.side / 2), y = self.window_y_ratio * 0.615 - (self.side / 2),
                                    color=hex_to_rgb(self.color_text_sequence_linear_box), anchor_x='center', anchor_y='baseline', batch=self.batch))

        self.labels.append(Label('BINARY SEARCH', font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.35,
                                color=hex_to_rgb(self.color_text_binary_search), anchor_x='center', anchor_y='baseline', batch=self.batch))
        
        for i1, value1 in enumerate(self.list_num):
            color = hex_to_rgb(self.color_on_binary_box)
            self.bars.append(Rectangle(self.position_list_num[i1], self.window_y_ratio * 0.15 - (self.side / 2),
                                       self.side, self.side, color=color, batch=self.batch))
            self.labels.append(Label(str(value1), font_name='Cascadia Code', font_size=15,x=self.position_list_num[i1] + (self.side / 2), y=self.window_y_ratio * 0.15,
                                     color=hex_to_rgb(self.color_text_binary_text_on_box), anchor_x='center', anchor_y='center',batch=self.batch))
            self.labels.append(Label(str(i1), font_name='Cascadia Code', font_size=12, x=self.position_list_num[i1] + (self.side / 2), y = self.window_y_ratio * 0.115 - (self.side / 2),
                                    color=hex_to_rgb(self.color_text_sequence_binary_box), anchor_x='center', anchor_y='baseline', batch=self.batch))
        
        ###for on_update
        self.count = -1
        self.check_linear = 'not finish'
        self.check_binary = 'not finish'
        self.sequence_linear = -1
        self.sequence_binary = [0,len(self.list_num)-1]
        self.color_checking_linear = -1
        self.color_checked_linear = -1
        self.color_checking_binary = -1
        self.finish_linear = True
        self.finish_binary = True
        self.count_all_finish = 0

    def on_update(self, deltatime):
        self.bars = []
        self.labels = []

        if self.count < 0 :
            self.list_num_linear = self.list_num.copy()

            if self.linear_sort == 'yes' :
                self.list_num_linear = sorted(self.list_num.copy())

            self.list_num_binary = sorted(self.list_num.copy())
            self.labels.append(Label('SORTED!', font_name='Cascadia Code', font_size=30, x=self.window_x_ratio / 2, y=self.window_y_ratio / 2,
                                    color=hex_to_rgb(self.color_text_main), anchor_x='center', anchor_y='center', batch=self.batch))

        elif self.count >= 0 and (self.check_linear == 'not finish' or self.check_binary == 'not finish') and not (self.count_all_finish > 0)  : #visual คำบนหัวbox และใส่เงื่อไขการแสดงสีของbox

            if self.count % 2 == 0 : #check

                if self.check_linear == 'not finish' :
                    self.sequence_linear += 1
                    self.color_checking_linear = self.sequence_linear
                    self.color_checked_linear = self.sequence_linear
                    self.text_linear = 'CHECK'
                    self.sequence_linear_text = self.sequence_linear

                if self.check_binary == 'not finish' :
                    self.color_checking_binary = self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)
                    self.text_binary = 'CHECK'
                    self.sequence_binary_text = self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)

            elif self.count % 2 == 1 :

                if self.check_linear == 'not finish' :
            
                    if self.list_num_linear[self.sequence_linear] == self.target :
                        self.check_linear = 'finish'

                    else :
                        self.color_checking_linear = - 1
                        self.text_linear = 'NOT'

                if self.check_binary == 'not finish' : 

                    if self.list_num_binary[self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)] == self.target :
                        self.check_binary = 'finish'

                    else :
                        self.color_checking_binary = -1
                        
                        if self.target > self.list_num_binary[self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)] :
                            self.sequence_binary[0] = (self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)) + 1
                            self.text_binary = 'OVER'

                        else :
                            self.sequence_binary[1] = (self.sequence_binary[0] + ((self.sequence_binary[1] - self.sequence_binary[0]) // 2)) - 1
                            self.text_binary = 'LESS'

            if self.check_linear == 'not finish' :
                self.labels.append(Label(self.text_linear, font_name='Cascadia Code', font_size=15, x=self.position_list_num[self.sequence_linear_text] + ((self.side) / 2), y=self.window_y_ratio * 0.65 + (self.side / 2) + (self.side * 0.25),
                                        color=hex_to_rgb(self.color_text_linear_text_on_box), anchor_x='center', anchor_y='baseline', batch=self.batch)) 
                
                self.count_linear = self.count

            if self.check_binary == 'not finish' :
                self.labels.append(Label(self.text_binary, font_name='Cascadia Code', font_size=15, x=self.position_list_num[self.sequence_binary_text] + ((self.side) / 2), y=self.window_y_ratio * 0.15 + (self.side / 2) + (self.side * 0.25),
                                        color=hex_to_rgb(self.color_text_binary_text_on_box), anchor_x='center', anchor_y='baseline', batch=self.batch))
                 
                self.count_bianry = self.count



        if self.check_linear == 'finish' or self.check_binary == 'finish':

            if self.check_linear == 'finish' and self.count_all_finish < 1 :
                self.labels.append(Label('FINISH', font_name='Cascadia Code', font_size=15, x=self.position_list_num[self.color_checking_linear] + ((self.side) / 2), y=self.window_y_ratio * 0.65 + (self.side / 2) + (self.side * 0.25),
                                        color=hex_to_rgb(self.color_text_linear_text_on_box), anchor_x='center', anchor_y='baseline', batch=self.batch)) 
                
                if self.finish_linear :
                    self.count_linear = self.count
                    self.finish_linear = False

            if self.check_binary == 'finish' and self.count_all_finish < 1 :
                self.labels.append(Label('FINISH', font_name='Cascadia Code', font_size=15, x=self.position_list_num[self.color_checking_binary] + ((self.side) / 2), y=self.window_y_ratio * 0.15 + (self.side / 2) + (self.side * 0.25),
                                        color=hex_to_rgb(self.color_text_binary_text_on_box), anchor_x='center', anchor_y='baseline', batch=self.batch)) 
                
                if self.finish_binary :
                    self.count_binary = self.count
                    self.finish_binary = False
            
            if self.check_linear == 'finish' and self.check_binary == 'finish' and self.count_all_finish < 1:
                self.count_all_finish += 1

        if self.check_linear == 'finish' and self.check_binary == 'finish' and self.count_all_finish > 0 :

            if self.check_linear == 'finish' and self.check_binary == 'finish' and self.count_all_finish > 1 :
                self.labels.append(Label('FINISH!', font_name='Cascadia Code', font_size=30, x=self.window_x_ratio / 2, y=self.window_y_ratio / 2,
                                        color=hex_to_rgb(self.color_text_main), anchor_x='center', anchor_y='center', batch=self.batch))

            self.count_all_finish += 1

        self.labels.append(Label('TARGET = ' + str(self.target), font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.925,
                                color=hex_to_rgb(self.color_text_target), anchor_x='center', anchor_y='baseline', batch=self.batch))

        if self.count >= 0 :
            self.labels.append(Label('ROUND = ' + str((self.count_linear // 2) + 1), font_name='Cascadia Code', font_size=12, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.8,
                        color=hex_to_rgb(self.color_text_linear_round), anchor_x='center', anchor_y='baseline', batch=self.batch))
            self.labels.append(Label('ROUND = ' + str((self.count_bianry // 2) + 1), font_name='Cascadia Code', font_size=12, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.3,
                        color=hex_to_rgb(self.color_text_binary_round), anchor_x='center', anchor_y='baseline', batch=self.batch))

        self.labels.append(Label('LINEAR SEARCH', font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.85,
                                color=hex_to_rgb(self.color_text_linear_search), anchor_x='center', anchor_y='baseline', batch=self.batch))
        
        for i, value in enumerate(self.list_num_linear):
            color = hex_to_rgb(self.color_on_linear_box)

            if i <= self.color_checked_linear :
                color = hex_to_rgb(self.color_linear_box_checked)

            if i == self.color_checking_linear :
                color = hex_to_rgb(self.color_linear_box_checking)

            self.bars.append(Rectangle(self.position_list_num[i], self.window_y_ratio * 0.65 - (self.side / 2),
                                       self.side, self.side, color=color, batch=self.batch))
            self.labels.append(Label(str(value), font_name='Cascadia Code', font_size=15,x=self.position_list_num[i] + (self.side / 2), y=self.window_y_ratio * 0.65,
                                     color=hex_to_rgb(self.color_text_linear_text_on_box), anchor_x='center', anchor_y='center',batch=self.batch))
            self.labels.append(Label(str(i), font_name='Cascadia Code', font_size=12, x=self.position_list_num[i] + (self.side / 2), y = self.window_y_ratio * 0.615 - (self.side / 2),
                                    color=hex_to_rgb(self.color_text_sequence_linear_box), anchor_x='center', anchor_y='baseline', batch=self.batch))

        self.labels.append(Label('BINARY SEARCH', font_name='Cascadia Code', font_size=20, x=self.window_x_ratio / 2, y=self.window_y_ratio * 0.35,
                                color=hex_to_rgb(self.color_text_binary_search), anchor_x='center', anchor_y='baseline', batch=self.batch))

        for i1, value1 in enumerate(self.list_num_binary):
            color = hex_to_rgb(self.color_on_binary_box)

            if i1 < self.sequence_binary[0] or i1 > self.sequence_binary[1] :
                color = hex_to_rgb(self.color_binary_box_checked)

            if i1 == self.color_checking_binary :
                color = hex_to_rgb(self.color_binary_box_checking)

            self.bars.append(Rectangle(self.position_list_num[i1], self.window_y_ratio * 0.15 - (self.side / 2),
                                       self.side, self.side, color=color, batch=self.batch))
            self.labels.append(Label(str(value1), font_name='Cascadia Code', font_size=15,x=self.position_list_num[i1] + (self.side / 2), y=self.window_y_ratio * 0.15,
                                     color=hex_to_rgb(self.color_text_binary_text_on_box), anchor_x='center', anchor_y='center',batch=self.batch))
            self.labels.append(Label(str(i1), font_name='Cascadia Code', font_size=12, x=self.position_list_num[i1] + (self.side / 2), y = self.window_y_ratio * 0.115 - (self.side / 2),
                                    color=hex_to_rgb(self.color_text_sequence_binary_box), anchor_x='center', anchor_y='baseline', batch=self.batch))

        self.count += 1

        if self.check_linear == 'finish' and self.check_binary == 'finish' and self.count_all_finish > 2 :
            clock.unschedule(self.on_update)

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()