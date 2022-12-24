class Solution:
    def interpret(self, command: str) -> str:

        # List to contain the parsed string and command map to map the command
        parsed = []
        command_map = {
            "G" : "G",
            "()" : "o",
            "(al)" : "al"
        }
        alphabet = ""

        # Iterate over command and map it
        for char in command:

            alphabet += char

            if alphabet in command_map:
                parsed.append(command_map[alphabet])
                alphabet = ""
        
        parsed = "".join(parsed)
        
        return parsed