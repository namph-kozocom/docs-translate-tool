The relationship between the elements that make up Xard and the ID system differ depending on whether balance management is done by a partner or by Xard.

The contents of each structure/element are as follows:

1.[For partner balance management (real-time switching method)](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#1.-%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%EF%BC%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F%EF%BC%89%E3%81%AE%E5%A0%B4%E5%90%88)

2.[For balance management with Xard](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#2-


For JCB, balance management using Xard will be supported in the future.This is not possible at this time.

* * *

## 1\. In case of balance management by partner (real-time switching method)

![](/wiki/download/attachments/201064518/XardConfiguration.png?api=v2)

**Partner**

Represents a partner company that uses Xard.A "**partner\_id**" is issued for each partner.

**Program**

Represents a service operated by a partner."**program\_id**" is issued for each program.

Multiple programs can be registered for one Partner.

**Program Gateway**

Represents the endpoint on the Partner side in a balance management type program by the partner."**program\_gateway\_id**" is issued for each program.
Register one Program Gateway for one Program.

**Funding Source**

Represents the charge source for the balance."**funding\_source\_id**" will be issued for each Funding Source.
For balance management type programs by partners, one Funding Source is registered for one program.

**Business**

Represents the corporation applying for the Program.A "**business\_id**" is issued for each legal entity.
Multiple businesses can be registered for one program.

**User**

Represents a cardholder, such as a Business employee."**user\_id**" is issued for each User.
Multiple users can be registered for one business.

**Account**

Represents a Business or User account (transaction information)."**account\_id**" will be issued for each account.
Register one Account for one Business or User.(An Account will be created when [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) and [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) are created.)

**Card Product**

Indicates the specifications of the issued card."**card\_product\_id**" is issued for each card specification.
Multiple Card Products can be registered for one Program.

For more information about Card Product registration, see "[Card specifications](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Card**

Represents a card owned by a user."**card\_id**" will be issued for each Card.
Multiple Cards can be registered for one User.

**Client**

Represents a server or terminal that connects to Xard."**client\_id**" and "**client\_secret**" are issued for each Client.
Multiple Clients can be registered for one Program.

**Hook**

Represents an event that Xard notifies partners about.
You can choose whether to receive notifications for each event.
For events that can be notified, please refer to "[Hook](https://api-doc.connect.xard.jp/#tag/Hook)" in API-DOC.

* * *

## 2\. For balance management using Xard

![](/wiki/download/attachments/201064518/XardConfiguration-02.png?api=v2)

**Partner**

Represents a partner company that uses Xard.A "**partner\_id**" is issued for each partner.

**Program**

Represents a service operated by a partner."**program\_id**" is issued for each program.

Multiple programs can be registered for one Partner.

**Funding Source**

Represents the charge source for the balance."**funding\_source\_id**" will be issued for each Funding Source.
In Virtual Account type programs, multiple Funding Sources can be registered for one Business or User.

**Business**

Represents the corporation applying for the Program.A "**business\_id**" is issued for each legal entity.
Multiple businesses can be registered for one program.

**User**

Represents the card owner, such as a Business employee."**user\_id**" is issued for each User.
Multiple users can be registered for one business.

**Account**

Represents a Business or User account (transaction information)."**account\_id**" will be issued for each account.
Register one Account for one Business or User.
(An Account will be created when [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) and [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) are created.)

**Card Product**

Indicates the specifications of the issued card."**card\_product\_id**" is issued for each card specification.
Multiple Card Products can be registered for one Program.

For more information about Card Product registration, see "[Card specifications](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Card**

Represents a card owned by a user."**card\_id**" will be issued for each Card.
Multiple Cards can be registered for one User.

**Client**

Represents a server or terminal that connects to Xard."**client\_id**" and "**client\_secret**" are issued for each Client.
Multiple Clients can be registered for one Program.

**Hook**

Represents an event that Xard notifies partners about.
You can choose whether to receive notifications for each event.
For events that can be notified, please refer to "[Hook](https://api-doc.connect.xard.jp/#tag/Hook)" in API-DOC.