class Place:
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        self.title = title
        self.description = description
        # On utilise des tirets bas (_price, _latitude...) pour stocker les valeurs en interne
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []  # Liste qui contiendra les équipements (Wi-Fi, etc.) plus tard

    # --- SÉCURITÉ / VALIDATION DU PRIX ---
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self._price = float(value)

    # --- SÉCURITÉ / VALIDATION DE LA LATITUDE ---
    @property
    def latitude(self):
        return self._latitude

    # On force la latitude à être sur Terre (entre -90 et 90)
    @latitude.setter
    def latitude(self, value):
        if not (-90.0 <= value <= 90.0):
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
        self._latitude = float(value)

    # --- SÉCURITÉ / VALIDATION DE LA LONGITUDE ---
    @property
    def longitude(self):
        return self._longitude

    # On force la longitude à être sur Terre (entre -180 et 180)
    @longitude.setter
    def longitude(self, value):
        if not (-180.0 <= value <= 180.0):
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
        self._longitude = float(value)