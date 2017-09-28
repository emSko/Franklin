from jproperties import Properties


class PropertiesService:
    def __init__(self, path, encoding="utf-8"):
        self._properties = Properties()
        self._path = path
        self._encoding = encoding
        with open(path, "rb") as f:
            self._properties.load(f, encoding)

    def get_property(self, key):
        prop, meta = self._properties[key]
        return prop

    def save_property(self, key, value):
        self._properties[key] = value
        with open(self._path, "wb") as f:
            self._properties.store(f, self._encoding)
