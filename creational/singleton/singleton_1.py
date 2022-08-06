class AppSettings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self) -> None:
        self.tema = 'tema escuro'
        self.font = '14px'


if __name__ == "__main__":
    as1 = AppSettings()
    
    as1.tema = 'claro'
    print(as1.tema)
    
    as2 = AppSettings()

    print(as1.tema)

    """
    Retorno:
    claro
    tema escuro
    """
