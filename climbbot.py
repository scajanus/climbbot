import gradeconvert
from ircutils import bot

class ClimbBot(bot.SimpleBot):

    def on_private_message(self, event):
        self.send_message(event.target, "Just received this private message: " + event.message)

    def on_channel_message(self, event):
        msg = str(event.message)
        if msg.startswith("~") or msg.startswith("!"):
            msg_text = msg[1:]
            try:
                if gradeconvert.is_grade(msg_text):
                    self.send_message(event.target, gradeconvert.convert(msg_text))
                else:
                    self.send_message(event.target, "I don't understand: " + msg_text)
            except StandardError as e:
                print "Error processing message: " + msg_text, e


if __name__ == "__main__":
    # Create an instance of the bot
    # We set the bot's nickname here
    climbbot = ClimbBot("climbbot")
    climbbot.real_name = "climbbot"

    # Let's connect to the host
    climbbot.connect("irc.snoonet.com", channel="#climbing")

    # Start running the bot
    climbbot.start()
