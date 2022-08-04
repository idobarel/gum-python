# Gum

A simple python3 implementation of a tool called 'gum'.
https://github.com/charmbracelet/gum
gum is a tool for glamorous shell scripts, written in go,
and supposed to be used in shell scripts.
I've created an eassy to use python class that takes advantage
of that tool and let the avrage python user create a cool looking
CLIs.

# Installation
Use the install instractions from https://github.com/charmbracelet/gum and then:
```bash
$ git clone https://github.com/idobarel/gum-python
$ cd gum-python
$ sudo python3 setup.py install
```

# Usage
```python
import gum

print("which basketball team you like the most?")
x = gum.search(["cavs", "magic", "golden state", "boston"])
gum.spin("hold on...")
print(f"No way! I'm there biggest fan!")
```

# Notice 
as it is for now, I have nothing to deal with the authours of the gum tool, I wanted it to be easier to use in big python applications, so I created this code.
Just to clear any missunderstandings, all the credit and the notice should go to @charm or https://github.com/charmbracelet.

Hope yall having a nice day!
