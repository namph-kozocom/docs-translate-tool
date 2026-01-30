Xard allows you to select the specifications of the card to be issued.Register the specifications of the selected card to Card Program or Card Product.

1. [Card type](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#1.-%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97)

2.[Activation type](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#2.-%E3%82%A2%E3%82%AF%E3%83%86%E3%82%A3%E3%83%99%E3%83%BC%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97)

3.[Ticket face/mount/envelope design](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#3.-%E5%88%B8%E9%9D%A2%E3%83%BB%E5%8F%B0%E7%B4%99%E3%83%BB%E5%B0%81%E7%AD%92%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3)

4.[Card number range](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E3%82%AB%E3%83%BC%E3%83%89%E7%95%AA%E5%8F%B7%EF%BC%88PAN%EF%BC%89%E3%81%AE%E7%AF%84%E5%9B%B2)

5.[Overseas markup fee rate/collection conditions](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#5.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6)


* Multiple Card Products can be registered depending on the product content of the card.

*[Overseas markup fee rate/collection conditions](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6) only, CardRegister Program and other items to Card Product.


* * *

## 1\. Card type

For each Card Product, select the card type from "**Physical**" or "**Virtual**".

**Physical**

* Send a Physical card to the user.

*You can select one of the following physical card types.

* IC card (contact/contactless IC dual card)

*Magnetic card

* When creating a card, you can select the PIN (Personal Identification Number) setting from automatic numbering or manual numbering.


* * *

**If the PIN is manually assigned**

* Before setting a PIN, the partner should check with the following information about the target user to ensure that the PIN is not easy to guess based on personal information.

* Date of birth, phone number (home and mobile)

* Other personal information

* Combination of the above

* Please set the PIN items using [“Create Card” API](https://api-doc.connect.xard.jp/#operation/createCard).

* To check the registered PIN, the user should execute ["Get PIN" API](https://api-doc.connect.xard.jp/#operation/getPin).

* PIN is subject to PCIDSS.We ask that partners consider the PCIDSS compliance policy.


**Virtual**

* A virtual card is created (physical card is not created).

* To check the card information of the virtual card, the user should execute ["Retrieve confidential card information" API](https://api-doc.connect.xard.jp/#operation/sensitiveData).


* * *

## 2\. Activation type

For each Card Product, select the activation type from "**Activation Required**" or "**Activation Not Required**".

**Activation required**

* Can only be selected when the card type is "Physical".

* The activation code and QR code will be printed on the backing paper when the card is sent.

* Users can use their cards by activating them in one of the following ways:

*Enter the activation code on the screen provided by the partner.

* Scan the QR code and authenticate on the screen provided by the partner that appears.


**Activation/Not required**

Users can use the card without activation.

* * *

# 3\. Card face/mount/envelope design

Create each of the following for each Card Product:

**Physical card design**

This is the face design of the Physical card.Created according to international brand business card regulations.
You will need to coordinate your design with your printing company and get international brand approval for your final design.

**Physical card mount design**
This is the design of the mount when sending Physical cards.Coordinate the design with the printing company.

**Physical Card Envelope Design**

This is the design of the envelope when sending physical cards.Coordinate the design with the printing company.

**Card design for card widget**

This is the design of the screen that is displayed when a user queries card information using the card widget function.Created according to international brand VirtualAccounts regulations.
Final design must be approved by international brands.

It is also possible to create a leaflet to be included when sending a physical card.

* Physical cards can be mailed by regular mail or simple registered mail, which can be specified using the Card Creation API.

* In the future, we plan to support specified registered mail.


* * *

# 4\. Card number (PAN) range

* Set the range of card numbers to be assigned when issuing cards for each CardProduct.

* Partners can freely set the card number between 9 and 15 digits.

* Digits 1 to 8 of the card number are the partner's BIN.

*The 16th digit of the card number is the check digit.

* It is also possible to use the same BIN for multiple CardProducts by dividing the specified range of card numbers.


![image-20240304-023832.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-023832.png?api=v2)

Card numbers are randomly obtained from the range of registered card numbers and issued, so once the range has been set, it is not possible to divide it later.

For testing on the Xard side, we will use the first 100 card numbers for each CardProduct.

Example) How to set 9 to 15 digits

When issuing a physical card and virtual card with the same BIN

**Physical Card**

![image-20240304-025424.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025424.png?api=v2)

**Virtual Card**

![image-20240304-025617.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025617.png?api=v2)

*The first 100 sheets will be used in Xard, so please specify from 100.

* * *

# 5\. Overseas markup fee rate/collection conditions

Set the following for each Card Program.

**Overseas markup fee rate**

Set the percentage of overseas markup fees (fees incurred when using your card overseas).
The standard commission rate is 3%, but other percentages can be set.
The commission rate can be set to two decimal places.

**Overseas markup fee collection conditions**

Set the conditions for collecting overseas markup fees.You can choose from the following two patterns.

Pattern 1:
Xard standard settings

An overseas markup fee will be collected if the currency code is other than Japanese yen.

Pattern 2:
Option settings (international brand standards)

Overseas markup fees will be collected if the following conditions are met.

[For Visa]

Authorization: If one or more of the following conditions ① to ③ are met and the transaction is determined to be an overseas transaction.
① Acquirer country code is other than “domestic”
②International brand member store country code is other than "JP"
③Currency is other than "Japanese yen"
Clearing: If the Settlement Flag linked from Visa is other than "8 (domestic)"

[For JCB]

Authorization, clearing: If the sending center ID linked from JCB is "1a996610000" (*ID for overseas transactions)

Xard's handling of overseas markup fees at the time of return is as follows.

When returning goods after sales have been confirmed: Overseas markup fees will not be refunded.

If canceled before sales are confirmed: Refunds will be made including overseas markup fees.