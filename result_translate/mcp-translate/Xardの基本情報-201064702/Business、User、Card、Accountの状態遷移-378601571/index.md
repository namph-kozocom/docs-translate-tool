Xardの構成要素であるBusiness、User、Card、Accountは、以下のように状態遷移します。

## 1\. Businessの状態遷移

![](/wiki/download/attachments/378601571/BusinessKYC-03-2.drawio.png?api=v2)

## 2\. Userの状態遷移

![](/wiki/download/attachments/378601571/BusinessKYC-04-2.drawio.png?api=v2)

## 3\. Cardの状態遷移

3.1 フィジカルカードの場合

![](/wiki/download/attachments/378601571/BusinessKYC-05-2.drawio.png?api=v2)

3.2 バーチャルカードの場合

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1700818216445.drawio.png?api=v2)

## 4\. Accountの状態遷移

Xardによる残高管理の場合のみ。

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1702374510748.drawio.png?api=v2)

Business、User、Card、Accountの状態を取得するには以下APIをご利用ください。

*   Business：[「Businessの取得」API](https://api-doc.connect.xard.jp/#operation/getBusiness)
    
*   User：[「Userの取得」](https://api-doc.connect.xard.jp/#operation/getUser)APIもしくは[「Userリストの取得」API](https://api-doc.connect.xard.jp/#operation/getUserList)
    
*   Card：[「カードの取得」API](https://api-doc.connect.xard.jp/#operation/getCard)もしくは[「カードリストの取得」API](https://api-doc.connect.xard.jp/#operation/getCardList)
    
*   Account：[「Accountの取得」API](https://api-doc.connect.xard.jp/#operation/getAccount)