class Television:


    def __init__(self):
        self.is_on = False

        self.channel = 0
        self.volume_level = 0



    def turn_on(self):
         self.is_on = True



    def turn_off(self):
        self.is_on = False



    def channel_up(self):
        if self.channel < 100:
            self.channel  += 1


    def channel_down(self):
        if self.channel > 0:
            self.channel -= 1



    def get_channel(self) -> int:
        return self.channel

    def set_channel(self, channel_number):
        self.channel = channel_number



    def  increase_volume(self):
        if self.volume_level < 100:
            self.volume_level += 1

    def  decrease_volume(self):
        if self.volume_level >= 0:
            self.volume_level -= 1


    def set_volume(self, volume):
        self.volume_level = volume

    def get_volume(self):
        return self.volume_level








