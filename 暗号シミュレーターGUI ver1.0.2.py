import tkinter as tk
import unicodedata
import random

#暗号文を格納するためのリスト
ciphertext_list=[]
#平文を英数字に変更した文字列をリストに変更する
change_plaintext_list=[]
#pass_codeを格納するためのリスト
pass_code_list=[]
#復号化の計算をするためのリスト
decode_list=[]
#平文を格納するためのリスト
plaintext_list=[]

#リストは乱数を用いる場合に扱う
random_list1=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i",
       "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


#辞書は左の文字を右の文字に変更する場合に扱う
dic1= {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',
       12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',
       23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x', 
       34:'y',35:'z'}

dic2= {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'a',11:'b',12:'c',13:'d',14:'e',
       15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',
       26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x', 34:'y',35:'z'}

dic3= {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,
       "c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,
       "n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,
       "y":34,"z":35}

dic4= {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"a":10,"b":11,"c":12,"d":13,"e":14,
       "f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,
       "q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}




class EncryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("暗号化シミュレーター")
        self.widgets = []
        self.encryption_home()
        
    #暗号化のGUI
    def encryption_home(self):
        fnt1=("Yu Gothic UI",15)
        fnt2=("Yu Gothic UI",20)
        fnt3=("Yu Gothic UI",25)
        fnt4=("Yu Gothic UI",40)
        
        # タイトル
        self.title = tk.Label(self.master, text="暗号化シミュレーター", font=fnt4)
        self.title.grid(row=0,rowspan=2, column=0, columnspan=7, sticky="ew")
        self.widgets.append(self.title)
        
        # 暗号化ラベル
        self.encryption_label = tk.Label(self.master, text="暗号化", font=fnt3)
        self.encryption_label.grid(row=2, column=0)
        self.widgets.append(self.encryption_label)
        
        # 暗号化→復号化にするボタン
        self.switching_button = tk.Button(self.master, text="復号化に切り替え", command=self.change, font=fnt2)
        self.switching_button.grid(row=2, column=5,columnspan=2, sticky="ew")
        self.widgets.append(self.switching_button)
        
        
        # 注意事項
        self.precautionary_statements_one = tk.Label(self.master, text="暗号化させたい文章を入力してください！", font=fnt2)
        self.precautionary_statements_one.grid(row=3, column=0, columnspan=4, sticky=tk.W)
        self.widgets.append(self.precautionary_statements_one)
        self.precautionary_statements_two = tk.Label(self.master, text="※ただし、暗号化可能な文章はひらがな、カタカナ、数字、一般的な記号となっています。　　　　　　　", font=fnt1,fg="red")
        self.precautionary_statements_two.grid(row=4, column=0, columnspan=6, sticky=tk.W)
        self.widgets.append(self.precautionary_statements_two)
        
        # 平文ラベル
        self.plaintext_label = tk.Label(self.master, text="平文", font=fnt3)
        self.plaintext_label.grid(row=5, column=0,sticky="w",padx=15)
        self.widgets.append(self.plaintext_label)
        
        #平文のテキストボックス
        self.plaintext_textbox = tk.Text(self.master, font=("",20), height=4, width=57)
        self.plaintext_textbox.grid(row=5, rowspan=4, column=1, columnspan=8,padx=15,pady=20)
        self.widgets.append(self.plaintext_textbox)
        
        # 暗号化ボタン
        self.encryption_button = tk.Button(self.master, text="暗号化", command=self.encryption_processing, font=fnt1, bg="skyblue")
        self.encryption_button.grid(row=9, column=6, pady=15, sticky="ew")
        self.widgets.append(self.encryption_button)
        
        self.master.grid_anchor(tk.N)


    #復号化のGUI
    def decryption_home(self):
        fnt1=("Yu Gothic UI",15)
        fnt2=("Yu Gothic UI",20)
        fnt3=("Yu Gothic UI",25)
        fnt4=("Yu Gothic UI",40)
        
        # タイトル
        self.title = tk.Label(self.master, text="暗号化シミュレーター", font=fnt4)
        self.title.grid(row=0, rowspan=2, column=0, columnspan=8, sticky="ew")
        self.widgets.append(self.title)
        
        # 復号化ラベル
        self.decryption_label = tk.Label(self.master, text="復号化", font=fnt3)
        self.decryption_label.grid(row=2, column=0, sticky="ew")
        self.widgets.append(self.decryption_label)
        
        # 復号化→暗号化にするボタン
        self.switching_button = tk.Button(self.master, text="暗号化に切り替え", command=self.change, font=fnt2)
        self.switching_button.grid(row=2, column=6,columnspan=2, sticky="ew")
        self.widgets.append(self.switching_button)
        

        # 注意事項
        self.precautionary_statements_one = tk.Label(self.master, text="解きたい暗号文とパスワードを入力してください！", font=fnt2)
        self.precautionary_statements_one.grid(row=3, column=0, columnspan=4, sticky=tk.W)
        self.widgets.append(self.precautionary_statements_one)
        self.precautionary_statements_two = tk.Label(self.master, text="※ただし、暗号文とパスワードは両方数字もしくは英単語であり、文字列の長さが等しくなければなりません。", font=fnt1,fg="red")
        self.precautionary_statements_two.grid(row=4, column=0, columnspan=7, sticky=tk.W)
        self.widgets.append(self.precautionary_statements_two)

        
        # 暗号文ラベル
        self.encryption_label = tk.Label(self.master, text="暗号文", font=fnt3)
        self.encryption_label.grid(row=5, column=0, sticky="ew")
        self.widgets.append(self.encryption_label)
        
        #暗号文のテキストボックス
        self.encryption_textbox = tk.Text(self.master, font=("",20), height=4, width=57)
        self.encryption_textbox.grid(row=5, rowspan=4, column=1, columnspan=8,padx=15,pady=20)
        self.widgets.append(self.encryption_textbox)
        
        # passラベル
        self.pass_label = tk.Label(self.master, text="pass", font=fnt3)
        self.pass_label.grid(row=10, column=0, sticky="ew")
        self.widgets.append(self.pass_label)
        
        #passのテキストボックス
        self.pass_textbox = tk.Text(self.master, font=("",20), height=4, width=57)
        self.pass_textbox.grid(row=10, rowspan=4, column=1, columnspan=8,padx=15,pady=10)
        self.widgets.append(self.pass_textbox)
        
        # 復号化ボタン
        self.decryption_button = tk.Button(self.master, text="復号化", command=self.decryption_processing, font=fnt1, bg="skyblue")
        self.decryption_button.grid(row=14, column=7,pady=10, sticky="ew")
        self.widgets.append(self.decryption_button)
        
        self.master.grid_anchor(tk.N)


    #切り替えボタン
    def change(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.widgets.clear()
        if self.switching_button.cget("text") == "復号化に切り替え":
            self.decryption_home()
        else:
            self.encryption_home()
        
        
    #暗号化処理と結果
    def encryption_processing(self):
        plaintext = self.plaintext_textbox.get("1.0", tk.END).strip()
        ciphertext,pass_code=self.encryption_mainprocessing(plaintext)
        # 2つ目のメインウィンドウを作成
        encryption_window = tk.Toplevel()
        encryption_window.title("暗号処理結果")
        encryption_window.geometry("800x450")
        if pass_code==-1:
            # 暗号ラベル
            encryption_label = tk.Label(encryption_window, font=("",20),text="暗号")
            encryption_label.place(x=10,y=20)
            # テキストボックスに暗号を出力
            encryption_resultbox = tk.Text(encryption_window,font=("",20), height=6, width=50)
            encryption_resultbox.place(x=80,y=20) 
    
            # passラベル
            pass_label = tk.Label(encryption_window,font=("",20), text="pass")
            pass_label.place(x=10,y=200)
            # テキストボックスにpassを出力
            pass_resultbox = tk.Text(encryption_window,font=("",20), height=6, width=50)
            pass_resultbox.place(x=80,y=200)
            
            #Errorメッセージ
            errormessage_label = tk.Label(encryption_window, font=("",20),text=f"{ciphertext}",fg="red")
            errormessage_label.place(x=10,y=400)
            
        else:
            # 暗号ラベル
            encryption_label = tk.Label(encryption_window, font=("",20),text="暗号")
            encryption_label.place(x=10,y=20)
            # テキストボックスに暗号を出力
            encryption_resultbox = tk.Text(encryption_window,font=("",20), height=6, width=50)
            encryption_resultbox.place(x=80,y=20)
            encryption_resultbox.insert(tk.END, f"{ciphertext}")  
    
            # passラベル
            pass_label = tk.Label(encryption_window,font=("",20), text="pass")
            pass_label.place(x=10,y=200)
            # テキストボックスにpassを出力
            pass_resultbox = tk.Text(encryption_window,font=("",20), height=6, width=50)
            pass_resultbox.place(x=80,y=200)
            pass_resultbox.insert(tk.END, f"{pass_code}")  
        # メインループ
        encryption_window.mainloop()


    #暗号化のメイン処理
    def encryption_mainprocessing(self,plaintext):
        #平文を英数字に変更した文字列をリストに変更する
        change_plaintext_list=[]
        
        error_message_one="文字が入力されていません！"
        error_message_two="漢字もしくは対応していない記号を暗号化することができません！"
        error_message_three="文字数が多すぎます！"
        
        if plaintext=="":
            return error_message_one,-1
        else:
            #plaintextの文の全角の英単語を半角に直す処理を行う
            plaintext=unicodedata.normalize('NFKC', plaintext)
            #plaintextを英数字に変換してchange_plaintextに代入する
            change_plaintext=self.change1(plaintext)
            #random_number1は3~9までの数字の乱数
            random_number1=int(random.randint(3,9))
            #random_number2は0~zまでの英数字を含む乱数
            random_number2=random.choice(random_list1)
            #change_plaintextに格納されている英数字をリストであるchange_plaintext_listに格納
            for i in change_plaintext:
                change_plaintext_list.append(i)
            #暗号化の計算
            try:
                ciphertext_list,pass_code_list=self.encryption(change_plaintext,change_plaintext_list,random_number1,random_number2)
            #漢字やその他の記号が入っていたときにエラーとなる。
            except ValueError:
                return error_message_two,-1
            else:
                #dummy1とdummy2はダミー文字
                dummy1=pass_code_list[-2]
                #passが0~zを超えていないか判断する（超えていた場合Noneが1つ以上ある状態となる）
                if pass_code_list.count(None)>0:
                   return error_message_three,-1
                else:
                    #passに乱数を用いる
                    if pass_code_list[-1]=="z":
                        dummy2=pass_code_list[-1]
                    else:
                        dummy2=int(random.randint(0,1))+dic4[pass_code_list[-1]]
                    dummy2=dic1.get(dummy2)
                    #求めた暗号を二つの乱数を暗号の後ろに代入してciphertextを作成する
                    ciphertext=''.join(ciphertext_list)+str(random_number1)+str(random_number2)
                    #求めたpass_code_listをダミー文字二つを暗号の後ろに代入してpass_codeを作成する
                    pass_code=''.join(map(str, pass_code_list))+str(dummy1)+str(dummy2)
                    #結果の出力
                    return ciphertext,pass_code
            
    
    #復号化処理と結果
    def decryption_processing(self):
        encryptiontext = self.encryption_textbox.get("1.0", tk.END).strip()
        passtext = self.pass_textbox.get("1.0", tk.END).strip()
        decryption_text,error_message=self.decryption_mainprocessing(encryptiontext,passtext)
        # 2つ目のメインウィンドウを作成
        decryption_window = tk.Toplevel()
        decryption_window.title("復号化処理結果")
        decryption_window.geometry("820x250")
        if  error_message==-1:
            # 復号ラベル
            decryption_label = tk.Label(decryption_window, font=("",20),text="復号文")
            decryption_label.place(x=10,y=20)
            # テキストボックスに暗号を出力
            decryption_resultbox = tk.Text(decryption_window,font=("",20), height=6, width=50)
            decryption_resultbox.place(x=100,y=20)
            #Errorメッセージ
            errormessage_label = tk.Label(decryption_window, font=("",20),text=f"{decryption_text}",fg="red")
            errormessage_label.place(x=10,y=200)
            
        else:
            # 復号ラベル
            decryption_label = tk.Label(decryption_window, font=("",20),text="復号文")
            decryption_label.place(x=10,y=20)
            # テキストボックスに暗号を出力
            decryption_resultbox = tk.Text(decryption_window,font=("",20), height=6, width=50)
            decryption_resultbox.place(x=100,y=20)
            decryption_resultbox.insert(tk.END, f"{decryption_text}")  

        # メインループ
        decryption_window.mainloop()
        
        
    #復号文のメイン処理
    def decryption_mainprocessing(self,encryptiontext,passtext):
        #平文を英数字に変更した文字列をリストに変更する
        change_plaintext_list=[]
        #plaintext_listの初期化
        plaintext_list=[]
        error_message_one="文字が入力されていません！"
        error_message_two="暗号またはパスワードは合っていません！"
        error_message_three="復号化処理にエラーが発生しました！"
        if encryptiontext=="":
            return error_message_one,-1
        elif len(encryptiontext)%2==0:
            for i in encryptiontext:
                change_plaintext_list.append(i)
            #ダミー文字を抜いた暗号文
            ciphertext_nodummy=change_plaintext_list[:-2]
            #偶数の乱数
            random_number1=change_plaintext_list[-2]
            #奇数の乱数
            random_number2=change_plaintext_list[-1]
            #passと暗号文が等しくないならエラーが起こる
            if len(encryptiontext)==len(passtext):
                #復号化の計算を行う
                #ciphertext_nodummyは暗号文、random_number1は一つ目の乱数、random_number2は二つ目の乱数、passtextはpass
                try:
                    decode_list=self.decode(ciphertext_nodummy,random_number1,random_number2,passtext)

                except ValueError:
                    return error_message_two,-1
                else:
                    #元に戻した平文の英数字を文字に戻す作業をし平文に変更する
                    for i in range(0,len(decode_list),2):
                        #decode_twotextという文字に二つの英数字の格納
                        decode_twotext=''.join(decode_list[i:i+2])
                        #格納した二つの文字を一つの文字に変更する
                        plaintext_one=self.change2(decode_twotext)
                        #文字をplaintext_listに格納する
                        plaintext_list.append(str(plaintext_one))
                    #文字の変換エラーの対処
                    if any("None" in judgement for judgement in plaintext_list):
                        return error_message_three,-1
                    else:
                        #格納した文字を取り出す作業を行う
                        plaintext=''.join(plaintext_list)
                        #結果の出力
                        return plaintext,0
            else:
                return error_message_two,-1
        else:
            return error_message_two,-1
            
            
    #暗号化の計算
    def encryption(self,change_plaintext,change_plaintext_list,random_number1,random_number2):
        #passに格納するための値
        pass_one=0
        #暗号文を格納するためのリスト
        ciphertext_list=[]
        #pass_codeを格納するためのリスト
        pass_code_list=[]
        #change_plaintextに格納を行った文字数分処理を行う
        for i in range(len(change_plaintext)):
            #英数字の偶数の部分（0~9）
            if i%2==0:
                #該当する数字と一つ目の乱数と文字の順番を足した数がcipher_oneに代入される
                #そして、iの場所が11なら3、７なら2、５なら１が足される
                if i%11==0:
                    cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+3
                elif i%7==0:
                    cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+2
                elif i%5==0:
                    cipher_one=int(change_plaintext_list[i])+random_number1+int(i)+1
                else:
                    cipher_one=int(change_plaintext_list[i])+random_number1+int(i)
                #cipher_oneが36を超えたら36を超えなくなるまでcipher_oneを36で引き続ける
                #cipher_oneから36を弾き続けた回数がpass_oneに代入される。
                #そのpass_oneが9未満ならそのままで、10を超えたらa~zの文字に置き換わり、pass_code_listに格納される。
                #cipher_oneは0~zに文字が置き換わり、ciphertext_listに格納される。
                if cipher_one >=36:
                    while cipher_one>=36:
                        cipher_one-=36
                        pass_one+=1
                    if pass_one>=10:
                        pass_one=dic1.get(pass_one)
                    cipher_one=str(dic1.get(cipher_one))
                    ciphertext_list.append(cipher_one)
                    pass_code_list.append(pass_one)
                    pass_one=0
                #cipher_oneが35以下ならcipher_oneが0~zに変更され、ciphertext_listに格納される。
                #そして、pass_code_listには0が格納される。
                else:
                    cipher_one=str(dic1.get(cipher_one))
                    ciphertext_list.append(cipher_one)
                    pass_code_list.append(0)
                    
            #英数字の奇数の部分（0~z）
            else:
                #該当する数字と二つ目の乱数と文字の順番を足した数がcipher_twoに代入される
                #そして、iの場所が11の倍数なら1、７の倍数なら2、５の倍数なら3が足される
                if i%11==0:
                    cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+1
                elif i%7==0:
                    cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+2
                elif i%5==0:
                    cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)+3
                else:
                    cipher_two=int(dic3[change_plaintext_list[i]])+int(dic3[random_number2])+int(i)
                #cipher_twoが36を超えたら36を超えなくなるまでcipher_twoを36で引き続ける
                #cipher_twoから36を弾き続けた回数がpass_oneに代入される。
                #そのpass_oneが9未満ならそのままで、10を超えたらa~zの文字に置き換わり、pass_code_listに格納される。
                #cipher_twoは0~zに文字が置き換わり、ciphertext_listに格納される。
                if cipher_two>=36:
                    while cipher_two>=36:
                        cipher_two-=36
                        pass_one+=1
                    if pass_one >=10:
                        pass_one=dic1.get(pass_one)
                    cipher_two=str(dic1.get(cipher_two))
                    ciphertext_list.append(cipher_two)
                    pass_code_list.append(pass_one)
                    pass_one=0
                #cipher_twoが35以下ならcipher_twoが0~zに変更され、ciphertext_listに格納される。
                #そして、pass_code_listには0が格納される。
                else:
                    cipher_two=str(dic1.get(cipher_two))
                    ciphertext_list.append(cipher_two)
                    pass_code_list.append(0)
                    
        return ciphertext_list,pass_code_list
               
    
    #復号化の計算               
    def decode(self,ciphertext_nodummy,random_number1,random_number2,pass_code):
        #decode_listの初期化
        decode_list=[]
        #暗号を英数字に変換した文字数分実行を行う
        for i in range(len(ciphertext_nodummy)):
            #英数字の偶数の部分
            if i % 2 == 0:
                #decode_oneに該当する英数字を数字に直し、パスの数字文36をかけて代入する。
                #そして、求めたdecode_oneに文字の順番と一つ目の乱数分値を引く。
                #その時に、順番が11の倍数なら3、7の倍数なら2、5の倍数なら1をさらに引く。
                #そして、計算した文字を英数字に変換して、decode_listに格納する。
                decode_one=int(dic3.get(ciphertext_nodummy[i]))+int(dic3.get(pass_code[i]))*36
                if i%11==0:
                    decode_one=decode_one-i-int(random_number1)-3
                elif i%7==0:
                    decode_one=decode_one-i-int(random_number1)-2
                elif i%5==0:
                    decode_one=decode_one-i-int(random_number1)-1
                else:
                    decode_one=decode_one-i-int(random_number1)
                decode_one=str(dic2.get(decode_one))
                decode_list.append(str(decode_one))
            #奇数の部分
            else:
                #decode_twoに該当する英数字を数字に直し、パスの数字文36をかけて代入する。
                #そして、求めたdecode_twoに文字の順番と一つ目の乱数分値を引く時に、順番が11の倍数
                #なら１、7の倍数なら2、5の倍数なら3を引く。
                #そして、計算した文字を英数字に変換して、decode_listに格納する。
                decode_two=int(dic3.get(ciphertext_nodummy[i]))+int(dic3.get(pass_code[i]))*36
                if i%11==0:
                    decode_two=decode_two-i-int(dic3.get(random_number2))-1
                elif i%7==0:
                    decode_two=decode_two-i-int(dic3.get(random_number2))-2
                elif i%5==0:
                    decode_two=decode_two-i-int(dic3.get(random_number2))-3
                else:
                    decode_two=decode_two-i-int(dic3.get(random_number2))
                decode_two=str(dic2.get(decode_two))
                decode_list.append(decode_two)
        return decode_list
                
    
    #平文を英数字で表示する 
    def change1(self,change_text):
        change_text = change_text.replace("0","00")
        change_text = change_text.replace("1","01")
        change_text = change_text.replace("2","02")
        change_text = change_text.replace("3","03")
        change_text = change_text.replace("4","04")
        change_text = change_text.replace("5","05")
        change_text = change_text.replace("6","06")
        change_text = change_text.replace("7","07")
        change_text = change_text.replace("8","08")
        change_text = change_text.replace("9","09")
        change_text = change_text.replace("a","0a")
        change_text = change_text.replace("b","0b")
        change_text = change_text.replace("c","0c")
        change_text = change_text.replace("d","0d")
        change_text = change_text.replace("e","0e")
        change_text = change_text.replace("f","0f")
        change_text = change_text.replace("g","0g")
        change_text = change_text.replace("h","0h")
        change_text = change_text.replace("i","0i")
        change_text = change_text.replace("j","0j")
        change_text = change_text.replace("k","0k")
        change_text = change_text.replace("l","0l")
        change_text = change_text.replace("m","0m")
        change_text = change_text.replace("n","0n")
        change_text = change_text.replace("o","0o")
        change_text = change_text.replace("p","0p")
        change_text = change_text.replace("q","0q")
        change_text = change_text.replace("r","0r")
        change_text = change_text.replace("s","0s")
        change_text = change_text.replace("t","0t")
        change_text = change_text.replace("u","0u")
        change_text = change_text.replace("v","0v")
        change_text = change_text.replace("w","0w")
        change_text = change_text.replace("x","0x")
        change_text = change_text.replace("y","0y")
        change_text = change_text.replace("z","0z")
        change_text = change_text.replace("A","10")
        change_text = change_text.replace("B","11")
        change_text = change_text.replace("C","12")
        change_text = change_text.replace("D","13")
        change_text = change_text.replace("E","14")
        change_text = change_text.replace("F","15")
        change_text = change_text.replace("G","16")
        change_text = change_text.replace("H","17")
        change_text = change_text.replace("I","18")
        change_text = change_text.replace("J","19")
        change_text = change_text.replace("K","1a")
        change_text = change_text.replace("L","1b")
        change_text = change_text.replace("M","1c")
        change_text = change_text.replace("N","1d")
        change_text = change_text.replace("O","1e")
        change_text = change_text.replace("P","1f")
        change_text = change_text.replace("Q","1g")
        change_text = change_text.replace("R","1h")
        change_text = change_text.replace("S","1i")
        change_text = change_text.replace("T","1j")
        change_text = change_text.replace("U","1k")
        change_text = change_text.replace("V","1l")
        change_text = change_text.replace("W","1m")
        change_text = change_text.replace("X","1n")
        change_text = change_text.replace("Y","1o")
        change_text = change_text.replace("Z","1p")
        change_text = change_text.replace("あ","1q")
        change_text = change_text.replace("い","1r")
        change_text = change_text.replace("う","1s")
        change_text = change_text.replace("え","1t")
        change_text = change_text.replace("お","1u")
        change_text = change_text.replace("か","1v")
        change_text = change_text.replace("き","1w")
        change_text = change_text.replace("く","1x")
        change_text = change_text.replace("け","1y")
        change_text = change_text.replace("こ","1z")
        change_text = change_text.replace("さ","20")
        change_text = change_text.replace("し","21")
        change_text = change_text.replace("す","22")
        change_text = change_text.replace("せ","23")
        change_text = change_text.replace("そ","24")
        change_text = change_text.replace("た","25")
        change_text = change_text.replace("ち","26")
        change_text = change_text.replace("つ","27")
        change_text = change_text.replace("て","28")
        change_text = change_text.replace("と","29")
        change_text = change_text.replace("な","2a")
        change_text = change_text.replace("に","2b")
        change_text = change_text.replace("ぬ","2c")
        change_text = change_text.replace("ね","2d")
        change_text = change_text.replace("の","2e")
        change_text = change_text.replace("は","2f")
        change_text = change_text.replace("ひ","2g")
        change_text = change_text.replace("ふ","2h")
        change_text = change_text.replace("へ","2i")
        change_text = change_text.replace("ほ","2j")
        change_text = change_text.replace("ま","2k")
        change_text = change_text.replace("み","2l")
        change_text = change_text.replace("む","2m")
        change_text = change_text.replace("め","2n")
        change_text = change_text.replace("も","2o")
        change_text = change_text.replace("や","2p")
        change_text = change_text.replace("ゐ","2q")
        change_text = change_text.replace("ゆ","2r")
        change_text = change_text.replace("ゑ","2s")
        change_text = change_text.replace("よ","2t")
        change_text = change_text.replace("ら","2u")
        change_text = change_text.replace("り","2v")
        change_text = change_text.replace("る","2w")
        change_text = change_text.replace("れ","2x")
        change_text = change_text.replace("ろ","2y")
        change_text = change_text.replace("わ","2z")
        change_text = change_text.replace("を","30")
        change_text = change_text.replace("ん","31")
        change_text = change_text.replace("ぁ","32")
        change_text = change_text.replace("ぃ","33")
        change_text = change_text.replace("ぅ","34")
        change_text = change_text.replace("ぇ","35")
        change_text = change_text.replace("ぉ","36")
        change_text = change_text.replace("ゃ","37")
        change_text = change_text.replace("ゅ","38")
        change_text = change_text.replace("ょ","39")
        change_text = change_text.replace("っ","3a")
        change_text = change_text.replace("が","3b")
        change_text = change_text.replace("ぎ","3c")
        change_text = change_text.replace("ぐ","3d")
        change_text = change_text.replace("げ","3e")
        change_text = change_text.replace("ご","3f")
        change_text = change_text.replace("ざ","3g")
        change_text = change_text.replace("じ","3h")
        change_text = change_text.replace("ず","3i")
        change_text = change_text.replace("ぜ","3j")
        change_text = change_text.replace("ぞ","3k")
        change_text = change_text.replace("だ","3l")
        change_text = change_text.replace("ぢ","3m")
        change_text = change_text.replace("づ","3n")
        change_text = change_text.replace("で","3o")
        change_text = change_text.replace("ど","3p")
        change_text = change_text.replace("ば","3q")
        change_text = change_text.replace("び","3r")
        change_text = change_text.replace("ぶ","3s")
        change_text = change_text.replace("べ","3t")
        change_text = change_text.replace("ぼ","3u")
        change_text = change_text.replace("ぱ","3v")
        change_text = change_text.replace("ぴ","3w")
        change_text = change_text.replace("ぷ","3x")
        change_text = change_text.replace("ぺ","3y")
        change_text = change_text.replace("ぽ","3z")
        change_text = change_text.replace("ア","40")
        change_text = change_text.replace("イ","41")
        change_text = change_text.replace("ウ","42")
        change_text = change_text.replace("エ","43")
        change_text = change_text.replace("オ","44")
        change_text = change_text.replace("カ","45")
        change_text = change_text.replace("キ","46")
        change_text = change_text.replace("ク","47")
        change_text = change_text.replace("ケ","48")
        change_text = change_text.replace("コ","49")
        change_text = change_text.replace("サ","4a")
        change_text = change_text.replace("シ","4b")
        change_text = change_text.replace("ス","4c")
        change_text = change_text.replace("セ","4d")
        change_text = change_text.replace("ソ","4e")
        change_text = change_text.replace("タ","4f")
        change_text = change_text.replace("チ","4g")
        change_text = change_text.replace("ツ","4h")
        change_text = change_text.replace("テ","4i")
        change_text = change_text.replace("ト","4j")
        change_text = change_text.replace("ナ","4k")
        change_text = change_text.replace("ニ","4l")
        change_text = change_text.replace("ヌ","4m")
        change_text = change_text.replace("ネ","4n")
        change_text = change_text.replace("ノ","4o")
        change_text = change_text.replace("ハ","4p")
        change_text = change_text.replace("ヒ","4q")
        change_text = change_text.replace("フ","4r")
        change_text = change_text.replace("ヘ","4s")
        change_text = change_text.replace("ホ","4t")
        change_text = change_text.replace("マ","4u")
        change_text = change_text.replace("ミ","4v")
        change_text = change_text.replace("ム","4w")
        change_text = change_text.replace("メ","4x")
        change_text = change_text.replace("モ","4y")
        change_text = change_text.replace("ヤ","4z")
        change_text = change_text.replace("ユ","50")
        change_text = change_text.replace("ヨ","51")
        change_text = change_text.replace("ラ","52")
        change_text = change_text.replace("リ","53")
        change_text = change_text.replace("ル","54")
        change_text = change_text.replace("レ","55")
        change_text = change_text.replace("ロ","56")
        change_text = change_text.replace("ワ","57")
        change_text = change_text.replace("ヲ","58")
        change_text = change_text.replace("ン","59")
        change_text = change_text.replace("ァ","5a")
        change_text = change_text.replace("ィ","5b")
        change_text = change_text.replace("ゥ","5c")
        change_text = change_text.replace("ェ","5d")
        change_text = change_text.replace("ォ","5e")
        change_text = change_text.replace("ャ","5f")
        change_text = change_text.replace("ュ","5g")
        change_text = change_text.replace("ョ","5h")
        change_text = change_text.replace("ッ","5i")
        change_text = change_text.replace("ガ","5j")
        change_text = change_text.replace("ギ","5k")
        change_text = change_text.replace("グ","5l")
        change_text = change_text.replace("ゲ","5m")
        change_text = change_text.replace("ゴ","5n")
        change_text = change_text.replace("ザ","5o")
        change_text = change_text.replace("ジ","5p")
        change_text = change_text.replace("ズ","5q")
        change_text = change_text.replace("ゼ","5r")
        change_text = change_text.replace("ゾ","5s")
        change_text = change_text.replace("ダ","5t")
        change_text = change_text.replace("ヂ","5u")
        change_text = change_text.replace("ヅ","5v")
        change_text = change_text.replace("デ","5w")
        change_text = change_text.replace("ド","5x")
        change_text = change_text.replace("バ","5y")
        change_text = change_text.replace("ビ","5z")
        change_text = change_text.replace("ブ","60")
        change_text = change_text.replace("ベ","61")
        change_text = change_text.replace("ボ","62")
        change_text = change_text.replace("パ","63")
        change_text = change_text.replace("ピ","64")
        change_text = change_text.replace("プ","65")
        change_text = change_text.replace("ペ","66")
        change_text = change_text.replace("ポ","67")
        change_text = change_text.replace("ー","68")
        change_text = change_text.replace("!","69")
        change_text = change_text.replace('"',"6a")
        change_text = change_text.replace("'","6b")
        change_text = change_text.replace("#","6c")
        change_text = change_text.replace("$","6d")
        change_text = change_text.replace("%","6e")
        change_text = change_text.replace("&","6f")
        change_text = change_text.replace("(","6g")
        change_text = change_text.replace(")","6h")
        change_text = change_text.replace("=","6i")
        change_text = change_text.replace("-","6j")
        change_text = change_text.replace("~","6k")
        change_text = change_text.replace("^","6l")
        change_text = change_text.replace("@","6m")
        change_text = change_text.replace("|","6n")
        change_text = change_text.replace("￥","6o")
        change_text = change_text.replace("`","6p")
        change_text = change_text.replace("{","6q")
        change_text = change_text.replace("[","6r")
        change_text = change_text.replace("「","6s")
        change_text = change_text.replace("+","6t")
        change_text = change_text.replace("*","6u")
        change_text = change_text.replace(";","6v")
        change_text = change_text.replace(":","6w")
        change_text = change_text.replace("}","6x")
        change_text = change_text.replace("]","6y")
        change_text = change_text.replace("」","6z")
        change_text = change_text.replace("<","70")
        change_text = change_text.replace(",","71")
        change_text = change_text.replace("、","72")
        change_text = change_text.replace(">","73")
        change_text = change_text.replace(".","74")
        change_text = change_text.replace("。","75")
        change_text = change_text.replace("?","76")
        change_text = change_text.replace("/","77")
        change_text = change_text.replace("・","78")
        change_text = change_text.replace("_","79")
        change_text = change_text.replace(" ","7a")
        change_text = change_text.replace("ゔ","7b")
        change_text = change_text.replace("ヴ","7c")
        return change_text
    
    
    #暗号文をを英数字で表示する
    def change2(self,change_text):
        change_text = change_text.replace("10","A")
        change_text = change_text.replace("11","B")
        change_text = change_text.replace("12","C")
        change_text = change_text.replace("13","D")
        change_text = change_text.replace("14","E")
        change_text = change_text.replace("15","F")
        change_text = change_text.replace("16","G")
        change_text = change_text.replace("17","H")
        change_text = change_text.replace("18","I")
        change_text = change_text.replace("19","J")
        change_text = change_text.replace("1a","K")
        change_text = change_text.replace("1b","L")
        change_text = change_text.replace("1c","M")
        change_text = change_text.replace("1d","N")
        change_text = change_text.replace("1e","O")
        change_text = change_text.replace("1f","P")
        change_text = change_text.replace("1g","Q")
        change_text = change_text.replace("1h","R")
        change_text = change_text.replace("1i","S")
        change_text = change_text.replace("1j","T")
        change_text = change_text.replace("1k","U")
        change_text = change_text.replace("1l","V")
        change_text = change_text.replace("1m","W")
        change_text = change_text.replace("1n","X")
        change_text = change_text.replace("1o","Y")
        change_text = change_text.replace("1p","Z")
        change_text = change_text.replace("1q","あ")
        change_text = change_text.replace("1r","い")
        change_text = change_text.replace("1s","う")
        change_text = change_text.replace("1t","え")
        change_text = change_text.replace("1u","お")
        change_text = change_text.replace("1v","か")
        change_text = change_text.replace("1w","き")
        change_text = change_text.replace("1x","く")
        change_text = change_text.replace("1y","け")
        change_text = change_text.replace("1z","こ")
        change_text = change_text.replace("20","さ")
        change_text = change_text.replace("21","し")
        change_text = change_text.replace("22","す")
        change_text = change_text.replace("23","せ")
        change_text = change_text.replace("24","そ")
        change_text = change_text.replace("25","た")
        change_text = change_text.replace("26","ち")
        change_text = change_text.replace("27","つ")
        change_text = change_text.replace("28","て")
        change_text = change_text.replace("29","と")
        change_text = change_text.replace("2a","な")
        change_text = change_text.replace("2b","に")
        change_text = change_text.replace("2c","ぬ")
        change_text = change_text.replace("2d","ね")
        change_text = change_text.replace("2e","の")
        change_text = change_text.replace("2f","は")
        change_text = change_text.replace("2g","ひ")
        change_text = change_text.replace("2h","ふ")
        change_text = change_text.replace("2i","へ")
        change_text = change_text.replace("2j","ほ")
        change_text = change_text.replace("2k","ま")
        change_text = change_text.replace("2l","み")
        change_text = change_text.replace("2m","む")
        change_text = change_text.replace("2n","め")
        change_text = change_text.replace("2o","も")
        change_text = change_text.replace("2p","や")
        change_text = change_text.replace("2q","ゐ")
        change_text = change_text.replace("2r","ゆ")
        change_text = change_text.replace("2s","ゑ")
        change_text = change_text.replace("2t","よ")
        change_text = change_text.replace("2u","ら")
        change_text = change_text.replace("2v","り")
        change_text = change_text.replace("2w","る")
        change_text = change_text.replace("2x","れ")
        change_text = change_text.replace("2y","ろ")
        change_text = change_text.replace("2z","わ")
        change_text = change_text.replace("30","を")
        change_text = change_text.replace("31","ん")
        change_text = change_text.replace("32","ぁ")
        change_text = change_text.replace("33","ぃ")
        change_text = change_text.replace("34","ぅ")
        change_text = change_text.replace("35","ぇ")
        change_text = change_text.replace("36","ぉ")
        change_text = change_text.replace("37","ゃ")
        change_text = change_text.replace("38","ゅ")
        change_text = change_text.replace("39","ょ")
        change_text = change_text.replace("3a","っ")
        change_text = change_text.replace("3b","が")
        change_text = change_text.replace("3c","ぎ")
        change_text = change_text.replace("3d","ぐ")
        change_text = change_text.replace("3e","げ")
        change_text = change_text.replace("3f","ご")
        change_text = change_text.replace("3g","ざ")
        change_text = change_text.replace("3h","じ")
        change_text = change_text.replace("3i","ず")
        change_text = change_text.replace("3j","ぜ")
        change_text = change_text.replace("3k","ぞ")
        change_text = change_text.replace("3l","だ")
        change_text = change_text.replace("3m","ぢ")
        change_text = change_text.replace("3n","づ")
        change_text = change_text.replace("3o","で")
        change_text = change_text.replace("3p","ど")
        change_text = change_text.replace("3q","ば")
        change_text = change_text.replace("3r","び")
        change_text = change_text.replace("3s","ぶ")
        change_text = change_text.replace("3t","べ")
        change_text = change_text.replace("3u","ぼ")
        change_text = change_text.replace("3v","ぱ")
        change_text = change_text.replace("3w","ぴ")
        change_text = change_text.replace("3x","ぷ")
        change_text = change_text.replace("3y","ぺ")
        change_text = change_text.replace("3z","ぽ")
        change_text = change_text.replace("40","ア")
        change_text = change_text.replace("41","イ")
        change_text = change_text.replace("42","ウ")
        change_text = change_text.replace("43","エ")
        change_text = change_text.replace("44","オ")
        change_text = change_text.replace("45","カ")
        change_text = change_text.replace("46","キ")
        change_text = change_text.replace("47","ク")
        change_text = change_text.replace("48","ケ")
        change_text = change_text.replace("49","コ")
        change_text = change_text.replace("4a","サ")
        change_text = change_text.replace("4b","シ")
        change_text = change_text.replace("4c","ス")
        change_text = change_text.replace("4d","セ")
        change_text = change_text.replace("4e","ソ")
        change_text = change_text.replace("4f","タ")
        change_text = change_text.replace("4g","チ")
        change_text = change_text.replace("4h","ツ")
        change_text = change_text.replace("4i","テ")
        change_text = change_text.replace("4j","ト")
        change_text = change_text.replace("4k","ナ")
        change_text = change_text.replace("4l","ニ")
        change_text = change_text.replace("4m","ヌ")
        change_text = change_text.replace("4n","ネ")
        change_text = change_text.replace("4o","ノ")
        change_text = change_text.replace("4p","ハ")
        change_text = change_text.replace("4q","ヒ")
        change_text = change_text.replace("4r","フ")
        change_text = change_text.replace("4s","ヘ")
        change_text = change_text.replace("4t","ホ")
        change_text = change_text.replace("4u","マ")
        change_text = change_text.replace("4v","ミ")
        change_text = change_text.replace("4w","ム")
        change_text = change_text.replace("4x","メ")
        change_text = change_text.replace("4y","モ")
        change_text = change_text.replace("4z","ヤ")
        change_text = change_text.replace("50","ユ")
        change_text = change_text.replace("51","ヨ")
        change_text = change_text.replace("52","ラ")
        change_text = change_text.replace("53","リ")
        change_text = change_text.replace("54","ル")
        change_text = change_text.replace("55","レ")
        change_text = change_text.replace("56","ロ")
        change_text = change_text.replace("57","ワ")
        change_text = change_text.replace("58","ヲ")
        change_text = change_text.replace("59","ン")
        change_text = change_text.replace("5a","ァ")
        change_text = change_text.replace("5b","ィ")
        change_text = change_text.replace("5c","ゥ")
        change_text = change_text.replace("5d","ェ")
        change_text = change_text.replace("5e","ォ")
        change_text = change_text.replace("5f","ャ")
        change_text = change_text.replace("5g","ュ")
        change_text = change_text.replace("5h","ョ")
        change_text = change_text.replace("5i","ッ")
        change_text = change_text.replace("5j","ガ")
        change_text = change_text.replace("5k","ギ")
        change_text = change_text.replace("5l","グ")
        change_text = change_text.replace("5m","ゲ")
        change_text = change_text.replace("5n","ゴ")
        change_text = change_text.replace("5o","ザ")
        change_text = change_text.replace("5p","ジ")
        change_text = change_text.replace("5q","ズ")
        change_text = change_text.replace("5r","ゼ")
        change_text = change_text.replace("5s","ゾ")
        change_text = change_text.replace("5t","ダ")
        change_text = change_text.replace("5u","ヂ")
        change_text = change_text.replace("5v","ヅ")
        change_text = change_text.replace("5w","デ")
        change_text = change_text.replace("5x","ド")
        change_text = change_text.replace("5y","バ")
        change_text = change_text.replace("5z","ビ")
        change_text = change_text.replace("60","ブ")
        change_text = change_text.replace("61","ベ")
        change_text = change_text.replace("62","ボ")
        change_text = change_text.replace("63","パ")
        change_text = change_text.replace("64","ピ")
        change_text = change_text.replace("65","プ")
        change_text = change_text.replace("66","ペ")
        change_text = change_text.replace("67","ポ")
        change_text = change_text.replace("68","ー")
        change_text = change_text.replace("69","!")
        change_text = change_text.replace("6a",'"')
        change_text = change_text.replace("6b","'")
        change_text = change_text.replace("6c","#")
        change_text = change_text.replace("6d","$")
        change_text = change_text.replace("6e","%")
        change_text = change_text.replace("6f","&")
        change_text = change_text.replace("6g","(")
        change_text = change_text.replace("6h",")")
        change_text = change_text.replace("6i","=")
        change_text = change_text.replace("6j","-")
        change_text = change_text.replace("6k","~")
        change_text = change_text.replace("6l","^")
        change_text = change_text.replace("6m","@")
        change_text = change_text.replace("6n","|")
        change_text = change_text.replace("6o","￥")
        change_text = change_text.replace("6p","`")
        change_text = change_text.replace("6q","{")
        change_text = change_text.replace("6r","[")
        change_text = change_text.replace("6s","「")
        change_text = change_text.replace("6t","+")
        change_text = change_text.replace("6u","*")
        change_text = change_text.replace("6v",";")
        change_text = change_text.replace("6w",":")
        change_text = change_text.replace("6x","}")
        change_text = change_text.replace("6y","]")
        change_text = change_text.replace("6z","」")
        change_text = change_text.replace("70","<")
        change_text = change_text.replace("71",",")
        change_text = change_text.replace("72","、")
        change_text = change_text.replace("73",">")
        change_text = change_text.replace("74",".")
        change_text = change_text.replace("75","。")
        change_text = change_text.replace("76","?")
        change_text = change_text.replace("77","/")
        change_text = change_text.replace("78","・")
        change_text = change_text.replace("79","_")
        change_text = change_text.replace("7a"," ")
        change_text = change_text.replace("7b","ゔ")
        change_text = change_text.replace("7c","ヴ")
        change_text = change_text.replace("0z","z")
        change_text = change_text.replace("0y","y")
        change_text = change_text.replace("0x","x")
        change_text = change_text.replace("0w","w")
        change_text = change_text.replace("0v","v")
        change_text = change_text.replace("0u","u")
        change_text = change_text.replace("0t","t")
        change_text = change_text.replace("0s","s")
        change_text = change_text.replace("0r","r")
        change_text = change_text.replace("0q","q")
        change_text = change_text.replace("0p","p")
        change_text = change_text.replace("0o","o")
        change_text = change_text.replace("0n","n")
        change_text = change_text.replace("0m","m")
        change_text = change_text.replace("0l","l")
        change_text = change_text.replace("0k","k")
        change_text = change_text.replace("0j","j")
        change_text = change_text.replace("0i","i")
        change_text = change_text.replace("0h","h")
        change_text = change_text.replace("0g","g")
        change_text = change_text.replace("0f","f")
        change_text = change_text.replace("0e","e")
        change_text = change_text.replace("0d","d")
        change_text = change_text.replace("0c","c")
        change_text = change_text.replace("0b","b")
        change_text = change_text.replace("0a","a")
        change_text = change_text.replace("09","9")
        change_text = change_text.replace("08","8")
        change_text = change_text.replace("07","7")
        change_text = change_text.replace("06","6")
        change_text = change_text.replace("05","5")
        change_text = change_text.replace("04","4")
        change_text = change_text.replace("03","3")
        change_text = change_text.replace("02","2")
        change_text = change_text.replace("01","1")
        change_text = change_text.replace("00","0")
        return change_text
    

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()