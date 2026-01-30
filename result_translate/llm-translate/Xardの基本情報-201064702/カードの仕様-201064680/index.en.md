In Xard, you can choose the specifications of the card to be issued. The selected card specifications are registered in either the Card Program or Card Product.

1.  [Card Type](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#1.-%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97)
    
2.  [Activate Type](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#2.-%E3%82%A2%E3%82%AF%E3%83%86%E3%82%A3%E3%83%99%E3%83%BC%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97)
    
3.  [Design of Face, Cover Sheet, and Envelope](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#3.-%E5%88%B8%E9%9D%A2%E3%83%BB%E5%8F%B0%E7%B4%99%E3%83%BB%E5%B0%81%E7%AD%92%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3)
    
4.  [Range of Card Number](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E3%82%AB%E3%83%BC%E3%83%89%E7%95%AA%E5%8F%B7%EF%BC%88PAN%EF%BC%89%E3%81%AE%E7%AF%84%E5%9B%B2)
    
5.  [Overseas Markup Fee Rate and Collection Conditions](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#5.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6)
    
*   Card Products can be registered multiple times according to the product content of the card.
    
*   Only [Overseas Markup Fee Rate and Collection Conditions](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6) is registered in the Card Program, while the other items are registered in the Card Product.
    

* * *

## 1\. Card Type

Select the card type for each Card Product from either “**Physical**” or “**Virtual**”.

**Physical**

*   A Physical card is sent to the user.
    
*   The type of Physical card can be chosen from the following:
    
    *   IC card (contact/contactless dual IC card)
        
    *   Magnetic card
        
*   When creating a card, you can choose between auto-assignment or manual assignment for the PIN (personal identification number).
    

* * *

**When using manual assignment for the PIN**

*   Before setting the PIN, the partner should verify the following information about the target user to ensure the PIN is not easily predictable from personal information.
    
    *   Date of birth, phone number (home and mobile)
        
    *   Other personal information
        
    *   Combination of the above
        
*   Set the PIN item in the [“Create Card” API](https://api-doc.connect.xard.jp/#operation/createCard).
    
*   Users can execute the [“Get PIN” API](https://api-doc.connect.xard.jp/#operation/getPin) to check the registered PIN.
    
*   The PIN is subject to PCIDSS. Partners should review compliance with PCIDSS policies.
    

**Virtual**

*   A virtual card is created (a Physical card is not created).
    
*   To check the card information of the virtual card, users should execute the [“Get Card’s Sensitive Information” API](https://api-doc.connect.xard.jp/#operation/sensitiveData).
    

* * *

## 2\. Activate Type

Select the activate type for each Card Product from either “**Activation Required**” or “**Activation Not Required**”.

**Activation Required**

*   Can only be selected if the card type is “Physical”.
    
*   An activation code and QR code are printed on the cover sheet when the card is sent.
    
*   Users can use the card by activating it in one of the following ways:
    
    *   Enter the activation code on the screen provided by the partner.
        
    *   Scan the QR code and authenticate on the screen provided by the partner.
        

**Activation Not Required**

Users can use the card without activating it.

* * *

# 3\. Design of Face, Cover Sheet, and Envelope

Create the following for each Card Product.

**Design for Physical Card Face**

This is the face design of the Physical card. Create in accordance with the regulations for business cards of international brands.  
Coordinate with the printing company for the design, and obtain approval from the international brand for the final design.

**Design for Physical Card Cover Sheet**

This is the design of the cover sheet when the Physical card is sent. Coordinate with the printing company for the design.

**Design for Physical Card Envelope**

This is the design of the envelope when the Physical card is sent. Coordinate with the printing company for the design.

**Design for Card Widget**

This is the design of the screen displayed when users inquire about card information using the card widget function. Create following the regulations for virtual accounts of international brands.  
Obtain approval from the international brand for the final design.

It’s also possible to correspond to creating a leaflet to be enclosed when sending a Physical card.

*   The mailing method for Physical cards can be ordinary mail or simplified registered mail, specified in the Create Card API.
    
*   There are plans to support specific recorded mail in the future.
    

* * *

# 4\. Range of Card Number (PAN)

*   Set the range of card numbers to be assigned when issuing cards for each Card Product.
    
*   You can freely set between the 9th and 15th digits of the card number on the partner side.
    
    *   The first 1 to 8 digits of the card number are the partner’s BIN.
        
    *   The 16th digit of the card number is a check digit.
        
*   By dividing the range of the specified card number, it is possible to use the same BIN for multiple Card Products.
    

![image-20240304-023832.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-023832.png?api=v2)

Since the card number is issued randomly from the registered range of card numbers, you cannot partition a once-set range afterward.

For test purposes on the Xard side, we will use about the first 100 card numbers for each Card Product.

Example) Method for setting 9 to 15 digits

When issuing both Physical and Virtual cards with the same BIN

**Physical Card**

![image-20240304-025424.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025424.png?api=v2)

**Virtual Card**

![image-20240304-025617.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025617.png?api=v2)

※Specifiable from 100, as the first 100 are used by Xard.

* * *

# 5\. Overseas Markup Fee Rate and Collection Conditions

Settings for the following are made for each Card Program.

**Overseas Markup Fee Rate**

Set the percentage of overseas markup fees (fees incurred when using the card overseas).  
The standard fee rate is 3%, but you can set other percentages.  
The fee rate can be set to the second decimal place.

**Conditions for Collecting Overseas Markup Fees**

Set the conditions under which overseas markup fees will be collected. You can choose from the following two patterns.

Pattern 1:  
Standard Xard setting

Overseas markup fees are collected when the currency code is not Japanese Yen.

Pattern 2:  
Optional Setting (International Brand Standard)

The overseas markup fee will be collected if the following conditions are met.

[Visa]

Authorization: Determined as an overseas transaction if it matches at least one of the following conditions ①～③  
① Acquirer country code is other than "domestic"  
② International brand merchant country code is other than "JP"  
③ Currency is other than "Japanese Yen"  
Clearing: If the Settlement Flag relayed by Visa is other than "8 (domestic)"

[JCB]

Authorization, Clearing: If the Sender Center ID relayed by JCB is “1a996610000” (*ID for overseas transactions*)

The handling of overseas markup fees during returns at Xard is as follows.

For returns after sales confirmation: Overseas markup fees are not refunded.

For cancellations before sales confirmation: The overseas markup fees are included in the refund.