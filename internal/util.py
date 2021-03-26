import re


class Util:
    @staticmethod
    def only_num(text) -> int:
        found_num = re.findall('\d+', text)
        if len(found_num) <= 0:
            return None
        return int(''.join(found_num))
