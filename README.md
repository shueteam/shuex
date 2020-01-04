<h1 align="center">shuex</h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white"></img>
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></img>
</p>

## Подготовка группы
1. [Создайте](https://vk.com/groups?w=groups_create) сообщество ВКонтакте, выбрав любой тип и тематику
2. Перейдите в Управление > Настройки > Работа с API и создайте новый ключ с доступом к управлению и сообщениям сообщества, он понадобится позже

## Установка
### На Heroku
Понадобится аккаунт Heroku с привязанной картой (дебетовая карта QIWI подойдёт).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/shueteam/shuex)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fshueteam%2Fshuex.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fshueteam%2Fshuex?ref=badge_shield)

1. Нажмите на кнопку Deploy to Heroku
2. В поле token введите ключ сообщества, полученный в этапе 2 подготовки группы
3. В меню выбора региона выберите Europe для лучшей производительности и нажмите Deploy app
4. После успешного деплоя ваш рейд бот готов разрывать беседы! Никакой дополнительной настройки не требуется

### Локально
1. Установите [Python](https://www.python.org/downloads/) версии не ниже 3.6, если ещё не сделали этого. При установке убедитесь, что отметили галочку ![Add Python to PATH](https://user-images.githubusercontent.com/42045258/69171091-557d2780-0b0c-11ea-8adf-7f819357f041.png)
2. [Скачайте](https://github.com/shueteam/shuex/archive/master.zip) этот репозиторий и распакуйте в любое удобное место
3. Откройте командную строку и введите следующую команду:
```sh
pip install -r requirements.txt --upgrade
```
4. Откройте файл `config.toml` любым текстовым редактором и укажите ключ сообщества, полученный в этапе 2 подготовки группы в поле token
5. Для запуска введите в командную строку `python shuex.py`


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fshueteam%2Fshuex.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fshueteam%2Fshuex?ref=badge_large)