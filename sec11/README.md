# Section11


## 本セクションについて

本セクションではカスタムユーザーモデルを定義・作成していきます。

これまで、Djangoのデフォルトのユーザーモデルを使用してきましたが、ここで独自のカスタムユーザーモデルへ作り替えます（＊１）。

元になる参考コードは
https://docs.djangoproject.com/ja/3.2/topics/auth/customizing/#a-full-example
になります。

また、ユーザーモデルは認証に関わるコアな部分のみとし、そのほかのユーザーのプロフィール情報（住所など）について別で`Profile`モデルを実装し、そちらをOneToOneで関連させます。

実装が完了した段階で、データベース等を作り直し、改めてユーザーやアイテムを登録していきます。


＊１　なぜここで行うかにについて「管理画面のセクション説明」を参照してください
