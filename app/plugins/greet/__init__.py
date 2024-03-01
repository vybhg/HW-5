from app.commands import Command


class GreetCommand(Command):
    def execute(self, *args):
        print("Hello, World!")