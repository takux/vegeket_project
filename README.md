# 【中級者向け・Django4対応】Python/DjangoによるECサイト開発講座（Django3.2系にも対応）

## はじめに

こちらでは Udemy講座 で使用しているソースコードを掲載しています。

<!-- [【中級者向け】Django でショッピングサイト開発 - EC サイト構築で行う Python・WEB アプリケーション開発講座](https://www.udemy.com/course/django-ecweb-vegeket/?referralCode=47EA4C2DDB607E3500D5)-->

=> [定期的にクーポンを発行しているコース一覧ページはこちら](https://takux.one)。

本リポジトリについて、

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

[requirements.txt](https://github.com/takux/vegeket_project/blob/main/requirements.txt)


必要な方は、下記手順で一括インストールできます。

1. プロジェクト直下に [requirements.txt](https://github.com/takux/vegeket_project/blob/main/requirements.txt) と同じ中身のファイルを用意します。
2. 仮想環境が有効になっていることを確認し、
3. `pip install -r requirements.txt` をターミナルで実行します。

## 3.2系をインストールする場合

直接 3.2系をインストールするか、
```
pip install --upgrade "Django==3.2.*"
```

次のrequriementsファイルを使用していただいても構いません。
```
pip install --upgrade -r requirements-v3.2.txt
``` 


### 既にインストール済みのライブラリのアップデート

仮想環境が有効になっていることを確認した上で、次のようにしてアップデートできます。

```
pip install -U <ライブラリ>
```
