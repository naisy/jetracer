import traitlets


class Racecar(traitlets.HasTraits):
    steering = traitlets.Float()
    throttle = traitlets.Float()
    steering_min_endpoint = traitlets.Float()
    steering_max_endpoint = traitlets.Float()
    throttle_min_endpoint = traitlets.Float()
    throttle_max_endpoint = traitlets.Float()

    @traitlets.validate('steering')
    def _clip_steering(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']
        
    @traitlets.validate('throttle')
    def _clip_throttle(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']

    @traitlets.validate('steering_min_endpoint')
    def _clip_steering_min_endpoint(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']

    @traitlets.validate('steering_max_endpoint')
    def _clip_steering_max_endpoint(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']

    @traitlets.validate('throttle_min_endpoint')
    def _clip_throttle_min_endpoint(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']

    @traitlets.validate('throttle_max_endpoint')
    def _clip_throttle_max_endpoint(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']
