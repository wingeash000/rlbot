# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *

class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        if self.ball.location.z > 50:
            self.set_intent(goto(self.friend_goal.location))
            return
        dist1 = abs(self.ball.location.y - self.foe_goal.location.y)
        dist2 = abs(self.me.location.y - self.foe_goal.location.y)
        ahead_of_ball = dist1 - 60 > dist2
        if ahead_of_ball or self.ball.location.z > 20:
            self.set_intent(goto(self.friend_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))
