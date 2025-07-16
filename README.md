# Aviation Model

This is a simple model for estimating the global fleet size for aircraft.

## Developer guide 

### Installing Dependeniies in virtual enronments
This project uses uv to manage dpendencies and virtual environments. This can be found [ here.](https://docs.astral.sh/uv/).
Run the following command on the terminal create the necesary environment:

'''
uv sync
'''

### Accessing The Documentation
The documentation explaining the model and implementation is written using the mkdocs package. This can be accessed using the terminal through uv and typing:

'''
uv run mkdocs serve
'''
 and will be hosted locally. 

The documentaion is separated into two sections:
- 'index.md' is the home page
- 'aviation.md' is the documention of the model including constants, equations.



