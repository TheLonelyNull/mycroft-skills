# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'TheLonelyNull'
LOGGER = getLogger(__name__)

class SpaceXLaunchSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(SpaceXLaunchSkill, self).__init__(name="SpaceXLaunchSkill")

    @intent_handler(IntentBuilder("LaunchIntent").require("When").require("PrevNext").require("SpaceXLaunch"))
    def handle_launch_intent(self, message):
        when = message.data["PrevNext"]
        
        if when == "last" or when == "previous":
            self.speak_dialog("Previous launch to be fetched")
            #TODO find previous spacex launch details
        elif when == "next":
            self.speak_dialog("Next launch to be fetched")
            #find next spacex launch details

# The "create_skill()" method is used to create an instance of the skill.
def create_skill():
    return SpaceXLaunchSkill()
