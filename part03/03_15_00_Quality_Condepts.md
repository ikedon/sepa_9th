わたしたちの生活のあらゆるところにソフトウェアが急速に入り込んでくるに連れて、ソフトウェアにより良い品質を求める声も出てきた。1990年までには、約束されたはずのフィーチャーや機能性をもたらさないソフトウェアのために毎年何十億ドルもの金が無駄になっていることを、多くの企業が認識していた。さらに悪いことに、ソフトウェアの重大な不具合のために重要なインフラストラクチャーが利用できなくなり、数百億以上のコストになりかねないことを、政府も産業界もますます心配するようになった。今世紀の初めには *『CIO Magazine』* が、「アメリカの産業界が、できるはずのこともできないソフトウェアのために何十億ドルも費やしている」という事実を嘆いて、「毎年780億ドルもの無駄遣いをするのをやめよう」とヘッドラインで吹聴した[Lev01]。悲しいことに、2014年に行われたソフトウェア品質の手法の状況について、少なくとも一つ調査では、ソフトウェア開発の全コストの90%が保守と改修の作業にかかっているとしている[Nan14]。十分なテストもせずに慌てて製品をリリースすることでもたらされる低品質なソフトウェアは、ソフトウェア産業の悩みの種であり続けているのだ。

ソフトウェアの品質は今もって課題のままだが、誰を責めればいいのか。顧客は、いい加減なやり方が低品質なソフトウェアにつながっているとして開発者を責める。開発者は、不合理に設定された提供日程と絶え間ない変更の波のせいで、しっかり検証する前にソフトウェアを提供せざるを得なかったとして、顧客（や他のステークホルダー）を責める。どちらが正しいのか。両方だ。それが問題なのだ。この章では、ソフトウェア品質というコンセプトについて考え、それがソフトウェアエンジニアリングの手法を適用する際にはいつだって熟考に値するといえる理由を考察しよう。

##### キーコンセプト
* 品質のコスト
* 十分によい★
* 負債★
* 機械学習
* 管理活動
* 品質
* 品質のジレンマ
* 品質の次元
* 品質の要素
* 定量的な品質改善
* リスク
* セキュリティ

#### QUICK LOOK★

**これは何？**

あなたが思っているほどには、答えは簡単でない。品質というのは見ればわかるものではあるが、定義するにはなお、つかみどころのないものでもある。しかしコンピューターのソフトウェアにおいては、品質をしっかり定義しなければならないし、それこそがこの章で行うことである。

**誰がそれをやるの？**

全員である。ソフトウェアプロセスに関わる全員、ソフトウェアエンジニア、マネージャー、すべてのステークホルダーに、品質に対する責任がある。

**なぜ重要なの？**

正しくやることもできるし、それを繰り返すこともできる。`★この訳は自信なし。正しいことを繰り返すのか、正しくできずやり直すのか。`ソフトウェアエンジニアリングの活動において、ソフトウェアチームが品質を強調すれば、やらざるを得ない手戻りは減らすことができる。そうすればコストを下げられるし、さらに大事なこととして、製品かまでの時間も改善することができる。

**どんなステップがあるの？**

高品質なソフトウェアを実現するためには、裏付けのあるソフトウェアエンジニアリングのプロセスと手法、堅実なプロジェクトマネジメント、包括的な品質コントロール、品質保証のインフラの存在という、四つの活動を行う必要がある。

**作業成果物 Work Productは何？**

顧客のニーズに合致し、正確かつ信頼性があり、使う人すべてに価値を提供するソフトウェア。

**正しくやれたと自信を持つにはどうすればいい？**

品質コントロールのすべての活動の結果を検証することで品質を追跡し、リリース前のエラーと、フィールドに出てしまった欠陥を検証することで品質を測定する。