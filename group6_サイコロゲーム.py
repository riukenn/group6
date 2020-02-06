import random

def setRule():
    istoSet = input('ゲーム関連ルールの設定を開始するかどうか：（はいを入力すると設定に入り、その他はデフォルトを使用します。）')
    game_Num = 3
    game_Money = 10
    one_Game = 1
    if istoSet == 'はい':
        gameNum = input("いくつかのサイコロをプレイするように設定してください。")
        if gameNum.isdigit():
            if int(gameNum) > 0:
                game_Num = int(gameNum)
            else:
                print("入力誤りは，デフォルト値を採用する。")
        else:
            print("入力誤りは，デフォルト値を採用する。")
        gameMoney = input("初期金額を設定してください。")
        if gameMoney.isdigit():
            if int(gameMoney) > 0:
                game_Money = int(gameMoney)
            else:
                print("入力誤りは，デフォルト値を採用する。")
        else:
            print("入力誤りは，デフォルト値を採用する。")
        oneGame = input("試合毎の投入金額を設定してください。（数字を入力してください。0より大きいだけではなく、初期金額より小さい必要があります。他のものを入力する場合は標準を使用します。）")
        if oneGame.isdigit():
            if int(oneGame) > 0 and int(oneGame) <= game_Money:
                one_Game = int(oneGame)
            else:
                print("入力誤りは，デフォルト値を採用する。")
        else:
            print("入力誤りは，デフォルト値を採用する。")
    else:
        print("設定完了おめでとうございます。")
    data = [game_Num,game_Money,one_Game]
    return data
 

def myGame():
    data=setRule()
    game_Num = data[0]
    game_Money1 = data[1]
    game_Money2 = data[1]
    one_Game = data[2]
    print( 'サイコロ'+str(game_Num) + 'つを大サイズゲームより開始します。')
    while game_Money1 > 0 and game_Money2 > 0:
        print("現在の資産:",game_Money1,",AIの現在の資産：",game_Money2)
        choice = ['大', '小']
        user_choice = input('大のを買うかそれとも小のを買うか:')
        number = game_Num
        if user_choice in choice:
            points = []
            bigest = game_Num * 6
            smallest = game_Num
            data = get_median(smallest, bigest)
            while number > 0:
                point = random.randrange(1, 7)
                points.append(point)
                number = number - 1
            total = sum(points)
            big = data[0] <= total <= bigest
            small = smallest <= total <= data[1]
            win = (big and user_choice == '大') or (small and user_choice == '小')
            if win:
                print('合計点数は:' + str(total) + '勝利おめでとうございます！')
                game_Money1 = game_Money1 + one_Game
                game_Money2 = game_Money2 - one_Game
            else:
                print('合計点数は:' + str(total) + '残念ですが、失敗しました！')
                game_Money1 = game_Money1 - one_Game
                game_Money2 = game_Money2 + one_Game
        else:
            print('「大」または「小」を入力してください。')
    else:
        if game_Money1 <= 0:
            print("もうお金がないので、ゲームは終わります！")
        else:
            print("相手はもう破産しました。最後の勝利をおめでとうございます！")
 
def get_median(number1, number2):
    data = []
    while number1 <= number2:
        data.append(number1)
        number1 = number1 + 1
    data.sort()
    half = len(data) // 2
    lists = [data[half], data[~half]]
    return lists
 
 
if __name__ == '__main__':
    myGame()