class InvalidExtensionEnvironment(Exception):
    pass


class Extension:
    _enabled = True

    def enable(self, keyboard):
        self._enabled = True

        self.on_runtime_enable(self, keyboard)

        return self

    def disable(self, keyboard):
        self._enabled = False

        self.on_runtime_disable(self, keyboard)

        return self

    # The below methods should be implemented by subclasses

    def on_runtime_enable(self, keyboard):
        return self

    def on_runtime_disable(self, keyboard):
        return self

    def during_bootup(self, keyboard):
        return self

    def before_matrix_scan(self, keyboard):
        return self

    def after_matrix_scan(self, keyboard):
        return self

    def before_hid_send(self, keyboard):
        return self

    def after_hid_send(self, keyboard):
        return self
