# 設計メモ

## 要件

自然言語のプロンプトをLLMに解釈させ、適切な関数名と入力の持つJSON形式で出力させる

単純にJSON形式に出力するだけでは、小規模のLLMにおける正答率が低くなってしまう。
小規模LLMでも精度を担保するために制約デコーディング

### 機能要件
 - 関数定義ファイルのparsing
 - LLM が出す出力を要求する型に制限
 - LLMに渡した関数定義ファイルに則って出力させる

### 非機能要件
 - JSONの出力を100%正しい形式になるようにする
 - LLMが出す関数の選択と引数の抽出で90%以上の正答率
 - 全てのテストプロンプトを五分以内に処理する
 - 不正な入力、存在しないファイル、エッジケースを適切に処理する

## 制約

 - 出力のJSON形式ではprompt, name, parametersが含まれていないといけない
 - 全てのテストプロンプトは5分以内に処理される必要がある

## 入力と出力

 - 入力
 関数定義
  {
    "name" : 関数名,
    "description": 関数の説明,
    "parameters" : {
        引数: {
            "type": 引数の型,
        }
    },
    "returns" : {
        "type": returnの型
    }
  }
 プロンプト


- 出力
出力の型
{
    {
        "prompt": 入力プロンプト,
        "name": 関数の名前,
        "parameters": {"引数": 引数の具体的な数値}
    }
}


## 処理の分担
 
1. CLI/main.py: 引数解析、実行管理
2. Loaderクラス: JSON読み込み、 pydantic検証
3. FunctionCallingService: LLMに対する入力などの処理を行う
4. ConstrainedDecoding: 制限つきDecodeを行う。
5. JSONFormat: JSONフォーマットに準拠しているか確認
6. LLMクラス: LLMの処理を担当
7. Outputvalidator: 生成完了後、関数名・引数・型が定義に適合しているか検証する
8. Output: 検証済みの結果をJSONファイルに保存する


## 処理シーケンス

1. CLI/main.py(argsを入力)
 初期化、入力処理(function_definitionなどのファイルを読み込む)
2. Loader(ファイルパスを入力として受け取る)
 Pydanticを用いてfunction_definitionの構造に問題がないかを処理
3. FunctionCallingServiceで処理を開始
4. プロンプトを読み込む。
5. LLMクラスを利用してencode, tokenizationを実施。
6. Constrained Decodingを用いて出力を関数、引数の形に制限、JSONFormatで出力
7. OutputValidatorで出力形式が求めるものかどうかを確認
8. Outputにて出力

6. において、logitsで不必要なものを-intfにして繰り返し出力させる

##　詳細設計
ConstrainedDecoding

関数
 step(state, char): 1文字受け取って状態を進める
 walk(state, text): 複数文字を含むトークン全体を試す
 allowed(state, vocab): 許可できるトークンIDを集める
 generate: 候補として正しくないものを-intfにし、選んだトークンで状態を更新

build_index -> BFDの形式で、現在の状態stateと次に移動できる候補をindexにまとめる

## 決めたことと理由

 - JSONの構造制約と、数値・文字列などの型の制約は分離しない
 - 関数の


## 未決定、疑問

