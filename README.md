# VegeKet

## Udemy 講座

- 各セクション終了時点ごとのソースコードを各 sec フォルダへ掲載しています。必要な箇所にご活用ください。

- secrets フォルダは Github には UP していません（UP しない目的のフォルダだからです）。ですので、動画を参考に作成等行ってください（ちなみに皆さんも UP しないようにしましょう）。

- 仮想環境の venv フォルダも Github には UP していません。vegeket フォルダを丸ごと使用する際はご自身の環境で仮想環境を構築してください。

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
