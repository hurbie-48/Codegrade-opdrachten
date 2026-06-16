from product import Product
from country import Country
class Trade:

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    def get_country_from(self) -> Country:
        raise NotImplementedError

    def get_product(self) -> Product:
        raise NotImplementedError

    def get_country_to(self) -> Country:
        raise NotImplementedError

    def mass_in(self, unit:str) -> list:
        raise NotImplementedError
