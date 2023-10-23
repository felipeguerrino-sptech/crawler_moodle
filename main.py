import requests
import wget

def main():
    ra = input('Insira o RA: ')
    senha = input('Insira a senha: ')
    cookie = get_cookie(ra, senha)
    token = get_github_token(cookie)
    print(token)

def get_cookie(ra, senha):
    s = requests.Session()
    login = s.post('https://moodle.sptech.school/login/index.php', params={'ra': '02231048', 'senha': '#Gf50008690871'})

    return login.cookies['MoodleSession']

def get_github_token(cookie):
    s = requests.Session()
    res = wget.download('https://moodle.sptech.school/draftfile.php/20653/user/draft/727639391/github.txt')

    print(res.status_code)
    return res.content
if __name__ == '__main__':
    main()