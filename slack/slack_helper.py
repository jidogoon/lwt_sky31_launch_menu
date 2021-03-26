import json
import requests


class SlackHelper:
    def __init__(self, hook_url: str):
        self.hook_url = hook_url

    def report_to_slack(self, content: str):
        if self.hook_url is None:
            raise Exception('check conf!')

        print(f'post message [{content}] to slack')
        payload = {"text": content}

        requests.post(
            self.hook_url, data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
