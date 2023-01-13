import pypresence
import pypresence.exceptions

class Presence:
    def __init__(self):
        try:
            self.presence = pypresence.Presence('995373260105592832')
            self.presence.connect()
            self.presence_use = True
        except pypresence.exceptions.DiscordNotFound:
            self.presence_use = False

    def checkUse(self):
        return self.presence_use

    def update(self, **kwargs):
        try:    
            self.presence.update(**kwargs)
            return True
        except Exception:
            self.presence.close()
            return False
