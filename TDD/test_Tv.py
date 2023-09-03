import unittest
from Tv import *


class  TestTvFunction(unittest.TestCase):
    def setUp(self):
        self.samsung = Television()
        self.samsung.turn_on()

    def test_television_isOn(self):
        self.samsung = Television()
        self.samsung.turn_on()
        self.assertTrue(self.samsung.is_on)

    def test_television_isOff(self):
        self.samsung = Television()
        self.samsung.turn_off()
        self.assertFalse(self.samsung.is_on)



    def test_television_can_change_channel(self):
        self.samsung.set_channel(66)
        self.samsung.channel_up()

        newChannel = self.samsung.get_channel()
        self.assertEqual(67,newChannel)




    def test_television_can_change_channel_2(self):
        self.samsung.set_channel(66)
        self.samsung.channel_up()
        self.samsung.channel_up()

        newChannel = self.samsung.get_channel()
        self.assertEqual(68, newChannel)





    def test_television_can_change_channel_above_100(self):

        self.samsung.set_channel(99)
        self.samsung.channel_up()
        self.samsung.channel_up()

        newChannel = self.samsung.get_channel()
        self.assertEqual(100, newChannel)



    def test_television_can_change_decrease(self):
        self.samsung.set_channel(66)
        self.samsung.channel_down()

        newChannel = self.samsung.get_channel()
        self.assertEqual(65, newChannel)





    def test_television_can_change_decrease_twice(self):

        self.samsung.set_channel(66)
        self.samsung.channel_down()
        self.samsung.channel_down()

        newChannel = self.samsung.get_channel()
        self.assertEqual(64, newChannel)


    def test_television_can_not_decrease_below_0(self):

        self.samsung.set_channel(1)
        self.samsung.channel_down()
        self.samsung.channel_down()

        newChannel = self.samsung.get_channel()
        self.assertEqual(0, newChannel)



    def test_television_volume_can_increase(self):

        self.samsung.set_volume(30)
        self.samsung.increase_volume()

        check_volume = self.samsung.get_volume()
        self.assertEqual(31, check_volume)



    def test_television_can_increase_twice(self):
        self.samsung.set_volume(30)
        self.samsung.increase_volume()
        self.samsung.increase_volume()

        check_volume = self.samsung.get_volume()
        self.assertEqual(32, check_volume)



    def test_television_can_not_increase_above_100(self):
        self.samsung.set_volume(99)
        self.samsung.increase_volume()
        self.samsung.increase_volume()

        newVolume = self.samsung.get_volume()
        self.assertEqual(100, newVolume)



    def test_television_can_decrease_volume(self):
        self.samsung.set_volume(99)
        self.samsung.decrease_volume()

        newVolume = self.samsung.get_volume()
        self.assertEqual(98, newVolume)




    def test_television_can_decrease_volume_2(self):
            self.samsung.set_volume(99)
            self.samsung.decrease_volume()
            self.samsung.decrease_volume()


            newVolume = self.samsung.get_volume()
            self.assertEqual(97, newVolume)









