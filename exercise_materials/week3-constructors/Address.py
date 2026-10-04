class Address:
    def __init__(
        self,
        apartment,
        address_line1,
        city,
        county,
        postcode,
        country,
        address_line2="N/A",
        address_line3="N/A",
    ):
        self.apartment = apartment
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.city = city
        self.county = county
        self.postcode = postcode
        self.country = country

    def display_address(self):
        address_parts = [self.apartment, self.address_line1]

        if self.address_line2 != "N/A":
            address_parts.append(self.address_line2)

        if self.address_line3 != "N/A":
            address_parts.append(self.address_line3)

        address_parts.extend([self.city, self.county, self.postcode, self.country])

        return ", ".join(address_parts)