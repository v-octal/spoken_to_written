# spoken_to_written

A module to convert text from a speech recognition system to written format. Spoken english refers to the textual transcript of a speech recognition system.

## Install

It's recommended that you use a virtual environment while using this module.

1. Download or Clone the repository
2. Install it using pip: `pip install spoken_to_written/`

## Usage

Make sure that you have succesfully installed the module.

### Import

`from spoken_to_written import spoken_to_written`

### Create an object

`stw = spoken_to_written.stw()`

**stw** class is responsible for handling the conversion of spoken to written.

You can also pass your set of rules for parsing text:

`stw = spoken_t_written.stw(path_to_rules.json)`

_As of now only json file is supported for rules._

### Parse

`text = "My jersey number is 8"`

`stw.parse(text)`

Output: `'My jersey number is 8'

**stw.parse()** takes in a _string_ and returns a converted _string_.

## Rules

### Format

The rules are written in json format. The format is:

```
{
  "rules": [
    {
      "search": "YOUR SEARCH REGEX 1",
      "replace": "REPLACEMENT REGEX 1",
      "type": "regex"
    },
    {
      "search": "YOUR SEARCH REGEX 2",
      "replace": "REPLACEMENT REGEX 2",
      "type": "regex"
    },
  ]
}
```

###

## Dependency

As of now this module uses [word2number](https://github.com/akshaynagpal/w2n) to convert number in word format to numerical format. word2number has it's limitation. I have an easier and better implementation in mind but it's not high priority and it works for now.

## Future Release

A complete revamp of system. This will allow you to easily extend this library to implement complex logic. It will also allow you to pass your text to a selected set of logic/rules.

Here's a digaram to explain a bit of the revamp:
![image](https://user-images.githubusercontent.com/19239291/70391425-1b13f580-19fb-11ea-8f16-77a31ccc475f.png)

You can check out **component_divison** branch for the implementation of this system. (_It's still under development_)

Apart from this there are few things which can be added to the current version:

1. More regex rules
2. Improve Rule format

##

_Contributions are welcome_
