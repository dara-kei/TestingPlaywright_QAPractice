import enum

class ProgrammingLanguage(enum.Enum):
    """ It is used in single select testing"""


    PYTHON = "Python"
    JAVASCRIPT = "JavaScript"
    JAVA = "Java"
    RUBY = "Ruby"
    SHARP = "C#"



    # с помощью enum создаем перечисление ProgrammingLanguage, в котором:
    # PYTHON — это имя элемента
    # "Python" — его значение

    # ProgrammingLanguage.PYTHON - это объект enum, у которого:
    # ProgrammingLanguage.PYTHON.name   # "PYTHON"
    # ProgrammingLanguage.PYTHON.value  # "Python"