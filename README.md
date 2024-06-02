# Online Calorie Tracker [Django Project]

![Language](https://img.shields.io/badge/Language-Python-blue) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/giovannibianchinidebarros/javascript-piano/graphs/commit-activity)

Online Calorie Tracker é uma aplicação web construída com Django para ajudar os usuários a monitorar sua ingestão diária de calorias. Os usuários podem adicionar, visualizar e deletar itens alimentares para monitorar o consumo de carboidratos, proteínas, gorduras e calorias totais.

## Funcionalidades

- Adicionar Itens: Selecionar itens alimentares para adicionar ao consumo diário.
- Visualizar um resumo da ingestão diária de alimentos, incluindo carboidratos, proteínas, gorduras e calorias totais.
- Deletar Itens: Remover itens alimentares da lista diária.
- Limpar Todos os Itens: Limpar todos os itens alimentares da lista para começar do zero.

## Dados

Os dados utilizados para popular o banco de dados deste projeto foram baixados do site [kaggle.com](https://www.kaggle.com/). Dataset: [Nutritional values for common foods and products](https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products).Esses dados incluem informações nutricionais sobre vários alimentos, como carboidratos, proteínas, gorduras e calorias, e foram resumidos em um arquivo csv: [fooditems.csv](https://github.com/giovannibianchinidebarros/Online-Calorie-Tracker/blob/main/trackersite/trackerapp/management/commands/fooditems.csv).

## Como instalar e rodar

1. Clone este repositório em sua máquina local usando o comando bash:

```
git clone https://github.com/giovannibianchinidebarros/Online-Calorie-Tracker.git

cd online-calorie-tracker
```

2. Criar um ambiente virtual:

```
python -m venv venv
venv/Scripts/activate
```

3. Instalar as dependências:

```
pip install -r requirements.txt
```

4. Aplicar migrações:

```
python manage.py migrate
```

5. Criar um superusuário (opcional, para acesso ao admin):

```
python manage.py createsuperuser
```

6. Popular o banco de dados:

   Os dados estão no arquivo: [fooditems.csv](https://github.com/giovannibianchinidebarros/Online-Calorie-Tracker/blob/main/trackersite/trackerapp/management/commands/fooditems.csv).

   Para facilitar, criei um código para extrair todos os itens deste csv diretamente para o banco de dados do projeto.

   Você pode popular o banco de dados com o comando abaixo:

```
python manage.py populateitems
```

7. Executar o servidor de desenvolvimento:

```
python manage.py runserver
```

8. Abra seu navegador e vá para http://127.0.0.1:8000/

## Screenshot

![image](https://github.com/giovannibianchinidebarros/Online-Calorie-Tracker/blob/main/docs/image.png)
