import re


class TagManipulator():
    def parse_string(self, tags, regex=","):
        result = []

        tempResult = re.split(regex, tags)
        for token in tempResult:
            if token.strip():
                result.append(token.strip())

        return result
