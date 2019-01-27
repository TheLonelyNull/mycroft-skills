# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
import requests
import json

__author__ = 'TheLonelyNull'
LOGGER = getLogger(__name__)


class SpaceXLaunchSkill(MycroftSkill):
    mission_name = ""
    rocket_name = ""
    date = ""
    facility = ""
    # The constructor of the skill, which calls MycroftSkill's constructor

    def __init__(self):
        super(SpaceXLaunchSkill, self).__init__(name="SpaceXLaunchSkill")

    @intent_handler(IntentBuilder("LaunchIntent").require("When").require("PrevNext").require("SpaceXLaunch"))
    def handle_launch_intent(self, message):
        when = message.data["PrevNext"]

        if when == "last" or when == "previous":
            self.respond("latest")
            self.speak_dialog("previous.launch.is", data={"date":self.date, "facility":self.facility, "mission_name":self.mission_name, "rocket_name":self.rocket_name})
            # TODO find previous spacex launch details
        elif when == "next":
            self.respond("next")
            self.speak_dialog("next.launch.is", data={"date":self.date, "facility":self.facility, "mission_name":self.mission_name, "rocket_name":self.rocket_name})

    def getContent(self, PrevNext):
        content = requests.get(
            "https://api.spacexdata.com/v3/launches/"+PrevNext).content
        return content

    def respond(self, PrevNext):
        content = self.getContent(PrevNext)
        dictionary = json.loads(content)
        self.misssion_name = dictionary["mission_name"]
        self.date = dictionary["launch_date_unix"]
        self.rocket_name = dictionary["rocket"]["rocket_name"]
        self.facility = dictionary["launch_site"]["site_name_long"]


# The "create_skill()" method is used to create an instance of the skill.
def create_skill():
    return SpaceXLaunchSkill()
