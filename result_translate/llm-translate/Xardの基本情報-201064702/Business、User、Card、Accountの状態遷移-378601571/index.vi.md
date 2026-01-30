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

Chỉ khi quản lý số dư bằng Xard.

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1702374510748.drawio.png?api=v2)

Để lấy trạng thái của Business、User、Card、Account, hãy sử dụng các API dưới đây.

*   Business：[API 「Businessの取得」](https://api-doc.connect.xard.jp/#operation/getBusiness)
    
*   User：[API 「Userの取得」](https://api-doc.connect.xard.jp/#operation/getUser) hoặc [API 「Userリストの取得」](https://api-doc.connect.xard.jp/#operation/getUserList)
    
*   Card：[API 「カードの取得」](https://api-doc.connect.xard.jp/#operation/getCard) hoặc [API 「カードリストの取得」](https://api-doc.connect.xard.jp/#operation/getCardList)
    
*   Account：[API 「Accountの取得」](https://api-doc.connect.xard.jp/#operation/getAccount)