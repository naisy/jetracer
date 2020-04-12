from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit


class NvidiaRacecar(Racecar):
    i2c_address = traitlets.Integer(default_value=0x40)
    steering_gain = traitlets.Float(default_value=-0.65)
    steering_offset = traitlets.Float(default_value=0)
    steering_channel = traitlets.Integer(default_value=0)
    throttle_gain = traitlets.Float(default_value=0.5)
    throttle_channel = traitlets.Integer(default_value=1)
    
    def __init__(self,type,  *args, **kwargs):
        super(NvidiaRacecar, self).__init__(*args, **kwargs)
        self.type = type
        self.kit = ServoKit(channels=16, address=self.i2c_address)
        self.steering_motor = self.kit.continuous_servo[self.steering_channel]
        self.throttle_motor = self.kit.continuous_servo[self.throttle_channel]
    
    @traitlets.observe('steering')
    def _on_steering(self, change):
        if self.type == "TT02":
            self.steering_motor.throttle = -(change['new'] * self.steering_gain + self.steering_offset - 0.2)
        elif self.type == "OPTION":
            self.steering_motor.throttle = change['new'] * self.steering_gain + self.steering_offset
        else:
            self.steering_motor.throttle = change['new'] * self.steering_gain + self.steering_offset

    @traitlets.observe('throttle')
    def _on_throttle(self, change):
        if self.type == "TT02":
            self.throttle_motor.throttle = -change['new'] * self.throttle_gain + 0.2
        elif self.type == "OPTION":
            self.throttle_motor.throttle = change['new'] * self.throttle_gain - 0.2
        else:
            self.throttle_motor.throttle = change['new'] * self.throttle_gain
