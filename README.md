![stupygorounded](https://github.com/user-attachments/assets/9e711ac9-d0c1-409f-8512-0e76fc311993)

(THE README IS STILL A W.I.P!!!)

Stu.pyGO is a Free and Open Source Software (FOSS) based on the Python Terminal that allows you to study words efficiently and quickly, much like you can on programs such as Quizlet or StudyGO. This program is designed to provide a reliable studying platform for users who cannot afford other options or would prefer an open-source solution over proprietary alternatives.

## The Basics

Stu.pyGO is built using Python and requires the following to function correctly:

### Requirements
1. **Python** (preferably the latest version: 3.11 at the time of writing)
2. **Pip**, so you can install the required packages.
    - **Tkinter** (for the graphical interface)
      - Install using `pip install tk`

The program is designed to run in the terminal, and it works on both **Windows** and **Linux** operating systems. It should work on any platform that supports Python.

> _I assume that you know how to execute Python programs, so I will not cover the process of running Python scripts._

### Features
- **Study Mode**: A terminal-based word study feature, where you can quickly learn words using a command-line interface.
- **Localization**: The program supports multiple languages for different prompts and feedback (based on detected or selected language settings).
- **Custom Word Sets**: You can input your own word sets, allowing for personalized study sessions.
- **Randomization**: Words can be shuffled, helping you study in a more dynamic and less predictable manner.
- **Efficiency**: Lightweight and fast, focused on delivering an optimal study experience in the terminal.
- **Open Source**: You have full control over the code, allowing you to modify or extend functionality as needed.

### Usage Instructions
  
1. **Language Support**:  
   - Upon starting, the program will ask you to set a language. Currently, there is only support for ENGLISH (en) and DUTCH (nl)

2. **Adding Word Lists**:  
   - The program allows for importing custom word lists through file dialogs, enabled by `tkinter`. A file selection window will appear, allowing you to choose the file containing your study data.

### Known Issues
- On the RANDOM modes there is a chance for the program to crash at the end of the list. This is not consistent.
  
### Future Updates
The current version is **v0.9.9**, and future updates may include:
- Text to speech
- A dynamic mode, giving you an options menu first and then making you type it in
- More in-depth settings

### Contributing
This is my first ever Python project that I've released out to the public, so please feel free to call me out on any programming mistakes I've done! I'm open to any criticism. I'm also open to anyone wanting to make fan translations for the program. I will only accept volunteer work.

