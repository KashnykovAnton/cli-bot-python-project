from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

class CustomCompleter(Completer):
    
    def __init__(self, commands: list, all_commands: bool = False) -> None:
        super().__init__()
        self.commands = commands
        self.all_commands = all_commands

    def get_completions(self, document, complete_event):
        for command in self.commands:
            if (
                command[: len(document.current_line)] != document.current_line
                and not self.all_commands
            ):
                continue
            yield Completion(
                command,
                start_position=-len(document.current_line),
                style="bg:#F5F5DC fg:ansiblack",
                selected_style="fg:orange bg:ansiblack",
            )


class Prompt():
    
    def __init__(self, mouse_support=False) -> None:
        self.session = PromptSession()
        self.mouse_support = mouse_support

    def prompt(
        self,
        message: str,
        commands: list,
        all_commands: bool = False,
        style: str = ''
    ) -> str:
        
        color_style = Style.from_dict({'prompt': style})
        return self.session.prompt(
            message=[('class:prompt', message)],
            completer=CustomCompleter(commands, all_commands),
            style=color_style,
            mouse_support=self.mouse_support
        )

    def styled_prompt(
        self,
        styled_message: list,
        commands: list,
        all_commands: bool = False
    ) -> str:
        
        message = []
        styles = {}
        for i, (msg, style) in enumerate(styled_message.items()):
            message.append((f"class:prompt{i}", msg))
            styles[f"prompt{i}"] = style

        color_style = Style.from_dict(styles)
        return self.session.prompt(
            message=message,
            completer=CustomCompleter(commands, all_commands),
            style=color_style,
            mouse_support=self.mouse_support
        )
