# VegeKet

## はじめに

こちらでは Udemy 講座[【中級者向け】Django でショッピングサイト開発 - EC サイト構築で行う Python・WEB アプリケーション開発講座](https://www.udemy.com/course/django-ecweb-vegeket/?referralCode=47EA4C2DDB607E3500D5) で使用しているソースコードを掲載しています。

- 各セクション終了時点ごとのソースコードを各 sec フォルダへ掲載しています。必要な箇所にご活用ください。

- secrets フォルダは Github には UP していません（UP しない目的のフォルダだからです）。ですので、動画を参考に作成等行ってください（ちなみに皆さんも UP しないようにしましょう）。

- 仮想環境の venv フォルダも Github には UP していません。vegeket フォルダを丸ごと使用する際はご自身の環境で仮想環境を構築してください。

## 講師の環境

- OS：MacOS
- シェル：zsh
- Python：3.9 系
- エディター：VSCode

## 全体構成図/tree

＊ `__pycache__`などのキャッシュフォルダ・ファイルは表示から除外しています。

```
vegeket
├── base
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account_models.py
│   │   ├── item_models.py
│   │   └── order_models.py
│   ├── tests.py
│   └── views
│       ├── __init__.py
│       ├── account_views.py
│       ├── cart_views.py
│       ├── item_views.py
│       ├── order_views.py
│       └── pay_views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── custom_context_processors.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── secrets
│   ├── .env.dev
│   └── .env.prod
├── static
│   └── items
└── templates
    ├── base.html
    ├── pages
    │   ├── account.html
    │   ├── cancel.html
    │   ├── cart.html
    │   ├── index.html
    │   ├── item.html
    │   ├── list.html
    │   ├── login_signup.html
    │   ├── order.html
    │   ├── orders.html
    │   ├── profile.html
    │   └── success.html
    └── snippets
        ├── footer.html
        ├── header.html
        ├── headline.html
        ├── item_add_box.html
        ├── item_box.html
        ├── messages.html
        └── pagination.html
```

## ライブラリ

講座で使用するライブラリは下記になります。

requirements.txt

```txt
asgiref==3.4.1
certifi==2021.5.30
charset-normalizer==2.0.3
Django==3.2.12
django-environ==0.4.5
idna==3.2
Pillow==9.0.0
pytz==2021.1
requests==2.26.0
sqlparse==0.4.2
stripe==2.60.0
urllib3==1.26.6
```

必要な方は、下記手順で一括インストールできます。

1. プロジェクト直下に requirements.txt を用意
2. 仮想環境が有効になっていることを確認
3. `pip install -r requirements.txt`で一括インストール
