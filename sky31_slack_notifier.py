from datetime import date

from sky31 import SKY31
from slack.file_reader import FileReader
from slack.slack_helper import SlackHelper

def num_to_slack_emoji(num: int) -> str:
    if num == 0:
        return ':zero:'
    elif num == 1:
        return ':one:'
    elif num == 2:
        return ':two:'
    elif num == 3:
        return ':three:'
    elif num == 4:
        return ':four:'
    elif num == 5:
        return ':five:'
    return str(num)

if __name__ == '__main__':
    today_menu = SKY31().get_today_menus()
    if len(today_menu) <= 0:
        print('nothing to do... couldn\'t find menu')
        exit(0)

    today = date.today()
    message = f'오늘의 31층 점심메뉴 - {today.year}년 {today.month}월 {today.day}일'
    index = 0
    for menu in filter(lambda m: m.price is not None, today_menu):
        message += f'\n{num_to_slack_emoji(index + 1)} {menu.menu} ({menu.price:,d}원)'
        index += 1
    message += f'\n{num_to_slack_emoji(index + 1)} ' + \
               '/'.join(map(lambda m: m.menu, filter(lambda m: m.price is None, today_menu)))

    hook_urls = FileReader('hook_url.conf', default_value=None).read_lines()
    for hook_url in hook_urls:
        slack = SlackHelper(hook_url=hook_url)
        slack.report_to_slack(message)
