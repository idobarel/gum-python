"""
A simple python3 implementation of a tool called 'gum'.
https://github.com/charmbracelet/gum
gum is a tool for glamorous shell scripts, written in go,
and supposed to be used in shell scripts.
I've created an eassy to use python class that takes advantage
of that tool and let the avrage python user create a cool looking
CLIs.
"""
from gum.utils import choose
from  gum.utils import input
from gum.utils import confirm
from gum.utils import write
from gum.utils import search
from gum.utils import spin
from gum.utils import bunner
