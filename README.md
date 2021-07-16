# VegeKet

## 全体構成図/tree

```
vegeket
├── base
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
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
├── secrets
│   ├── .env.dev
│   └── .env.prod
├── static
│   ├── items
│   └── vegetables
│       ├── banana.png
│       ├── kyabetsu.png
│       ├── goya.png
│       ├── jyagaimo.png
│       ├── komatsuna.png
│       ├── kyuri.png
│       ├── lemon.png
│       ├── ninjin.png
│       ├── piman.png
│       └── tamanegi.png
├── templates
│   ├── base.html
│   ├── pages
│   │   ├── account.html
│   │   ├── cancel.html
│   │   ├── cart.html
│   │   ├── index.html
│   │   ├── item.html
│   │   ├── list.html
│   │   ├── login_signup.html
│   │   ├── order.html
│   │   ├── orders.html
│   │   ├── profile.html
│   │   └── success.html
│   └── snippets
│       ├── footer.html
│       ├── header.html
│       ├── headline.html
│       ├── item_add_box.html
│       ├── item_box.html
│       ├── messages.html
│       └── pagination.html
├── db.sqlite3
└── manage.py
```
