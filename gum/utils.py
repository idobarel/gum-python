from os import popen
from os import system


def choose(msg: str, opt: list["str"], type: object = str):
    """A drop down menu.\n
    takes 2 arguments & 1 potential.
    msg >> the question you want to ask the user.
    opt >> the options you want to give the user. as a list of strings*
    *type >> the return type. a string or a number typed obj.

    Althogh the type is different, the list must be a list of
    strings.
    """
    print(msg)
    s = " ".join(opt)
    return type(popen("gum choose " + s).read().strip())


def input(placeholder: str = "", is_password=True, header="", prompt="") -> str:
    """
    Regular input, with a potetial placeholder.
    """
    if not is_password:
        x = popen(f"gum input --placeholder '{placeholder}' --header '{header}' --prompt '{prompt}'").read().strip()
    else:
        x = popen(f"gum input --placeholder '{placeholder}' --header '{header}' --prompt '{prompt}' --password").read().strip()
    return x


def confirm(msg: str, background_color=212, color=255) -> bool:
    """
    A yes or no question box, will return
    True on yes, False on no.
    """
    x = system(f'gum confirm "{msg}" --selected.background {background_color} --selected.foreground {color}')
    return x == 0


def write() -> str:
    """
    Let you write multi-lined text,
    CTRL+C to stop, and recive the input.
    """
    x = popen("gum write").read()
    return x


def search(options: list[str]):
    """
    Opens up a search box in your terminal,
    where the user can search from your options.
    """
    s = "\n".join(options)
    with open("temp", "w") as f:
        f.write(s)
        f.close()
    x = popen("cat temp | gum filter").read().strip()
    popen("rm temp")
    return x


def spin(title: str, time: int = 3, spinner: str = "dot"):
    """
    Printing a spinner with a title
    types of spinners:\ndot,
    line,
    minidot,
    jump,
    pulse,
    points,
    globe,
    moon,
    monkey,
    meter,
    hamburger"""
    spinners = [
        "dot",
        "line",
        "minidot",
        "jump",
        "pulse",
        "points",
        "globe",
        "moon",
        "monkey",
        "meter",
        "hamburger",
    ]
    if spinner not in spinners:
        raise ValueError(f"The spinner {spinner} was not found...")
    system(f'gum spin --title "{title}" --spinner "{spinner}" sleep {time}')


def bunner(text: str, border: str, margin: int, padding: tuple, color: int = 212):
    system(
        f"""gum style --border {border} --margin "{margin}" --padding "{padding[0]} {padding[1]}" --border-foreground {color} "{text}" """
    )
