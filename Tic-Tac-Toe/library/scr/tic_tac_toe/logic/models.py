# Tic-Tac-Toe\library\scr\tic_tac_toe\logic\models.py

import enum

# By default, you can’t compare a member of a Python enum against its value. 
# For instance, comparing Mark.CROSS == "X" will give you False. 
# This is to avoid confusing identical values defined in different places and having unrelated semantics.
# However, it may sometimes be more convenient to think about them in terms of strings instead of enum members.
# So we define Mark as a mixin class of the str and enum.Enum types:
# This is known as a derived enum, members can be compared to instances of the mixed-in type.
# You can now compare Mark.NAUGHT and Mark.CROSS to string values.

class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    # enums are glorified classes, you can put methods and properties into them.
    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT