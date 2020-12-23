# textlint設定ルール

textlintに設定したルール一式をまとめておきます。

基本、[こちらのスプレッドシート](https://docs.google.com/spreadsheets/d/1dLg0KlA861Vpdyo1fiYT441r_cJOJ5Gb/edit#gid=941388480)を確認ください。

## 用語揺らぎルール一覧

以下スプレッドシートから確認ください。（後者はrule.ymlを見るほうが早いです）

- [spellcheck_tech_word参照用語揺らぎルール](https://docs.google.com/spreadsheets/d/1dLg0KlA861Vpdyo1fiYT441r_cJOJ5Gb/edit#gid=246555494)
- [rule.yml独自設定用語揺らぎルール](https://docs.google.com/spreadsheets/d/1dLg0KlA861Vpdyo1fiYT441r_cJOJ5Gb/edit#gid=631667513)


## .textlintrc設定ルール一覧

.textlintrcにもコメントで確認しやすくしてますが、参考としてください。また、[スプレッドシート](https://docs.google.com/spreadsheets/d/1dLg0KlA861Vpdyo1fiYT441r_cJOJ5Gb/edit#gid=941388480)に参考情報含めて置いておきます。

※今後は↑をアップデート予定です。

以下表の「警告」という記載は判定が厳しいためエラーではなく警告が出るようにしております。


|ルール/ルール内設定|設定値|設定の意味|警告|
|:--------|:----|:--------|:----|
|textlint-filter-rule-comments | TRUE | `<!-- textlint-disable -->`で対象範囲を除外する | 
| textlint-filter-rule-allowlist | TRUE | 元Whitelist、許可用語を入れる | |
| textlint-rule-prh | - | rule.ymlでユーザ定義の揺らぎ対策をチェック | |
| textlint-rule-spellcheck-tech-word | TRUE | JavaScript関連の用語を辞書＋Web DB用語を<br>元にチェックする日本語向けのルール　※別シート参考 | |
| textlint-rule-preset-ja-technical-writing | TRUE | 技術文書用ルールセット（下記に詳細） | |
| &ensp;sentence-length | 120 | 1文の長さは100文字以下とする：長過ぎる文は読みにくさに繋がる | 警告 |
| &ensp;max-comma | 3 | カンマは1文中に3つまで：カンマ（,）の多用は、文が長くなっている可能性があります。 | |
| &ensp;max-ten | 4 | 読点は1文中に4つまで：読点（、）の多用は、文が長くなっている可能性があります。 | 警告 |
| &ensp;max-kanji-continuous-len | 7 | 連続できる最大の漢字長は7文字まで：漢字同士が連続していると読みにくさにつながります。 | |
| &ensp;arabic-kanji-numbers | TRUE | 漢数字と算用数字を使い分けます：数量を表現し、数を数えられるものは算用数字を使用します。 | |
| &ensp;no-mix-dearu-desumasu | である設定 | 「ですます調」、「である調」を統一します。 | |
| &ensp;ja-no-mixed-period | 。をチェック | 文末の句点記号として「。」を使います：文末には「。」を使い文を区切ります。 |  |
| &ensp;no-double-negative-ja | TRUE | 二重否定は使用しない |  |
| &ensp;no-dropping-the-ra | TRUE | ら抜き言葉を使用しない |  |
| &ensp;no-doubled-conjunctive-particle-ga | TRUE | 逆接の接続助詞「が」を連続して使用しない：特に否定の意味ではなくても安易に使われてしまいがちです。 |  |
| &ensp;no-doubled-conjunction | TRUE | 同じ接続詞を連続して使用しない |  |
| &ensp;no-doubled-joshi | min_interval 1 | 同じ助詞を連続して使用しない | 警告 |
| &ensp;no-nfd | TRUE | UTF8-MAC 濁点を使用しない：文章中にUTF8-MAC 濁点は不要です。 |  |
| &ensp;no-invalid-control-character | TRUE | 不必要な制御文字を使用しない：改行(\n)やタブ(\t)以外の不自然な制御文字が入るのを防止します。 |  |
| &ensp;no-exclamation-question-mark | FALSE | 感嘆符!！、感嘆符?？を使用しない |  |
| &ensp;no-hankaku-kana | TRUE | 半角カナを使用しない：全角カタカナを使用してください。 |  |
| &ensp;ja-no-weak-phrase | TRUE | 弱い日本語表現の利用を使用しない：かもしれない 等の弱い表現を使用しない。 |  |
| &ensp;ja-no-successive-word | TRUE | 同一の単語を間違えて連続しているのをチェックする：誤字の可能性があります。 |  |
| &ensp;ja-no-abusage | TRUE | よくある日本語の誤用をチェックする | 警告 |
| &ensp;ja-no-redundant-expression | TRUE | 冗長な表現をチェックする："することができる"という冗長な表現を"できる"にするといったルール | 警告 |
| &ensp;ja-unnatural-alphabet | TRUE | 入力ミスで発生する不自然なアルファベットをチェックする |  |
| &ensp;no-unmatched-pair | TRUE | 対になっていない括弧をチェックする：1文中で(に対応する)がない場合などの括弧の対応関係 | 警告 |
| textlint-rule-preset-ja-spacing | TRUE | 日本語のスペースチェック用ルールセット（下記に詳細） | |
| &ensp;ja-space-between-half-and-full-width | FALSE | 半角文字と全角文字の間にスペースを入れるかどうかのルール デフォルトはスペースを入れない。 |
| &ensp;ja-space-around-code | TRUE | インラインコードの周りにスペースを入れるかを決めるルール |
| &ensp;ja-no-space-between-full-width | TRUE | 全角文字同士の間のスペースについてのtextlintルール。 全角文字どうしの間にスペースを入れません。 |
| &ensp;ja-nakaguro-or-halfwidth-space-between-katakana | TRUE | カタカナ語間の区切り文字についてのtextlintルール。 カタカナ語間は中黒、半角スペースで区切る。 |
| &ensp;ja-no-space-around-parentheses | FALSE | かっこの外側、内側ともにスペースを入れないようにするルール |
| &ensp;ja-space-after-exclamation | TRUE | 文末に感嘆符を使用し、後に別の文が続く場合は、直後に全角スペースを挿入します。 |
| &ensp;ja-space-after-question | TRUE | 文末に疑問符を使用し、後に別の文が続く場合は、直後に全角スペースを挿入します。 |
| textlint-rule-period-in-list-item | FALSE | 箇条書きのピリオド、句点のチェック | |
| textlint-rule-ja-hiragana-keishikimeishi | TRUE | 漢字よりもひらがなで表記したほうが読みやすい形式名詞を指摘（prh） | |
| textlint-rule-ja-hiragana-fukushi | TRUE | 漢字よりもひらがなで表記したほうが読みやすい副詞を指摘します（prh） | |
| textlint-rule-ja-hiragana-hojodoushi | TRUE | 漢字よりもひらがなで表記したほうが読みやすい補助動詞を指摘します（prh） | |
| textlint-rule-no-mixed-zenkaku-and-hankaku-alphabet | TRUE | 全角と半角アルファベットを混在をチェックするtextlintルール | |
| textlint-rule-footnote-order | TRUE | 引用の順序をチェック | |

