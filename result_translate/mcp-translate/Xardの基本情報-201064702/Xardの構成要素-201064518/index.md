Xardを構成する各要素の関係性およびIDの体系は、残高管理をパートナーで行うかXardで行うかによって異なります。

それぞれの構成・要素の内容は以下のとおりです：

1.  [パートナーによる残高管理（リアルタイムスイッチング方式）の場合](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#1.-%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%EF%BC%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F%EF%BC%89%E3%81%AE%E5%A0%B4%E5%90%88)
    
2.  [Xardによる残高管理の場合](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#2.-Xard%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%E3%81%AE%E5%A0%B4%E5%90%88)
    

JCBについては、Xardによる残高管理は今後対応予定です。現時点では実施できません。

* * *

## 1\. パートナーによる残高管理（リアルタイムスイッチング方式）の場合

![](/wiki/download/attachments/201064518/XardConfiguration.png?api=v2)

**Partner**

Xardを利用するパートナー企業を表します。パートナーごとに「**partner\_id**」が発行されます。

**Program**

パートナーが運営するサービスを表します。Programごとに「**program\_id**」が発行されます。

1つのPartnerに対して、複数のProgramを登録できます。

**Program Gateway**

パートナーによる残高管理型のProgramにおける、Partner側のエンドポイントを表します。Programごとに「**program\_gateway\_id**」が発行されます。  
1つのProgramに対して、1つのProgram Gatewayを登録します。

**Funding Source**

残高のチャージ元を表します。Funding Sourceごとに「**funding\_source\_id**」が発行されます。  
パートナーによる残高管理型のProgramでは、1つのProgramに対して、1つのFunding Sourceを登録します。

**Business**

Programに申し込む法人を表します。法人ごとに「**business\_id**」が発行されます。  
1つのProgramに対して、複数のBusinessを登録できます。

**User**

Businessの従業員など、カード所有者を表します。Userごとに「**user\_id**」が発行されます。  
1つのBusinessに対して、複数のUserを登録できます。

**Account**

BusinessまたはUserの口座（取引情報）を表します。Accountごとに「**account\_id**」が発行されます。  
1つのBusinessまたはUserに対して、1つのAccountを登録します。（[Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business)、[User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User)が作成されたタイミングでAccountが作成されます。）

**Card Product**

発行するカードの仕様を表します。カードの仕様ごとに「**card\_product\_id**」が発行されます。  
1つのProgramに対して、複数のCard Productを登録できます。

Card Productの登録内容について詳しくは、「[カードの仕様](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)」を参照してください。

**Card**

ユーザーが所有するカードを表します。Cardごとに「**card\_id**」が発行されます。  
1つのUserに対して、複数のCardを登録できます。

**Client**

Xardに接続するサーバーまたは端末を表します。Clientごとに「**client\_id**」と「**client\_secret**」が発行されます。  
1つのProgramに対して、複数のClientを登録できます。

**Hook**

Xardからパートナーに通知するイベントを表します。  
イベントごとに通知の有無を選択できます。  
通知可能なイベントは、API-DOCの「[Hook](https://api-doc.connect.xard.jp/#tag/Hook)」を参照してください。

* * *

## 2\. Xardによる残高管理の場合

![](/wiki/download/attachments/201064518/XardConfiguration-02.png?api=v2)

**Partner**

Xardを利用するパートナー企業を表します。パートナーごとに「**partner\_id**」が発行されます。

**Program**

パートナーが運営するサービスを表します。Programごとに「**program\_id**」が発行されます。

1つのPartnerに対して、複数のProgramを登録できます。

**Funding Source**

残高のチャージ元を表します。Funding Sourceごとに「**funding\_source\_id**」が発行されます。  
Virtual Account型のProgramでは、1つのBusinessまたはUserに対して、複数のFunding Sourceを登録できます。

**Business**

Programに申し込む法人を表します。法人ごとに「**business\_id**」が発行されます。  
1つのProgramに対して、複数のBusinessを登録できます。

**User**

Businessの従業員など、カードの所有者を表します。Userごとに「**user\_id**」が発行されます。  
1つのBusinessに対して、複数のUserを登録できます。

**Account**

BusinessまたはUserの口座（取引情報）を表します。Accountごとに「**account\_id**」が発行されます。  
1つのBusinessまたはUserに対して、1つのAccountを登録します。  
（[Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business)、[User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User)が作成されたタイミングでAccountが作成されます。）

**Card Product**

発行するカードの仕様を表します。カードの仕様ごとに「**card\_product\_id**」が発行されます。  
1つのProgramに対して、複数のCard Productを登録できます。

Card Productの登録内容について詳しくは、「[カードの仕様](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)」を参照してください。

**Card**

ユーザーが所有するカードを表します。Cardごとに「**card\_id**」が発行されます。  
1つのUserに対して、複数のCardを登録できます。

**Client**

Xardに接続するサーバーまたは端末を表します。Clientごとに「**client\_id**」と「**client\_secret**」が発行されます。  
1つのProgramに対して、複数のClientを登録できます。

**Hook**

Xardからパートナーに通知するイベントを表します。  
イベントごとに通知の有無を選択できます。  
通知可能なイベントは、API-DOCの「[Hook](https://api-doc.connect.xard.jp/#tag/Hook)」を参照してください。