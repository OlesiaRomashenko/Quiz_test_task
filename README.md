# API-сервер для сайта викторины

## Как запустить

В корне репозитория находится файл .env.example, его необходимо переименовать в .env и заполнить значениями для старта, а именно

 - POSTGRES_PASSWORD - пароль для пользователя базы данных (БД)
 - POSTGRES_USER - логин для пользователя базы данных
 - POSTGRES_DB - название базы данных
 - POSTGRES_PORT - порт для подключения к базе данных
 - POSTGRES_HOST - хост для подключения к базе данных
 - POSTGRES_ENGINE - драйвер для подключения к БД
 - API_TITLE - заголовок документации
 - API_DESCRIPTION - описание сервиса
 - API_SUMMARY - сводка о приложении
 - API_DOCS_URL - ссылка, по которой доступна документация АПИ

Для запуска приложения необходимо выполнить следующие команды в терминале:

`
git clone git@github.com:OlesiaRomashenko/Quiz_test_task.git
`

`
cd Quiz_test_task
`

Произвести манипуляции с .env файлом (см указания выше).

`
docker-compose up -d
`

## Примеры запросов

`
curl -X 'POST' \
  'http://0.0.0.0:8000/api/question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 2
}'
`

## Требования к системе

 - docker
 - docker-compose
 - curl
 - свободные порты (5432, 8000)
