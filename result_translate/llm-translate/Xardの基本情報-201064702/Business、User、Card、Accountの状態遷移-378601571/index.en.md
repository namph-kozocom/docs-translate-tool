Xard components, Business, User, Card, and Account, transition states as shown below.

## 1\. Business State Transitions

![](/wiki/download/attachments/378601571/BusinessKYC-03-2.drawio.png?api=v2)

## 2\. User State Transitions

![](/wiki/download/attachments/378601571/BusinessKYC-04-2.drawio.png?api=v2)

## 3\. Card State Transitions

3.1 In the case of a physical card

![](/wiki/download/attachments/378601571/BusinessKYC-05-2.drawio.png?api=v2)

3.2 In the case of a virtual card

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1700818216445.drawio.png?api=v2)

## 4\. Account State Transitions

Only in cases of balance management by Xard.

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1702374510748.drawio.png?api=v2)

Please use the following APIs to retrieve the states of Business, User, Card, and Account.

*   Business: [“Get Business” API](https://api-doc.connect.xard.jp/#operation/getBusiness)
    
*   User: [“Get User”](https://api-doc.connect.xard.jp/#operation/getUser) API or [“Get User List” API](https://api-doc.connect.xard.jp/#operation/getUserList)
    
*   Card: [“Get Card” API](https://api-doc.connect.xard.jp/#operation/getCard) or [“Get Card List” API](https://api-doc.connect.xard.jp/#operation/getCardList)
    
*   Account: [“Get Account” API](https://api-doc.connect.xard.jp/#operation/getAccount)