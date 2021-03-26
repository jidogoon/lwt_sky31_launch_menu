from datetime import date

from sky31 import SKY31
from slack.file_reader import FileReader
from slack.slack_helper import SlackHelper

if __name__ == '__main__':
    today_menu = SKY31().get_today_menus()
    if len(today_menu) <= 0:
        print('nothing to do... couldn\'t find menu')
        exit(0)

    today = date.today()
    message = f':lwt: 오늘의 SKY 31 점심메뉴 - {today.year}년 {today.month}월 {today.day}일 :lwt:'
    for menu in today_menu:
        message += f'\n> {menu.menu} ({menu.price:,d}원)'

    hook_urls = FileReader('hook_url.conf', default_value=None).read_lines()
    for hook_url in hook_urls:
        slack = SlackHelper(hook_url=hook_url)
        slack.report_to_slack(message)
