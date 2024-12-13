# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
import math

def dist_to(point1, point2):
    xdist = abs(point1.x - point2.x)
    ydist = abs(point1.y - point2.y)
    return math.sqrt(xdist**2 + ydist**2)

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.kickoff_flag:
            self.set_intent(atba())
            return

        if dist_to(self.ball.location, self.friend_goal.location) < 1500:
            point = self.friend_goal.location + self.foe_goal.location * 0.1
        else:
            line = self.foe_goal.location - self.ball.location
            hypotenuse = dist_to(self.ball.location, self.foe_goal.location)
            y_dist = line.y / hypotenuse * 400
            x_dist = line.x / hypotenuse * 400
            point = self.ball.location - [x_dist, y_dist, 0]

        self.set_intent(go_near(point, ball = 1))

        dist = dist_to(self.me.location, point)
          
        if dist < 200:
            self.set_intent(short_shot(self.foe_goal.location))