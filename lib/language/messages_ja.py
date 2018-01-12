#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "Nettackerエンジンが始動しました...\n\n",
            "1": "python nettacker.py [options]",
            "2": "Nettackerヘルプメニューを表示する",
            "3": "ライセンスと契約書をお読みくださいhttps://github.com/viraintel/OWASP-Nettacker\n",
            "4": "エンジン",
            "5": "エンジン入力オプション",
            "6": "言語を選択{0}",
            "7": "範囲内のすべてのIPをスキャンする",
            "8": "サブドメインの検索とスキャン",
            "9": "ホストへの接続のスレッド番号",
            "10": "スキャンホストのスレッド番号",
            "11": "すべてのログをファイルに保存する（results.txt, results.html, results.json）",
            "12": "ターゲット",
            "13": "ターゲット入力オプション",
            "14": "ターゲットリスト、 \",\"で区切る",
            "15": "ファイルからターゲットを読み込む",
            "16": "スキャン方法のオプション",
            "17": "スキャン方法{0}を選択してください",
            "18": "スキャン方法を選択して{0}を除外する",
            "19": "ユーザ名リスト、 \",\"",
            "20": "ファイルからユーザー名を読み込む",
            "21": "パスワードのリスト、 \",\"で区切る",
            "22": "ファイルからパスワードを読み込む",
            "23": "ポートリスト、 \",\"",
            "24": "ファイルからパスワードを読む",
            "25": "各リクエストの間にスリープする時間",
            "26": "ターゲットを指定できません",
            "27": "ファイルを開くことができないターゲットを指定することはできません：{0}",
            "28": "100より低いスレッド番号を使用する方が良いです、私たちは続けています...",
            "29": "タイムアウトを{0}秒に設定すると大きすぎますね。私たちが続けているところで...",
            "30": "このスキャンモジュール[{0}]は見つかりませんでした！",
            "31": "このスキャンモジュール[{0}]は見つかりませんでした！",
            "32": "すべてのスキャン方法を除外することはできません",
            "33": "すべてのスキャン方法を除外することはできません",
            "34": "除外するように選択した{0}モジュールが見つかりません！",
            "35": "メソッドの入力を入力します（例： \"ftp_brute_users=test,admin＆ftp_brute_passwds"
                  "=read_from_file：/tmp/pass.txt&ftp_brute_port=21\"",
            "36": "ファイル{0}を読むことができません",
            "37": "ユーザー名を指定できません。ファイルを開くことができません：{0}",
            "38": "",
            "39": "パスワードを指定できません。ファイルを開くことができません：{0}",
            "40": "ファイル \"{0}\"は書き込み可能ではありません！",
            "41": "あなたのスキャン方法を選んでください！",
            "42": "一時ファイルを削除！",
            "43": "結果を並べ替える！",
            "44": "完了！",
            "45": "{2}の{0}、{1}を攻撃し始める",
            "46": "このモジュール\"{0}\" は使用できません",
            "47": "残念ながら、このバージョンのソフトウェアはlinux /osx/windows上で実行できます。",
            "48": "あなたのPythonバージョンはサポートされていません！",
            "49": "重複するターゲットをスキップします（一部のサブドメイン/ドメインには同じIP"
                  "と範囲が含まれることがあります）",
            "50": "不明なタイプのターゲット[{0}]",
            "51": "{0}の範囲をチェックしています...",
            "52": "{0}をチェックしています...",
            "53": "ホスト",
            "54": "ユーザー名",
            "55": "パスワード",
            "56": "ポート",
            "57": "タイプ",
            "58": "DESCRIPTION",
            "59": "冗長モードレベル（0〜5）（デフォルトは0）",
            "60": "ショーソフトウェアバージョン",
            "61": "更新を確認",
            "62": "",
            "63": "",
            "64": "接続タイムアウト（デフォルトは3）",
            "65": "{0}へのFTP接続：{1}タイムアウト、{2}をスキップ：{3}",
            "66": "成功裏にログオン！",
            "67": "成功裏にログに記録され、許可はリストコマンドに拒否されました！",
            "68": "{0}へのftp接続：{1}は{3}の[{2}}プロセス全体をスキップしました！次のステップに進む",
            "69": "{0}モジュールの入力ターゲットはDOMAIN、HTTP、またはSINGLE_IPv4で、"
                  "{1}をスキップする必要があります",
            "70": "ユーザー：{0}合格：{1}ホスト：{2}ポート：{3}が見つかりました！",
            "71": "（リストファイルの許可なし）",
            "72": "{3} {4}：{5}のプロセス{2}で{1}の{0}",
            "73": "{0}へのsmtp接続：{1}タイムアウト、{2}をスキップ：{3}",
            "74": "{0}へのsmtp接続：{1}の全工程[{2}}をスキップしました！次のステップに進む",
            "75": "{0}モジュールの入力ターゲットは、{1}をスキップしてHTTPでなければなりません",
            "76": "{0}へのssh接続：{1}タイムアウト、{2}をスキップ：{3}",
            "77": "{0}へのssh接続が失敗しました。{3}の{{2}}プロセス全体をスキップしました！次のステップに進む",
            "78": "％sへのssh接続：％sは失敗しました。[％sの％sプロセス]をスキップしました！次のステップに進む",
            "79": "オープンポート",
            "80": "ホスト：{0}ポート：{1}が見つかりました！",
            "81": "ターゲット{0}が送信されました。",
            "82": "プロキシリストファイルを開くことができません：{0}",
            "83": "プロキシリストファイルが見つかりません：{0}",
            "84": "OWASP Nettackerのバージョン{0} {1} {2} {6}をコード名{3} {4} {5}で実行しています。",
            "85": "この機能はまだ利用できません。最後のバージョンを取得するには、 \"git clone "
                  "https://github.com/viraintel/OWASP-Nettacker.git\"または \"pip install "
                  "-U OWASP-Nettacker\"を実行してください。",
            "86": "すべての活動と情報のグラフを作成するには、HTML出力を使用する必要があります。利用可能なグラフ：{0}",
            "87": "グラフフィーチャを使用するには、出力ファイル名が \".html\"または \".htm\"で終わる必要があります。",
            "88": "グラフを作成する...",
            "89": "グラフを完成させる！",
            "90": "侵入テストグラフ",
            "91": "このグラフは、OWASP Nettackerによって作成されました。グラフには、すべてのモジュール"
                  "アクティビティ、ネットワークマップ、機密情報が含まれています。信頼できない場合は、この"
                  "ファイルを誰とも共有しないでください。",
            "92": "OWASP Nettackerレポート",
            "93": "ソフトウェアの詳細：{2}のOWASP Nettackerのバージョン{0} [{1}]",
            "94": "開いているポートは見つかりませんでした。",
            "95": "ユーザー/パスワードが見つかりません！",
            "96": "{0}モジュールがロードされました...",
            "97": "このグラフモジュールが見つかりません：{0}",
            "98": "このグラフモジュール \"{0}\"は使用できません",
            "99": "ホストをスキャンする前にping",
            "100": "--ping-before-scanが真であり、応答しなかったため、ターゲット{0}とスキャン方法{1}全体をスキップします！",
            "101": "OWASP Nettackerの最新バージョンを使用していない場合は、更新してください。",
            "102": "アップデートを確認できません。インターネット接続を確認してください。",
            "103": "OWASP Nettackerの最新バージョンを使用しています...",
            "104": "{0}にあるディレクトリリスト",
            "105": "URLの代わりに-gまたは--methods-argsスイッチを使用してポートを挿入してください",
            "106": "http接続{0}タイムアウト！",
            "107": "",
            "108": "ポート{1}の{0}のディレクトリまたはファイルが見つかりません",
            "109": "{0}を開くことができません",
            "110": "dir_scan_http_methodの値はGETまたはHEADでなければなりません。デフォルトはGETに設定されています。",
            "111": "すべてのメソッドargsをリストする",
            "112": "{0}モジュールの引数を取得できません",
            "113": "",
            "114": "",
            "115": "",
            "116": "",
            "117": ""
        }
