from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit


class NvidiaRacecar(Racecar):
    i2c_address = traitlets.Integer(default_value=0x40)
    steering_gain = traitlets.Float(default_value=1.0)
    steering_offset = traitlets.Float(default_value=0)
    steering_channel = traitlets.Integer(default_value=0)
    throttle_gain = traitlets.Float(default_value=0.5)
    throttle_offset = traitlets.Float(default_value=0)
    throttle_channel = traitlets.Integer(default_value=1)

    _steering_min_endpoint = -0.3
    _steering_max_endpoint = 0.3
    _throttle_min_endpoint = -0.69
    _throttle_max_endpoint = 0.69
    
    def __init__(self, *args, **kwargs):
        super(NvidiaRacecar, self).__init__(*args, **kwargs)
        self.kit = ServoKit(channels=16, address=self.i2c_address)
        self.steering_motor = self.kit.continuous_servo[self.steering_channel]
        self.throttle_motor = self.kit.continuous_servo[self.throttle_channel]
    
    @traitlets.observe('steering')
    def _on_steering(self, change):
        if change['new'] <= 0:
            steering = -1.0 * self._steering_min_endpoint * change['new'] * self.steering_gain + self.steering_offset
        else:
            steering = 1.0 * self._steering_max_endpoint * change['new'] * self.steering_gain + self.steering_offset
        if steering < self.steering_min_endpoint:
            steering = self.steering_min_endpoint
        elif steering > self.steering_max_endpoint:
            steering = self.steering_max_endpoint
        self.steering_motor.throttle = steering

    @traitlets.observe('throttle')
    def _on_throttle(self, change):
        if change['new'] <= 0:
            throttle = -1.0 * self._throttle_min_endpoint * change['new'] * self.throttle_gain + self.throttle_offset
        else:
            throttle = 1.0 * self._throttle_max_endpoint * change['new'] * self.throttle_gain + self.throttle_offset
        if throttle < self.throttle_min_endpoint:
            throttle = self.throttle_min_endpoint
        elif throttle > self.throttle_max_endpoint:
            throttle = self.throttle_max_endpoint
        self.throttle_motor.throttle = throttle

    @traitlets.observe('steering_min_endpoint')
    def _on_steering_min_endpoint(self, change):
        self._steering_min_endpoint = change['new']

    @traitlets.observe('steering_max_endpoint')
    def _on_steering_max_endpoint(self, change):
        self._steering_max_endpoint = change['new']

    @traitlets.observe('throttle_min_endpoint')
    def _on_throttle_min_endpoint(self, change):
        self._throttle_min_endpoint = change['new']

    @traitlets.observe('throttle_max_endpoint')
    def _on_throttle_max_endpoint(self, change):
        self._throttle_max_endpoint = change['new']




