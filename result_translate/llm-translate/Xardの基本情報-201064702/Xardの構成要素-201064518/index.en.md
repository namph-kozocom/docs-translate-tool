The relationships and ID system of each element that constitutes Xard differ depending on whether balance management is conducted by a partner or by Xard.

The content of each configuration and element is as follows:

1.  [In the case of balance management by a partner (real-time switching method)](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#1.-%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%EF%BC%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F%EF%BC%89%E3%81%AE%E5%A0%B4%E5%90%88)
    
2.  [In the case of balance management by Xard](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#2.-Xard%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%E3%81%AE%E5%A0%B4%E5%90%88)
    

Regarding JCB, balance management by Xard is planned to be supported in the future. At present, it cannot be implemented.

* * *

## 1\. In the case of balance management by a partner (real-time switching method)

![](/wiki/download/attachments/201064518/XardConfiguration.png?api=v2)

**Partner**

Represents the partner company using Xard. A "**partner\_id**" is issued for each partner.

**Program**

Represents the service operated by the partner. A "**program\_id**" is issued for each Program.

Multiple Programs can be registered for one Partner.

**Program Gateway**

Represents the partner's endpoint in a Program with partner-managed balance. A "**program\_gateway\_id**" is issued for each Program.  
Only one Program Gateway is registered for one Program.

**Funding Source**

Indicates the source of balance charge. A "**funding\_source\_id**" is issued for each Funding Source.  
For a partner-managed balance Program, only one Funding Source is registered for one Program.

**Business**

Represents the corporation applying for the Program. A "**business\_id**" is issued for each corporation.  
Multiple Businesses can be registered for one Program.

**User**

Represents cardholders such as employees of the Business. A "**user\_id**" is issued for each User.  
Multiple Users can be registered for one Business.

**Account**

Represents the account (transaction information) of a Business or User. An "**account\_id**" is issued for each Account.  
One Account is registered for one Business or User. (The Account is created at the timing the [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) or [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) is created.)

**Card Product**

Represents the specifications of the card to be issued. A "**card\_product\_id**" is issued for each card specification.  
Multiple Card Products can be registered for one Program.

For details about Card Product registration content, refer to "[Card Specifications](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Card**

Represents the card owned by users. A "**card\_id**" is issued for each Card.  
Multiple Cards can be registered for one User.

**Client**

Represents the server or terminal connected to Xard. A "**client\_id**" and a "**client\_secret**" are issued for each Client.  
Multiple Clients can be registered for one Program.

**Hook**

Represents events notified from Xard to the partner.  
You can select whether or not to notify for each event.  
For events that can be notified, refer to the "Hook" in the API-DOC ([Hook](https://api-doc.connect.xard.jp/#tag/Hook)).

* * *

## 2\. In the case of balance management by Xard

![](/wiki/download/attachments/201064518/XardConfiguration-02.png?api=v2)

**Partner**

Represents the partner company using Xard. A "**partner\_id**" is issued for each partner.

**Program**

Represents the service operated by the partner. A "**program\_id**" is issued for each Program.

Multiple Programs can be registered for one Partner.

**Funding Source**

Indicates the source of balance charge. A "**funding\_source\_id**" is issued for each Funding Source.  
In a Virtual Account type Program, multiple Funding Sources can be registered for one Business or User.

**Business**

Represents the corporation applying for the Program. A "**business\_id**" is issued for each corporation.  
Multiple Businesses can be registered for one Program.

**User**

Represents cardholders such as employees of the Business. A "**user\_id**" is issued for each User.  
Multiple Users can be registered for one Business.

**Account**

Represents the account (transaction information) of a Business or User. An "**account\_id**" is issued for each Account.  
One Account is registered for one Business or User.  
(The Account is created at the timing the [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) or [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) is created.)

**Card Product**

Represents the specifications of the card to be issued. A "**card\_product\_id**" is issued for each card specification.  
Multiple Card Products can be registered for one Program.

For details about Card Product registration content, refer to "[Card Specifications](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Card**

Represents the card owned by users. A "**card\_id**" is issued for each Card.  
Multiple Cards can be registered for one User.

**Client**

Represents the server or terminal connected to Xard. A "**client\_id**" and a "**client\_secret**" are issued for each Client.  
Multiple Clients can be registered for one Program.

**Hook**

Represents events notified from Xard to the partner.  
You can select whether or not to notify for each event.  
For events that can be notified, refer to the "Hook" in the API-DOC ([Hook](https://api-doc.connect.xard.jp/#tag/Hook)).