from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

class CustomCompleter(Completer):
    
    def __init__(self, commands: list) -> None:
        super().__init__()
        self.commands = commands

    def get_completions(self, document, complete_event):
        current_input = document.text.lower()
        for command in self.commands:
            if command.lower().startswith(current_input):
                yield Completion(command, start_position=-len(current_input))
   
class Prompt:
    
    def __init__(self, mouse_support=False) -> None:
        self.session = PromptSession()
        self.mouse_support = mouse_support

    def prompt(self, message: str, commands: list, style: str = '') -> str:

        color_style = Style.from_dict({
            'prompt': style
        }) if style else None
        
        return self.session.prompt(
            message=[('class:prompt', message)],
            completer=CustomCompleter(commands),
            style=color_style,
            mouse_support=self.mouse_support
        )