import requests

class User:
    '''Name or ID'''
    def __init__(self, name: str):
        self.name = name
        auth = {'TRN-Api-Key': '1dd02ede-b940-44f9-bce6-4eb34908ea93'}
        req = requests.get(f'https://public-api.tracker.gg/v2/csgo/standard/profile/kbm/{self.name}', params=auth)
        self.data = req.json()

    def basic_info(self):
        info = {'name': self.data['data']['platformInfo']['platformUserHandle'],
                'picture': self.data['data']['platformInfo']['avatarUrl'],
                'region': self.data['data']['userInfo']['countryCode'],
                'id': self.data['data']['platformInfo']['platformUserId']}
        return info
        
    def time_played(self):
        time = self.data['data']['segments'][0]['stats']['timePlayed']['displayValue']
        return time
    
    def combat_info(self):
        info = {'kills': self.data['data']['segments'][0]['stats']['kills']['displayValue'],
                'deaths': self.data['data']['segments'][0]['stats']['deaths']['displayValue'],
                'score': self.data['data']['segments'][0]['stats']['score']['displayValue'],
                'kd': self.data['data']['segments'][0]['stats']['kd']['displayValue'],
                'damage': self.data['data']['segments'][0]['stats']['damage']['displayValue'],
                'headshots': self.data['data']['segments'][0]['stats']['headshots']['displayValue'],
                'headshotPercentage': self.data['data']['segments'][0]['stats']['headshotPct']['displayValue'],
                'shotsFired': self.data['data']['segments'][0]['stats']['shotsFired']['displayValue'],
                'shotsHit': self.data['data']['segments'][0]['stats']['shotsHit']['displayValue'],
                'shotsAccuracy': self.data['data']['segments'][0]['stats']['shotsAccuracy']['displayValue']}
        return info
    
    def matches_info(self):
        info = {'bombsPlanted': self.data['data']['segments'][0]['stats']['bombsPlanted']['displayValue'],
                'bombsDefused': self.data['data']['segments'][0]['stats']['bombsDefused']['displayValue'],
                'moneyEarned': self.data['data']['segments'][0]['stats']['moneyEarned']['displayValue'],
                'mvp': self.data['data']['segments'][0]['stats']['mvp']['displayValue'],
                'wins': self.data['data']['segments'][0]['stats']['wins']['displayValue'],
                'losses': self.data['data']['segments'][0]['stats']['losses']['displayValue'],
                'ties': self.data['data']['segments'][0]['stats']['ties']['displayValue'],
                'winPercentage': self.data['data']['segments'][0]['stats']['wlPercentage']['displayValue'],}
        return info

#print(User('76561198358702059').basic_info())