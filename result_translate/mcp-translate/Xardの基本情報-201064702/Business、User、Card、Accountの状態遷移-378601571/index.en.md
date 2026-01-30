The states of Business, User, Card, and Account, which are components of Xard, transition as follows:

## 1. Business State Transition

![](/wiki/download/attachments/378601571/BusinessKYC-03-2.drawio.png?api=v2)

## 2. User State Transition

![](/wiki/download/attachments/378601571/BusinessKYC-04-2.drawio.png?api=v2)

## 3. Card State Transition

3.1 In the case of a physical card

![](/wiki/download/attachments/378601571/BusinessKYC-05-2.drawio.png?api=v2)

3.2 In the case of a virtual card

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1700818216445.drawio.png?api=v2)

## 4. Account State Transition

Only in the case of balance management by Xard.

![](/wiki/download/attachments/378601571/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB-1702374510748.drawio.png?api=v2)

To retrieve the states of Business, User, Card, and Account, please use the following APIs:

* Business: ["Retrieve Business" API](https://api-doc.connect.xard.jp/#operation/getBusiness)

* User: ["Retrieve User" API](https://api-doc.connect.xard.jp/#operation/getUser) or ["Retrieve User List" API](https://api-doc.connect.xard.jp/#operation/getUserList)

* Card: ["Retrieve Card" API](https://api-doc.connect.xard.jp/#operation/getCard) or ["Retrieve Card List" API](https://api-doc.connect.xard.jp/#operation/getCardList)

* Account: ["Retrieve Account" API](https://api-doc.connect.xard.jp/#operation/getAccount)