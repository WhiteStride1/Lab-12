class Television:
    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 2  # Maximum TV volume

    def __init__(self):
        """
        This creates TV object with the default starting values
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        This method changes the ON/OFF state of the TV
        ON is status = True, OFF is status = False
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self):
        """
        This method changes the Channel up by 1 when the TV status is ON
        If the MAX_CHANNEL is reached then it rolls over to the MIN_CHANNEL Value
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self):
        """
        This Method changes the Channel down by 1 when the TV status is ON
        If the MIN_CHANNEL value is reached then it rolls  over to the MAX_CHANNEL Value
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self):
        """
        This Method changes the Volume up by 1 when the TV status is ON
        If the MAX_VOLUME value is reached then it will remain at that value
        """
        if self.__status == True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume = self.__volume + 1

    def volume_down(self):
        """
        This method changes the Volume down by 1 when the TV status is OFF
        If the MIN_VOLUME is reached then it will remain at that value
        """
        if self.__status == True:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume - 1

    def __str__(self):
        """
       This method returns the TV status
       :return tv: returns tv status
        """
        tv = 'TV Status: Is on = {}, Channel = {}, Volume = {}'.format(self.__status, self.__channel, self.__volume)
        return str(tv)

