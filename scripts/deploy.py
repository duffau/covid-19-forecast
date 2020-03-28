from subprocess import call
from datetime import datetime


def deploy():
    date_str = datetime.now().strftime('%Y-%m-%d')
    commit_tag = 'v' + date_str
    commit_msg = f'Deployed forecast {date_str}'

    call(f'git commit -am "{commit_msg}"', shell=True)
    call(f'git tag {commit_tag}', shell=True)
    call('git push origin master --tags', shell=True)


if __name__ == '__main__':
    deploy()
